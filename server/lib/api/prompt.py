import logging
import json
import requests

from .response_utils import create_response_message
from ..entities import Prompt, PromptEncoder

from flask import g, request, jsonify, Blueprint, current_app

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

prompt_bp = Blueprint('prompt', __name__, url_prefix='/prompt')

@prompt_bp.before_app_request
def set_app_context():
    g.app = current_app


@prompt_bp.route('/<string:prompt_id>')
def get_prompt(prompt_id):
    storage = g.get('storage')
    if prompt_id not in storage.prompts:
        return f'No prompt found for id: {prompt_id}', 400
    return current_app.response_class(
        response=json.dumps(storage.prompts[prompt_id], cls=PromptEncoder),
        status=200,
        mimetype='application/json',
        headers={'Access-Control-Allow-Origin': '*'}
    )
