from flask import Flask
from flask import request

# We are using REST here.
# We created an object of Flask, it means all methods available inside class 'Flask' will be available for object "app".
app = Flask(__name__)

# First,The client will reach to server,
# Second, app/ Flask will provide client ,the route "/" to access the function 'hello_world'.

# "/" is our home route, it means if client reach this machine/system and port number, then the function will run.
@app.route("/")
# simple function
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"


@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test")
def test():
    a = 5 + 6
    return "this is function to run app {}".format(a)

# after test2 ,write , [ ?x=monika ] and we can see the result
@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return "this is a data input from my url {}".format(data)

# Like in multiprocessing and multithreading, inside the main function, app/flask is run and making this program into server.
if __name__=="__main__":
    app.run(host="0.0.0.0")

# here are teh APIs
# https://mango-waitress-icczg.pwskills.app:5000/test
# We are integrating WEB(HTML) and Python codes. We are accessing Python codes from HTML(Web).