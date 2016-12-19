from flask import Flask, request
import twilio.twiml
from messages import responses

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    """Sends text message"""

    message = request.values['Body'].lower()
    resp = twilio.twiml.Response()
    resp.message(responses.get(message, "boo"))

    return str(resp)

if __name__ == "__main__":

    app.run(debug=True)
