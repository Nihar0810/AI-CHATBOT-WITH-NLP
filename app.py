from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Chatbot responses dictionary
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm great!", "Doing well, thank you!"],
    "bye": ["Goodbye!", "See you!", "Bye!"],
    "what is your name": ["I'm your chatbot!", "Call me ChatBot!"],
    "thank you": ["You're welcome!", "Anytime!", "No problem!"],
    "what can you do": ["I can chat with you!", "I answer simple questions."],
    "who made you": ["I was made by a Python developer!", "Someone smart built me!"],
    "help": ["Tell me what you need help with.", "I'm here to assist!"]
}

# Simple rule-based reply generator
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    bot_reply = get_response(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
