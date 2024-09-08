from flask import Blueprint
from flask import current_app

api_music = Blueprint('api_music', __name__, url_prefix='/api/music')

@api_music.route("aaaa", methods=["POST"])
def aaaa():
    current_app.logger.info("aaaa")
    return "aaaa"
