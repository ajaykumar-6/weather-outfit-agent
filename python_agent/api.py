from flask import Flask, request, jsonify
from weather_api import get_weather
from agent_logic import recommend_clothes
from memory import get_user_preferences

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        city = data.get("city")

        if not city:
            return jsonify({"error": "City is required"}), 400

        weather = get_weather(city)
        preferences = get_user_preferences()
        clothes = recommend_clothes(weather, preferences)

        return jsonify({
            "weather": weather,
            "recommendations": clothes
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
