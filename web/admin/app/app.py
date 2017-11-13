from flask import Flask, render_template, request, abort

app = Flask(__name__)


@app.route('/')
def page():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip == '10.8.0.111':
        return render_template("flag.html")
    else:
        abort(403)

if __name__ == '__main__':
    app.run()

