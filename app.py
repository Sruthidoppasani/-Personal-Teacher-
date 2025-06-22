from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import markdown  # ✅ Converts Markdown to HTML

app = Flask(__name__)
CORS(app)

# Configure Gemini
genai.configure(api_key="Enter your API Key")
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
        markdown_response = response.text

        # ✅ Convert Markdown to HTML
        html_response = markdown.markdown(markdown_response, extensions=["tables"])

        return jsonify({"response": html_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
