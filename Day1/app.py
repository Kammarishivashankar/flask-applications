from flask import Flask

app = Flask(__name__)


@app.route('/')
def Welcome():
    return f"<h1>Hi Welcome the Home page!</h1>"

@app.route('/Home/<name>')
def Welcome_page(name):
    return f"<h1>Hi {name} Welcome the Home page!</h1>"

@app.route('/Addition/<int:num1>/<int:num2>')
def Addition(num1,num2):
    return f"<h1>Addition of {num1} and {num2} is {num1 + num2}</h1>"



if __name__ == "__main__":
    app.run(debug=True)