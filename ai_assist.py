from google import genai
from config import apikey

client = genai.Client(api_key=apikey)

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Hello, how can you help me today?"
)

print(response.text)
