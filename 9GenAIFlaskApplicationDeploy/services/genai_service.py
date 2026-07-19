from google import genai
from google.genai import types
from config import Gemini_API_KEY

client =  genai.Client(api_key=Gemini_API_KEY)
chat = client.chats.create(
    model="gemini-3.1-flash-lite")

def get_response(prompt):

    fixed_prompt = f"""
                    Answer in valid HTML only.

                    Use:
                    <h2>, <h3>
                    <p>
                    <ul><li>
                    <pre><code>

                    Do not return markdown.

                    Question:
                    {prompt}
                    """
    response= chat.send_message(fixed_prompt)

    return response.text