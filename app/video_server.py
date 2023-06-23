from flask import Flask, Response, stream_with_context

app = Flask(__name__)


@app.route('/video')
def stream_video():
    video_path = 'drone_herd.mp4'

    def generate():
        with open(video_path, 'rb') as video_file:
            while True:
                chunk = video_file.read(1024 * 1024)  # reading in 1MB chunks
                if not chunk:
                    break
                yield chunk

    return Response(stream_with_context(generate()), content_type='video/mp4')


if __name__ == '__main__':
    app.run(port=5000)