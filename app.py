from pricefetch import yup
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    #print("HW")
    return render_template('crypto.html')

if __name__== "__main__":
    app.run(debug=True, port=8000)
# print(yup('BTC'))
# print(yup('ETH'))
# print(yup('SOL'))
# print(yup('LTC'))
# print(yup('DOGE'))
# print(yup('ADA'))
# print(yup('SHIB'))

