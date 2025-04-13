from flask import Flask, render_template
# from waitress import serve
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('template1.html')

@app.route("/template1")
def back():
    return render_template('template1.html')

@app.route("/layout2")
def compSciPortfolio():
    return render_template('layout2.html')

@app.route("/layout3")
def compEngPortfolio():
    return render_template('layout3.html')

@app.route("/layout4")
def sculpturePortfolio():
    return render_template('layout4.html')

if __name__ == "__main__":
    # serve(app, host= "0.0.0.0", port=8000)
    app.run( host= "0.0.0.0", port=8000)
