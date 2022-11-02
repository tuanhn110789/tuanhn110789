
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for


app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
