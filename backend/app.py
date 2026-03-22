from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_prediction
import os

app = Flask(__name__)

# ✅ Enable CORS (important for frontend communication)
CORS(app)


@app.route("/")
def home():
    return "Stock Prediction API Running 🚀"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validate input
        if not data or "stock" not in data:
            return jsonify({"error": "Stock symbol required"}), 400

        stock = data.get("stock")

        # Call prediction function
        result = get_prediction(stock)

        if result is None:
            return jsonify({"error": "Invalid stock symbol"}), 400

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


# ✅ IMPORTANT: Cloud deployment fix (Render needs this)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)