from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"
@app.route("/about")
def about():
    return "<h1>Hello, world this my frist flask app!</h1>"
@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "you are sand data"
    else:
        return "you are only veiwing the form"
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
