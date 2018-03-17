from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"homepage"
@app.route("/sudesh")

def homen():
    return" <html> <h1>Testing the flask </h1></html>"

if __name__ == "__main__":
    app.run(debug=True)
