import google.generativeai as genai

from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SUMMARY_PROMPT

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


def summarize(transcript):

    prompt = SUMMARY_PROMPT.format(text=transcript)

    response = model.generate_content(prompt)

    return response.text
