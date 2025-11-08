from flask import Blueprint, request, jsonify
import google.genai as genai

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/gemini', methods=['POST'])
def chat_gemini():
    data = request.get_json()
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
    try:
        client = genai.Client() 
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
