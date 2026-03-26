#request metode GET/ POST
from flask import Flask, render_template, request,make_response
import random

app = Flask(__name__)

#združen GET / POST route
stop = False
stevec= 0
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["fname"]
        resp = make_response(render_template("metode.html", user = user) )
        resp.set_cookie('user',user)
        return resp

# treavb narediti še za logout
    return render_template("login.html")

@app.route("/", methods = ["GET", "POST"]) #če nič ne damo metode potem je ssmo privzeto GET dovoljeno
def hello_world():
    global user
    global stop
    #head = request.headers
    if request.method == "GET":
        #request.args
        user = request.cookies.get('user')
        resp = make_response(render_template("metode.html", user = user)) 
        resp.set_cookie('user',user)
        return resp
    elif request.method == "POST":
        global stevec
        stevec = stevec  + 1
        print(request.form)
        num = str(random.randint(1, 150))
        if num == "13":
            stop = True
            bes = f"JOJ zadel si številko 13, konec je... \nŠt. poskusol:{stevec}"
            return {"status":bes,"run":stop}
        return {"status":num}
    print(request.method)

app.run(debug=True)