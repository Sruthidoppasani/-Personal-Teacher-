from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to access backend API

# Configure Gemini API
genai.configure(api_key="AIzaSyCqPgAQTdbtN1B7dPJ8b_3A5gtrLQ3PrF0")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
chat = model.start_chat()

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.json
    user_input = data.get("message", "")
    
    if not user_input:
        return jsonify({"error": "No message received"}), 400

    try:
        response = chat.send_message(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
