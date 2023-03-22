from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/getrgb', methods=['GET'])
def get_rgb():
    url = request.args.get('url')
    if not url:
        return 'No URL specified'

    try:
        with urlopen(url) as img_url:
            img = Image.open(BytesIO(img_url.read()))
            width, height = img.size
            rgb_data = [list(rgb) for rgb in img.getdata()]
            return_string = '{'
            return_string += ','.join([f'{{{rgb[0]},{rgb[1]},{rgb[2]}}}' for i, rgb in enumerate(rgb_data)])
            return_string += ',info={'
            return_string += f'{width},{height}'
            return_string += '}}'
            return return_string
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
