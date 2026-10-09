import random
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    guess = int(request.form["guess"])
    print(guess)
    return "Your guess was recivied"
sec_num=random.randint(1, 100)

if __name__ == "__main__":
 app.run(debug=True, port=5000)



