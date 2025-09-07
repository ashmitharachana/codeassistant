CodeGuru – AI Code Assistant

CodeGuru is a coding assistant I built using Ollama and Gradio.
It’s more than just a chatbot – it can explain code step by step, quiz you with coding questions, and give answers in a clean IDE-style interface with syntax highlighting.

What it can do:

Answer coding questions in a chat format
Explain Mode → break down code like a tutor
Learning Mode → ask coding quizzes and debugging challenges
Dark, IDE-inspired UI with proper code formatting

Tech I used:

Ollama - runs the large language model locally (fast, private, no API costs)
Modelfile - defines the "CodeGuru" assistant personality and behavior
Gradio - powers the chat interface with toggles for different modes
Markdown + CSS -makes the answers look like real code with syntax highlighting
Python (requests, langchain) - handles API calls and leaves room for future extensions

Getting Started:

Install Ollama
 and run the model:

ollama run codeguru


Clone the repo and install dependencies:

git clone https://github.com/yourusername/codeguru.git
cd codeguru
pip install -r requirements.txt


Start the app:

python app.py


Open http://127.0.0.1:7860
 in your browsers

