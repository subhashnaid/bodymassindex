from flask import Flask, render_template, request
import os  # For fetching PORT environment variable

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi = None
    category = ""
    if request.method == "POST":
        try:
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
        except ValueError:
            category = "Invalid input. Please enter numeric values."
    
    return render_template("index.html", bmi=bmi, category=category)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000 if PORT not found
    app.run(host='0.0.0.0', port=port)
