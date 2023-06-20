from flask import Flask, send_file

app = Flask(__name__)


@app.route('/video')
def stream_video():
    video_path = 'stock_monitoring.mp4'

    return send_file(video_path, as_attachment=False, mimetype='video/mp4')


if __name__ == '__main__':
    app.run(debug=True)
