# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import render_template

 
# Flask constructor takes the name of
# current module (__name__) as argument.
context = ('tdp-vietnam_com.pem','key.pem')
app = Flask(__name__)


##@app.before_request
##def before_request():
##    if not request.is_secure:
##        url = request.url.replace('http://', 'https://', 1)
##        code = 301
##        return redirect(url, code=code)
    
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'
@app.route("/web")
def hello(name=None):
    return render_template('index.html', name=name)
# main driver function
if __name__ == '__main__':
    
    # run() method of Flask class runs the application
    # on the local development server.
    key = r'C:\Users\tuanhd\Downloads\Flask-Application-On-IIS-main\tdp-vietnam_com.pem'
    key1 = r'C:\Users\tuanhd\Downloads\Flask-Application-On-IIS-main\key.pem'
    app.run(ssl_context=('cert.pem', 'key.pem'))

##from fastapi import FastAPI
##from a2wsgi import ASGIMiddleware
##
##app = FastAPI()
##
##@app.get("/")
##def read_main():
## return {"message": "Hello World"}
##
##wsgi_app = ASGIMiddleware(app)
