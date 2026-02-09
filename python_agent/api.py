from flask import Flask, request, jsonify
import os

from weather_api import get_weather
from agent_logic import recommend_clothes
from memory import get_user_preferences

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        city = data.get("city") if data else None

        if not city:
            return jsonify({
                "error": "City is required"
            }), 400

        # Get weather data
        weather = get_weather(city)

        # Get user preferences
        preferences = get_user_preferences()

        # Get outfit recommendation
        outfit = recommend_clothes(weather, preferences)

        return jsonify({
            "weather": weather,
            "recommendations": outfit
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    # IMPORTANT: Required for Render deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
