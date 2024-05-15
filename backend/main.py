from flask import Flask, jsonify, request
from flask_cors import CORS

from encode import *

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests


@app.route('/api/search', methods=['POST'])
def clip():
    data = request.get_json()
    caption = data.get('caption')

    image_list, text_list = get_image_text_list_from_text_file()

    count = 5
    image_index = get_image_from_text(
        caption=caption,
        count=count,
        image_list=image_list,
        plot_or_not=False
    )

    return jsonify(image_index)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
