from flask import Flask, render_template
import socket
from datetime import date
import os

app = Flask(__name__)

@app.route("/")
def home():
    today = date.today()
    hostname = socket.gethostname()
    fqdn = socket.getfqdn()
    ip_address = socket.gethostbyname(hostname)

    return render_template(
        "index.html",
        today=today,
        hostname=hostname,
        fqdn=fqdn,
        ip_address=ip_address
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)


