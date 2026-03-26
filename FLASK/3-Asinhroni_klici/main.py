from flask import Flask, request, render_template, jsonify
import random
import requests #(mi kličemo)
#pip install flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/coinFlip")
def coin_flip():
    return render_template("coin.html")

@app.route("/coinData")
# če bi želeli z POST request.form
# GET
def coinData():
    print(request.args["vrednost"])
    rnd = random.randint(0,1)
    status = ["TAILS", "HEADS"][rnd]
    slika = ["https://postimg.cc/zysdXN8w","https://i.postimg.cc/3NM63XwM/head.png"][rnd]
    return {"img":slika, "status":status}

@app.route("/randomQuote")
def randomQuote():
    pass

@app.route("/debug", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def debug_request():
    data = {
        # osnovno
        "method": request.method,
        "url": request.url,
        "base_url": request.base_url,
        "host": request.host,
        "path": request.path,
        "full_path": request.full_path,
        "scheme": request.scheme,

        # IP in povezava
        "remote_addr": request.remote_addr,
        "access_route": list(request.access_route),

        # headers
        "headers": dict(request.headers),

        # parametri v URL (?a=1&b=2)
        "args": request.args.to_dict(flat=False),

        # form data
        "form": request.form.to_dict(flat=False),

        # JSON body
        "json": request.get_json(silent=True),

        # raw body
        "data_raw": request.data.decode("utf-8", errors="ignore"),

        # cookies
        "cookies": request.cookies,

        # files
        "files": {name: {
            "filename": file.filename,
            "content_type": file.content_type
        } for name, file in request.files.items()},

        # environment (WSGI)
        "environ": {k: str(v) for k, v in request.environ.items()}
    }

    return jsonify(data)
app.run(debug=True)

"""https://flask.palletsprojects.com/en/stable/quickstart/"""