from flask import Flask, render_template, redirect, request

app = Flask(__name__)

saved_data = {}

@app.route("/")
def main_page():
    text = None
    if "note" in saved_data:
        text = saved_data["note"]
    edits = saved_data.get("edit_count", 0)
    return render_template("index.html", note=text, edit_count=edits)


@app.route("/note", methods=["GET","POST"])
def note_form():
    if request.method == "POST":
        saved_data["note"] = request.form["note"]
        saved_data["edit_count"] = saved_data.get("edit_count", 0) + 1
        return redirect("/")
    return render_template("note.html")


if __name__ == "__main__":
    app.run(
        debug = True, 
        port = 7777
    )