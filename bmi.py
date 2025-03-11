from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi = None
    category = ""
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = weight / (height * height)
        if bmi < 18.5:
            category = "YOU ARE IN UNDERWEIGHT."
        elif 18.5 <= bmi < 24.9:
            category = "YOU ARE IN NORMAL WEIGHT."
        elif 25 <= bmi < 30:
            category = "YOU ARE IN OVERWEIGHT."
        else:
            category = "YOU ARE UNDER OBESITY. CONSULT A DOCTOR."
    return render_template("index.html", bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
