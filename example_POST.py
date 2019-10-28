#post example
from flask import Flask,request

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/', methods = ["GET", "POST"])
def example_me():
    #check for the methods if post
    if request.method == "POST":
        name = request.form.get("name")
        print(name)
        return format(name)
        #else for get
    else:
        return  '''<form method = "POST">
                <h1>NAME:<input type="text" name = "name"><h1>
                </form>
                '''


if __name__ == '__main__':
    app.run()
