from flask import Flask
import requests
import os

#PORT = os.environ.get('PORT')
#name = os.environ.get('NAME')
#if name == None or len(name) == 0:
#  name = "world"

#if PORT == None or len(PORT) == 0:
#  PORT = 5000
PORT = 80
MESSAGE = "\nFrontend Server - Port:" + str(PORT)
print("Message: '" + MESSAGE + "'")

app = Flask(__name__)


@app.route("/")
def root():
  print("Handling web request. Returning message.")
  r = requests.get('http://127.0.0.1:5000')
  result = MESSAGE + "\nRequesting backend on port 5000.\n" + "Response: " + r.text
  result = result.encode("utf-8")
  return result


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)
