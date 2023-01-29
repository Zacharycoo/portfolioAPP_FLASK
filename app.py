from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "Mtbc85625m!"

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/projects", methods=["POST", "GET"])
def projects():
        return render_template("projects.html")

@app.route("/projects/technical")
def technical():
    return render_template("technical.html")

@app.route("/projects/personal", methods=["POST", "GET"])
def personal():
    return render_template("personal.html")

if __name__ == '__main__':
    app.run(debug=True)