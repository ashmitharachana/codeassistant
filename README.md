CodeGuru – AI Code Assistant

CodeGuru is an AI-powered coding assistant built with Ollama and Gradio, designed to help developers write, debug, and learn code in an IDE-like chat interface.

🚀 Features

💬 Chat-style Assistant – answer coding questions in real time
🔎 Explain Mode – step-by-step explanation of code
📚 Learning Mode – coding quizzes & debugging challenges
🎨 IDE-Themed Dark UI – syntax highlighting + developer fonts

🛠️ Tech Stack

Ollama → runs local LLMs (fast, private, offline)
Modelfile → defines model behavior (CodeGuru personality)
Gradio → interactive chat UI with custom CSS styling
Markdown → renders clean, syntax-highlighted code blocks
Python (requests, langchain) → backend API calls & future extensions

⚡ Setup
1️⃣ Install Ollama

Download from Ollama
 and run the model:

ollama run codeguru

2️⃣ Clone & Install
git clone https://github.com/yourusername/codeguru.git
cd codeguru
pip install -r requirements.txt

3️⃣ Run the App
python app.py


Open http://127.0.0.1:7860
 in your browser


 Future Improvements
 Code-to-Flowchart visualization

 Save & reuse code snippets

 Run code sandbox for Python snippets

 Voice-to-Code support

