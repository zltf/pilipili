from flask import Flask
from flask import send_file
import logging
import datetime

from api.music import api_music

import config

app = Flask(__name__, static_folder = 'static')

app.register_blueprint(api_music)

@app.route('/')
def index():
    return send_file('static/index.html')

if __name__ == '__main__':
    handler = logging.FileHandler(config.LOG_PATH + 'flask.' + datetime.datetime.today().strftime('%Y-%m-%d_%H:%M:%S') + '.log', encoding='UTF-8')
    handler.setLevel(logging.INFO)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=config.PORT)
