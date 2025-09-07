**CodeGuru – AI Code Assistant**

CodeGuru is a coding assistant I built using Ollama and Gradio.
It’s more than just a chatbot – it can explain code step by step, quiz you with coding questions, and give answers in a clean IDE-style interface with syntax highlighting.

__What it can do:__

Answer coding questions in a chat format <br>
Explain Mode → break down code like a tutor <br>
Learning Mode → ask coding quizzes and debugging challenges <br>
Dark, IDE-inspired UI with proper code formatting

__Tech I used:__

Ollama → runs the large language model locally (fast, private, no API costs) <br>
Modelfile → defines the "CodeGuru" assistant personality and behavior <br>
Gradio → powers the chat interface with toggles for different modes <br>
Markdown + CSS → makes the answers look like real code with syntax highlighting <br>
Python (requests, langchain) → handles API calls and leaves room for future extensions

__Getting Started:__

Install Ollama
 and run the model:

ollama run codeguru


__Clone the repo and install dependencies:__

git clone https://github.com/yourusername/codeguru.git
cd codeguru
pip install -r requirements.txt


__Start the app:__

python app.py


Open http://127.0.0.1:7860
 in your browser
