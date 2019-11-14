from flask import Flask
from flask import render_template
from flask import Response
import video
import argparse

vc = None
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

def gen():
    global vc
    while True:
        frame = vc.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

def run():
    global app
    parser = argparse.ArgumentParser(description='A video streamer using flask')
    parser.add_argument("--h", default='0.0.0.0', help="http address, for example -h 127.0.0.1. Default is 0.0.0.0")
    parser.add_argument("--p", default=5000, help="port number, for example 4000. Default is 5000")
    args = parser.parse_args()
    app.run(host=args.h, port=args.p, debug=True)

vc = video.VideoCamera()
run()




