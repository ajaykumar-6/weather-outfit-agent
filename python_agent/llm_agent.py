import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def llm_clothing_recommendation(weather, user_preferences):
    prompt = f"""
    You are a smart fashion assistant.

    Weather:
    Temperature: {weather['temperature']}°C
    Condition: {weather['condition']}
    Humidity: {weather['humidity']}%

    User preferences:
    Style: {user_preferences.get('style')}
    Avoid: {user_preferences.get('avoid')}

    Recommend suitable clothing in a friendly way.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]
