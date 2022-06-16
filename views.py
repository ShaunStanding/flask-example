from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)
# view in this instance is a Blueprint

task_list = []

@views.route("/")
def home():
    return render_template("index.html")
@views.route("/about")
def about():
    return render_template("about.html")
@views.route("/contact")
def contact():
    return render_template("contact.html")
@views.route("/login")
def login():
    return render_template("login.html")
@views.route("/register")
def register():
    return render_template("register.html")
@views.route("/store")
def store():
    return render_template("store.html")


@views.route("/todos", methods=["GET","POST"])
def todos():
    if request.method == "POST":
        task = request.form.get("task-input")
        task_list.append(task)
        print(task_list)
        return render_template("todos.html", task_list=task_list)
    return render_template("todos.html")
