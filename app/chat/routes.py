from flask import jsonify, request, render_template
from flask_login import login_required
from . import bp
from .rag import RAGChat

rag_chat = RAGChat()

@bp.route('/')
#@login_required
def index():
    return render_template('chat/index.html')

@bp.route('/chat', methods=['POST'])
#@login_required
def chat():
    data = request.json
    response = rag_chat.get_response(data['message'])
    return jsonify({'response': response})