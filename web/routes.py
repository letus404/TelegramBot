
from flask import Blueprint, render_template, request, redirect, url_for
from bot.database import get_all_messages, add_message, update_message, delete_message, set_message_status, get_message_by_id, get_all_chat_ids

main = Blueprint("main", __name__)

@main.route("/")
def index():
    messages = get_all_messages()
    return render_template("index.html", messages=messages)

@main.route("/add", methods=["POST"])
def add():
    content = request.form["content"]
    interval_min = int(request.form["interval_min"])
    interval_max = int(request.form["interval_max"])
    add_message(content, interval_min, interval_max)
    return redirect(url_for("main.index"))

@main.route("/update/<int:msg_id>", methods=["POST"])
def update(msg_id):
    content = request.form["content"]
    interval_min = int(request.form["interval_min"])
    interval_max = int(request.form["interval_max"])
    update_message(msg_id, content, interval_min, interval_max)
    return redirect(url_for("main.index"))

@main.route("/delete/<int:msg_id>")
def delete(msg_id):
    delete_message(msg_id)
    return redirect(url_for("main.index"))

@main.route("/toggle/<int:msg_id>")
def toggle(msg_id):
    enabled = int(request.args.get("enabled", 1))
    set_message_status(msg_id, enabled)
    return redirect(url_for("main.index"))

