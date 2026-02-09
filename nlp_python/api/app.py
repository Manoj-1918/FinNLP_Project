from flask import Flask, jsonify, request
from nlp_python.model.finbert_interface import analyze_news

app = Flask(__name__)

@app.route("/sentiment", methods=["GET"])
def sentiment():
    # 1️⃣ Read company name from query param
    company = request.args.get("company")

    if not company:
        return jsonify({
            "error": "Company name is required. Example: /sentiment?company=TCS"
        }), 400

    try:
        # 2️⃣ Call FinBERT pipeline with company input
        result = analyze_news(company)
        return jsonify(result)

    except Exception as e:
        # 3️⃣ Safe error handling
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
