from flask import Flask,request
import otherclass_example
app = Flask(__name__)

@app.route('/',methods = ["GET", "POST"]) 
def ctof():
    if request.method == "POST":
        otherclass_example.abMethod()
        f = request.form.get('f')
        c = (float(f) - 32) * 5/9
        return "<h1>Celsius  =" + str(c) + "</h1>"
    else:
        return '''<form method = "POST">
                <h1>Enter fahrenheit<input type = "number" step=any name = "f"></h1>
                </form>'''



if __name__ == "__main__":
    app.run(debug=True)