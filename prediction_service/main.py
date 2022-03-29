import pickle
import json
from flask import Flask, jsonify, request

# Loading the model.
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    req = json.loads(request.data)
    message = req["message"]
    if isinstance(message, str) and message != "":
        predicted = model.predict([message])[0] # because it returns an array
        return jsonify({"prediction": predicted})
    return jsonify({"error": "Invalid input. Message must be a non empty string"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
