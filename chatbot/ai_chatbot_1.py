
from google import genai

api_key = "AIzaSyBC038g5sDMrkznWWAbcfn0sbI0euanHJ4"


my_ai = genai.Client(api_key = api_key)

responce = my_ai.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "why python is important to learn in 2026."
)

print(responce.text)