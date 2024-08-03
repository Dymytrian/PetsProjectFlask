from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route("/")
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/dog')
def dogfunk():
    return render_template("dog.html")

@app.route('/cat')
def catfunk():
    return render_template("cat.html")

@app.route("/dog", methods=['POST'])
def index_postdog():
    dani1 = request.form.get('numberdog')
    try:
        v1 = float(dani1)
        if v1 > 0:
            vik1 = round(16 * math.log(v1) + 31)
        return render_template('resultat1.html', result1=vik1)
    except ValueError:
        return "Введіть будь ласка коректні дані"

@app.route("/cat", methods=['POST'])
def index_postcat():
    dani2 = request.form.get('numbercat')
    try:
        v2 = float(dani2)
        if ((v2 >0) and (v2<1)):
            vik2 = v2 * 10
        elif v2 == 1:
            vik2 = 15
        elif (v2 > 1) and (v2 < 2):
            vik2 = v2 * 12.5
        elif v2 == 2:
            vik2 = 24
        elif v2 > 2:
            vik2 = 24 + (v2 - 2) * 4
        return render_template('resultat2.html', result2=vik2)
    except ValueError:
        return "Введіть будь ласка коректні дані"

if __name__ == "__main__":
    app.run()
