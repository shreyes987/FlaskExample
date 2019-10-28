from flask import Flask,request
import math
app =  Flask(__name__)


@app.route('/' , methods = ["GET","POST"])
def pythagoras():
    if request.method == "POST":
        side1 = request.form.get('side1')
        side2 = request.form.get('side2')
        # formula : a2 + b2  = c2
        sidea = float(side1)
        sidea2 = sidea * sidea
        sideb = float(side2)
        sideb2 = sideb * sideb
        ans = sidea2 + sideb2
        root = math.sqrt(ans)
        answer = str(root)
        return "<h1>Answer = "+answer+" </h1>"
    else:
        return '''<form method = "POST">
                <h1> Pythagoras theorm </h1>
                <h1>Side 1<input type = "number" name = "side1"><h1>
                <h1>Side 2<input type = "number" name = "side2"><h1>
                <input type = "submit">
                    </form>'''


if __name__ == "__main__":
    app.run(debug=True)