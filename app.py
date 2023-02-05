from flask import Flask, send_from_directory, make_response
import mimetypes

app = Flask(__name__, static_folder=None)


@app.route('/')
def hello_world():
    return send_from_directory('client/dist', 'index.html')


# Path for the rest of the static files (JS/CSS)
@app.route('/<path:path>')
def assets(path):
    mimetype = path if mimetypes.guess_type(path)[0] == "text/plain" else mimetypes.guess_type(path)[0]
    if ".js" in mimetype:
        mimetype = "text/javascript"
    response = make_response(send_from_directory('client/dist', path))
    response.headers['Content-Type'] = mimetype
    return response


if __name__ == '__main__':
    app.run(debug=True)
