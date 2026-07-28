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

        if provider == "ollama":
            self.client = ollama.Client(host="http://127.0.0.1:11434")

    def generate(self, prompt: str) -> str:

        if self.provider == "ollama":

            try:

                print("=" * 70)
                print("Connecting to Ollama...")
                print("=" * 70)

                response = self.client.chat(
                    model="qwen2.5:3b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                print("=" * 70)
                print("Ollama replied successfully.")
                print("=" * 70)

                return response["message"]["content"]

            except Exception as e:

                print("=" * 70)
                print("OLLAMA ERROR")
                print(type(e).__name__)
                print(str(e))
                print("=" * 70)

                return f"[OLLAMA ERROR] {e}"

        elif self.provider == "gemini":

            response = self.client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            return response.text

        return "[Provider not implemented]"