from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("index.html", section="about")

@app.route("/education")
def education():
    return render_template("index.html", section="education")

@app.route("/professional_skills")
def professional_skills():
    return render_template("index.html", section="professional_skills")

@app.route("/projects")
def projects():
    return render_template("index.html", section="projects")

@app.route("/Certifications")
def Certifications():
    return render_template("index.html", section="Certifications")

if __name__ == "__main__":
    app.run(debug=True)
