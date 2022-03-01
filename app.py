from pricefetch import yup
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        btc = request.form["amountbtc"]
        eth = request.form["amounteth"]
        ltc = request.form["amountltc"]
        sol = request.form["amountsol"]
        doge = request.form["amountdoge"]
        shib = request.form["amountshib"]

        tbtc = float(btc)*yup('BTC')*0.3
        teth = float(eth)*yup('ETH')*0.3
        tltc = float(ltc)*yup('LTC')*0.3
        tsol = float(sol)*yup('SOL')*0.3
        tdoge = float(doge)*yup('DOGE')*0.3
        tshib = float(shib)*yup('SHIB')*0.3

        total = round(tbtc+teth+tltc+tsol+tdoge+tshib)

        return redirect(url_for("user",usr=total))
    else:
        return render_template("crypto.html")


@app.route("/<usr>")
def user(usr):
    return render_template("crypto.html",usr=usr)

if __name__== "__main__":
    app.run(debug=True, port=8000)

