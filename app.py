from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

client = genai.Client(api_key="AIzaSyDVdWZ1U24A1dFi4pHVahHucTqJk5T0800")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message'].lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 😊 How can I help you?"

    elif "joke" in user_input:
        return "Why don’t programmers like nature? Because it has too many bugs 😂"

    elif "study" in user_input:
        return "Try studying in 25-minute focused sessions with short breaks 📚"

    elif "ai" in user_input:
        return "AI (Artificial Intelligence) allows machines to think, learn, and solve problems like humans 🤖"

    elif "smart assistant" in user_input:
        return "A smart assistant is a program that helps users by answering questions, giving suggestions, and automating tasks 🤖✨"

    elif "who are you" in user_input:
        return "I am your Smart Assistant built by you 😎"

    elif "time" in user_input:
        from datetime import datetime
        return f"Current time is {datetime.now().strftime('%H:%M:%S')} ⏰"

    elif "my name" in user_input:
        return "I don’t know your name yet 😄 but you can tell me!"

    elif "student" in user_input:
        return "That's awesome! 🎓 I can help you with study tips and learning strategies 📚"

    elif "motivate" in user_input:
        return "Keep going! 💪 Small progress every day leads to big success 🚀"

    elif "help" in user_input:
        return "I can help with study tips, AI basics, and simple questions 😊"

    elif "bye" in user_input:
        return "Goodbye! 👋 Have a productive day!"

    else:
        return "That's a great question! 🤔 I'm still improving, but I can help with study tips, AI basics, and more 🚀"

if __name__ == '__main__':
    app.run(debug=True)