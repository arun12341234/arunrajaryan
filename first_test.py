from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, flash
app = Flask(__name__)

@app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
def hello_world():
    error = 'Invalid username/password'
    return render_template('arunrajaryan.html', error=error)
    # return render_template('portfolio.html', error=error)




if __name__ == '__main__':
    # app.debug = True
    app.run()