from flask import Flask

# create a server instance
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!!"

# run the server
app.run()
