import os
import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key-change-me")

APP_NAME = os.getenv("APP_NAME", "Number Guessing Game")
APP_ENV = os.getenv("APP_ENV", "production")
APP_VERSION = "2.0.0"

# ✅ Единая настройка начального рекорда
DEFAULT_BEST_SCORE = 10


def init_game():
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)
        session["attempts"] = 0
        session["best_score"] = session.get("best_score", DEFAULT_BEST_SCORE)
        session["message"] = ""
        session["message_type"] = "info"


@app.route("/")
def index():
    init_game()
    return render_template(
        "index.html",
        app_name=APP_NAME,
        attempts=session.get("attempts", 0),
        best_score=session.get("best_score", DEFAULT_BEST_SCORE),
        message=session.get("message", ""),
        message_type=session.get("message_type", "info")
    )


@app.route("/guess", methods=["POST"])
def guess():
    init_game()

    user_input = request.form.get("guess", "").strip()

    try:
        guess_number = int(user_input)
    except ValueError:
        session["message"] = "Введи целое число от 1 до 100."
        session["message_type"] = "error"
        return redirect(url_for("index"))

    if guess_number < 1 or guess_number > 100:
        session["message"] = "Число должно быть в диапазоне от 1 до 100."
        session["message_type"] = "error"
        return redirect(url_for("index"))

    session["attempts"] += 1
    secret_number = session["secret_number"]

    if guess_number < secret_number:
        session["message"] = "⬆️ Слишком мало! Попробуй больше."
        session["message_type"] = "warning"

    elif guess_number > secret_number:
        session["message"] = "⬇️ Слишком много! Попробуй меньше."
        session["message_type"] = "warning"

    else:
        attempts = session["attempts"]
        best_score = session.get("best_score", DEFAULT_BEST_SCORE)

        if attempts < best_score:
            session["best_score"] = attempts
            session["message"] = f"🎉 Новый рекорд! Число {secret_number} угадано за {attempts} попыток."
        else:
            session["message"] = f"🎉 Победа! Число {secret_number} угадано за {attempts} попыток."

        session["message_type"] = "success"

        # Новая игра
        session["secret_number"] = random.randint(1, 100)
        session["attempts"] = 0

    return redirect(url_for("index"))


@app.route("/reset", methods=["POST"])
def reset():
    best_score = session.get("best_score", DEFAULT_BEST_SCORE)

    session.clear()

    session["best_score"] = best_score
    session["secret_number"] = random.randint(1, 100)
    session["attempts"] = 0
    session["message"] = "Игра сброшена. Я загадал новое число."
    session["message_type"] = "info"

    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {
        "status": "ok",
        "service": APP_NAME,
        "environment": APP_ENV
    }


@app.route("/info")
def info():
    return {
        "app": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)