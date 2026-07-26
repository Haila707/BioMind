import os

from dotenv import load_dotenv
from google import genai
import ollama

load_dotenv()


class AIProvider:

    def __init__(self, provider: str = "ollama"):

        self.provider = provider

        if provider == "gemini":
            api_key = os.getenv("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:

        if self.provider == "ollama":

            response = ollama.chat(
                model="qwen2.5:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        elif self.provider == "gemini":

            response = self.client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            return response.text

        return "[Provider not implemented]"