from flask import Flask

crt = r'C:\Users\tuanhd\Downloads\Flask-Application-On-IIS-main\tdp-vietnam_com.pem'
key = r'C:\Users\tuanhd\Downloads\Flask-Application-On-IIS-main\key.pem'
# create a server instance
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!!"

# run the server
app.run()
