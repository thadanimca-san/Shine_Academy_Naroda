import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA")
genai.configure(api_key=api_key)

print("Available Models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
