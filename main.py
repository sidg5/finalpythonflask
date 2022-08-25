from flask import Flask
import os
app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def hello():
    return "I have dockerized my flask application and deployed it on heroku"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=port)