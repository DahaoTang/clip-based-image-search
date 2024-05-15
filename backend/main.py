from flask import Flask, jsonify, request
from flask_cors import CORS

from utils import *

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests


@app.route('/api/search', methods=['POST'])
def clip():
    data = request.get_json()
    caption = data.get('caption')

    image_list, caption_list = get_image_and_caption_list()

    count = 12 * 5 # In the database, each image contains 5 different descriptions and hence appears 5 times in captions.txt

    image_index = get_image_from_caption(
        user_caption=caption,
        count=count,
        image_list=image_list,
        plot_or_not=False
    )

    return jsonify(list(set(image_index))) # Remove duplicated images


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
