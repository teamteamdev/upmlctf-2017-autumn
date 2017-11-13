from flask import Flask, session

app = Flask(__name__)


@app.route('/')
def main():
    count = int(session.get("count", "2017"))
    if count == 0:
        session["count"] = 31338
        session["joke"] = True
        return '''<meta charset="utf-8" /><p><b>Успех!<b> Держи флаг: <b>uctficandomanyrequests</b>.</p><p><i>Обнови страницу для получения супер-бонуса</i></p>'''
    else:
        session["count"] = count - 1
        if session.get("joke", False):
            session["joke"] = None
            hint = "<p><i>Это была шутка, никакого бонуса, конечно же, нет. Не доверяй мошенникам в интернете! (если ты не скопировал флаг, то это реально печально)</i></p>"
        elif count <= 1990:
            hint = "<p><i>Ты не думаешь, что нажимать <b>F5</b> много раз &ndash; не лучшая идея?</i></p>"
        else:
            hint = ""
        return '''<meta charset="utf-8"/><p>Извини :( Чтобы найти флаг, тебе нужно открыть эту страницу ещё <b>{}</b> раз.</p>{}'''.format(count, hint)

app.secret_key = 's4pmby6ptl8eabizdh8lp0avld52ke25'

if __name__ == "__main__":
    app.run()

