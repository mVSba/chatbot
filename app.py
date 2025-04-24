import os
import logging
from flask import Flask, render_template, request, jsonify, session
from chatbot import get_response

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-dev-secret-key")

@app.route("/")
def home():
    # Initialize chat history if it doesn't exist
    if "chat_history" not in session:
        session["chat_history"] = []
        # Add a welcome message
        session["chat_history"].append({
            "sender": "bot",
            "message": "Hi there! I'm here to help you through difficult moments. If you're experiencing a panic attack or anxiety, I can offer some coping techniques. How are you feeling right now?"
        })
        session.modified = True
    
    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.form.get("message", "").strip()
    
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    
    # Add user message to chat history
    if "chat_history" not in session:
        session["chat_history"] = []
    
    session["chat_history"].append({
        "sender": "user",
        "message": user_message
    })
    
    # Get bot response
    bot_response = get_response(user_message)
    
    # Add bot response to chat history
    session["chat_history"].append({
        "sender": "bot",
        "message": bot_response
    })
    
    session.modified = True
    
    return jsonify({
        "user_message": user_message,
        "bot_response": bot_response
    })

@app.route("/reset_chat", methods=["POST"])
def reset_chat():
    session.pop("chat_history", None)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
