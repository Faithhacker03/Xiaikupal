from flask import Flask, render_template, request
from whitenoise import WhiteNoise # 1. Import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/") # 2. Wrap the app

@app.route("/", methods=["GET", "POST"])
def index():
    show_video = False
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == "hindi":
            show_video = True
    return render_template("index.html", show_video=show_video)

if __name__ == "__main__":
    app.run(debug=True)