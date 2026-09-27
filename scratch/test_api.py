import os
import sys

has_key = "GEMINI_API_KEY" in os.environ
print("Has GEMINI_API_KEY:", has_key)
if has_key:
    try:
        from google import genai
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents='Translate "Hello" to Gujarati.'
        )
        print("Response:", response.text)
    except Exception as e:
        print("GenAI Error:", e)
