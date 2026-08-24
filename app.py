from flask import Flask, render_template, request
app = Flask (__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    attendance = None

    if request.method == "POST":
        total_classes = request.form["total_classes"]
        attended_classes = request.form["attended_classes"]

        total_classes = int(total_classes)
        attended_classes = int(attended_classes)

        attendance = (attended_classes / total_classes) * 100

    return render_template("index.html", attendance=attendance)

if __name__ == "__main__":
    app.run(debug=True)
        