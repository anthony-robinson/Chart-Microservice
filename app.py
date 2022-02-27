from flask import Flask, request, send_file
from quickchart import QuickChart

app = Flask(__name__)

@app.route("/line_chart", methods=['POST'])
def get_chart():
    path = request.json['path']
    width = int(request.json['width'])
    height = int(request.json['height'])
    data = request.json['data']
    options = {}
    if 'options' in request.json:
        options = request.json['options']
    create_line_chart(path, width, height, data, options)
    return send_file(path, mimetype='image/gif')


def create_line_chart(path, width, height, data, options={}):
    qc = QuickChart()
    qc.width = width
    qc.height = height
    qc.device_pixel_ratio = 2.0
    print(options)
    qc.config = {
        "type": "line",
        "data": data,
        "options": options
    }
    print(qc.config)
    qc.to_file(path)

if __name__ == "__main__":
    app.run()