from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("home.html")

notes = []
@app.route('/taking_notes', methods=["POST"])
def notes_fun():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)