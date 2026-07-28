import os

from dotenv import load_dotenv
from google import genai
import ollama


load_dotenv()


class AIProvider:

    def __init__(self, provider: str = None):

        # يقرأ من البيئة، وإذا لم يوجد يستخدم ollama محليًا
        self.provider = provider or os.getenv(
            "AI_PROVIDER",
            "ollama"
        )


        if self.provider == "gemini":

            api_key = os.getenv("GOOGLE_API_KEY")

            if not api_key:
                raise Exception(
                    "GOOGLE_API_KEY is missing"
                )

            self.client = genai.Client(
                api_key=api_key
            )


        elif self.provider == "ollama":

            self.client = ollama.Client(
                host=os.getenv(
                    "OLLAMA_HOST",
                    "http://127.0.0.1:11434"
                )
            )


    def generate(self, prompt: str) -> str:


        if self.provider == "ollama":

            try:

                print("=" * 70)
                print("Using Ollama local model")
                print("=" * 70)


                response = self.client.chat(
                    model=os.getenv(
                        "OLLAMA_MODEL",
                        "qwen2.5:3b"
                    ),

                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )


                return response["message"]["content"]


            except Exception as e:

                return (
                    "[OLLAMA ERROR] "
                    f"{str(e)}"
                )



        elif self.provider == "gemini":

            try:

                print("=" * 70)
                print("Using Gemini API")
                print("=" * 70)


                response = self.client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )


                return response.text


            except Exception as e:

                return (
                    "[GEMINI ERROR] "
                    f"{str(e)}"
                )


        return "[Provider not implemented]"