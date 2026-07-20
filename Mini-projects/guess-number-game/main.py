import random
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-me"  # fine for local play, swap out before deploying anywhere

MAX_ATTEMPTS = 5
LOW, HIGH = 1, 100


def new_game():
    session["secret"] = random.randint(LOW, HIGH)
    session["attempts_used"] = 0
    session["history"] = []
    session["over"] = False


@app.route("/")
def index():
    if "secret" not in session:
        new_game()
    return render_template("index.html", low=LOW, high=HIGH, max_attempts=MAX_ATTEMPTS)


@app.route("/api/state")
def state():
    if "secret" not in session:
        new_game()
    return jsonify({
        "attempts_used": session["attempts_used"],
        "max_attempts": MAX_ATTEMPTS,
        "history": session["history"],
        "over": session["over"],
    })


@app.route("/api/new-game", methods=["POST"])
def api_new_game():
    new_game()
    return jsonify({"ok": True})


@app.route("/api/guess", methods=["POST"])
def api_guess():
    if "secret" not in session:
        new_game()

    if session.get("over"):
        return jsonify({"error": "Game's already over, start a new one!"}), 400

    data = request.get_json(silent=True) or {}
    guess = data.get("guess")

    if not isinstance(guess, int) or not (LOW <= guess <= HIGH):
        return jsonify({"error": f"Guess has to be a whole number between {LOW} and {HIGH}."}), 400

    secret = session["secret"]
    session["attempts_used"] += 1
    attempts_used = session["attempts_used"]
    attempts_left = MAX_ATTEMPTS - attempts_used
    diff = abs(guess - secret)

    won = guess == secret
    out_of_tries = attempts_left <= 0 and not won

    if won:
        result = "win"
        hint = "boom"
    elif out_of_tries:
        result = "lose"
        hint = "over"
    elif diff <= 10 and guess < secret:
        result = "continue"
        hint = "warm_low"
    elif diff <= 10 and guess > secret:
        result = "continue"
        hint = "warm_high"
    elif guess < secret:
        result = "continue"
        hint = "cold_low"
    else:
        result = "continue"
        hint = "cold_high"

    session["history"].append({"guess": guess, "hint": hint})
    session["history"] = session["history"]  # force session to notice the mutation
    session.modified = True

    if won or out_of_tries:
        session["over"] = True

    return jsonify({
        "result": result,
        "hint": hint,
        "diff": diff,
        "attempts_used": attempts_used,
        "attempts_left": max(attempts_left, 0),
        "over": session["over"],
        "secret": secret if session["over"] else None,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)