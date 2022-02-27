from pricefetch import yup
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        btc = request.form["amountbtc"]
        tbtc = float(btc)*yup('BTC')*0.3

        return redirect(url_for("user",usr=tbtc))
    else:
        return render_template("crypto.html")


@app.route("/<usr>")
def user(usr):
    return render_template("crypto.html",usr=usr)

if __name__== "__main__":
    app.run(debug=True, port=8000)

