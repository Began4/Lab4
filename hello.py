from flask import Flask
app = Flask(__name__)

@app.route("/name/<name>")
def hello(name):
	return "Your name is " + name 

if __name__ == "__main__":
	app.run()
