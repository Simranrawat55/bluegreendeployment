from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Blue Environment</h1>
    <h2>Version 1.0<h2>
    <p>Application is running successfully in the blue environment
    what's app summi.</p>
    """

#if __name__ == "__main__":
   # app.run(host="0.0.0.0", port=5000)
