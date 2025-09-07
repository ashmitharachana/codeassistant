import requests, json, gradio as gr
import markdown

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
history = []

def generate_response(message, history_gradio, explain_mode, learning_mode):
    global history
    history.append(message)

    # Handle different modes
    if learning_mode:
        final_prompt = (
            "\n".join(history)
            + "\n\nYou are a coding teacher. Ask me a short programming question "
            "or debugging challenge (like MCQ or small snippet to fix). "
            "After I answer, evaluate whether I am right or wrong."
        )
    elif explain_mode:
        final_prompt = "\n".join(history) + "\n\nExplain this code step by step like a teacher."
    else:
        final_prompt = "\n".join(history)

    data = {"model": "codeguru", "prompt": final_prompt, "stream": False}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = json.loads(response.text)
        actual_response = data['response']

        # Render with markdown (for code blocks / formatting)
        html_response = markdown.markdown(
            actual_response, extensions=["fenced_code", "codehilite"]
        )
        return html_response
    else:
        return "Error: " + response.text


# Custom CSS (coding theme + syntax highlighting)
css = """
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Fira Code', monospace;
    color: #dcdcdc;
}
#chatbot {
    background-color: #1e1e1e !important;
    border-radius: 12px;
    border: 1px solid #444;
    padding: 10px;
}
.chatbot .user {
    background: #0d1117 !important;
    color: #58a6ff !important;
    border-radius: 8px;
    padding: 6px;
    margin: 4px;
    font-family: 'Fira Code', monospace;
}
.chatbot .assistant {
    background: #161b22 !important;
    color: #dcdcdc !important;
    border-radius: 8px;
    padding: 6px;
    margin: 4px;
    font-family: 'Fira Code', monospace;
}
textarea {
    background-color: #0d1117 !important;
    color: #00ff9f !important;
    font-family: 'Fira Code', monospace;
    border-radius: 8px;
    border: 1px solid #333;
}
pre code {
    background-color: #0d1117 !important;
    color: #00ff9f;
    padding: 8px;
    border-radius: 8px;
    display: block;
    overflow-x: auto;
}
"""

# ChatInterface with Explain + Learning mode
chatbot = gr.ChatInterface(
    fn=generate_response,
    additional_inputs=[
        gr.Checkbox(label="🔎 Explain Code Mode", value=False),
        gr.Checkbox(label="📚 Learning Mode", value=False)
    ],
    title="💻 Code Assistant",
    description="Write, debug, explain, or practice coding challenges ✨",
    theme="base",
    css=css
)

chatbot.launch()
