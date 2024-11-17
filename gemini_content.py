from config import key
import requests
from mic_to_task1 import mic1

def generate_response(input_text):
    messages = [{"role": "user", "parts": [{"text": input_text}]}]
    data = {"contents": messages}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={key}"

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        t1 = response.json()

        # Check if the response contains the expected data
        t2 = (
            t1.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "No response")
        )
        return t2
    except requests.exceptions.RequestException as e:
        print(f"Error fetching response from Gemini API: {e}")
        return f"Error: {e}"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {e}"

def generate_response_from_voice():
    try:
        user_voice_input = mic1()
        if user_voice_input:
            return generate_response(user_voice_input)
        else:
            return "Could not process voice input."
    except Exception as e:
        print(f"Error in voice response generation: {e}")
        return f"Error: {e}"
