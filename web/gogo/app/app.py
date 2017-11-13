from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def page():
    data = request.cookies.get("logged_in")
    if data == "1":
        response = make_response(render_template("main.html"))
    else:
        response = make_response(render_template("denied.html"))
    if data is None:
        response.set_cookie("logged_in", "0")
    return response


@app.route('/process/', methods=["POST"])
def process():
    if request.cookies.get("logged_in", None) != "1":
        return "error"

    password = request.form.get("password", None)
    if password == "Qwerty123":
        return render_template("flag.html")
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
