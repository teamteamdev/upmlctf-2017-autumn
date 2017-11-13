from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('register.html')


@app.route('/personal/')
def flag():
    return render_template('denied.html')


@app.route('/process/', methods=["GET", "POST"])
def process():
    return redirect('/personal/?flag=uctf_why_is_flag_here')

if __name__ == '__main__':
    app.run()
