from flask import Flask, request, jsonify
from nlp_python.model.finbert_interface import analyze_company

app = Flask(__name__)


# -------------------------------
# Health Check (important)
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "FinNLP Python Service Running"})


# -------------------------------
# Sentiment Endpoint
# -------------------------------
@app.route("/sentiment", methods=["GET"])
def sentiment():

    # Get parameters from request
    company = request.args.get("company")
    symbol = request.args.get("symbol")
    sector = request.args.get("sector")

    # Validation
    if not company or not symbol or not sector:
        return jsonify({
            "error": "Missing parameters",
            "required": "company, symbol, sector"
        }), 400

    try:
        result = analyze_company(company, symbol, sector)
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": "Processing failed",
            "details": str(e)
        }), 500


# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)