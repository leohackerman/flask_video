from flask import Flask
from flask import render_template
from flask import Response
import video

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



vc = video.VideoCamera()
app.run(host='0.0.0.0',debug=True)




