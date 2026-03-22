import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from utils import get_prediction

app = Flask(__name__)

frontend_origins = os.environ.get("FRONTEND_ORIGIN", "http://localhost:3000")
origin_list = [origin.strip() for origin in frontend_origins.split(",") if origin.strip()]
CORS(app, origins=origin_list)


@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Stock Prediction API Running"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


def predict_response():
    data = request.get_json(silent=True)
    if not data or "stock" not in data:
        return jsonify({"error": "Stock symbol required"}), 400
    stock = str(data.get("stock", "")).strip()
    
    try:
        result = get_prediction(stock)
        if result is None:
            return jsonify({"error": "Invalid stock symbol or insufficient market data"}), 400
        return jsonify({
            "stock": stock,
            "current_price": result["current_price"],
            "predicted_price": result["predicted_price"],
            "change_percent": result["change_percent"]
        })
    except Exception as e:
        # Debugging support
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500


@app.route("/", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict():
    return predict_response()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)