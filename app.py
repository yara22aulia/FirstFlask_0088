
from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    hasil = ""

    if request.method == "POST":
        nama = request.form.get("nama", "").strip()

        if nama:
            hasil = "Hello, " + nama + "!"
        else:
            hasil = "Nama tidak boleh kosong!"

    return render_template("index.html", hasil=hasil)


@app.route("/about")
def about():
    return "About us"


@app.route("/user/<name>")
def profile(name):
    return f"Hello, {escape(name)}!"


@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id
    }"


if __name__ == "__main__":
    app.run(debug=True)
