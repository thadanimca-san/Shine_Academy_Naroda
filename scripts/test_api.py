import os
from google import genai
from google.genai import types

def test_api():
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents='Hello, testing 1 2 3.'
        )
        print("Success:", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    test_api()
