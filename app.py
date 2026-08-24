from flask import Flask, render_template, request
app = Flask (__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    attendance = None
    required = None
    classes_can_miss = None
    classes_needed = None
    error = None

    if request.method == "POST":

        total_classes = int(request.form["total_classes"])
        attended_classes = int(request.form["attended_classes"])
        required = int(request.form["required"])

        # Input validation
        if total_classes <= 0:
            error = "Total classes must be greater than 0."

        elif attended_classes < 0:
            error = "Attended classes cannot be negative."

        elif attended_classes > total_classes:
            error = "Attended classes cannot be greater than total classes."

        else:

            attendance = round(
                (attended_classes / total_classes) * 100,
                2
            )

            if attendance >= required:

                classes_can_miss = 0

                while (
                    (attended_classes /
                     (total_classes + classes_can_miss + 1)) * 100
                    >= required
                ):
                    classes_can_miss += 1

            else:

                classes_needed = 0

                while (
                    (attended_classes + classes_needed) /
                    (total_classes + classes_needed) * 100
                    < required
                ):
                    classes_needed += 1

    return render_template(
        "index.html",
        attendance=attendance,
        required=required,
        classes_can_miss=classes_can_miss,
        classes_needed=classes_needed,
        error=error
    )
if __name__ == "__main__":
    app.run(debug=True)
        