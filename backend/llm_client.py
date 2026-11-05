# import os
# from google import genai


# class LLMClient:
#     """
#     ORCA LLM Client.

#     Provides a simple interface between ORCA
#     and the Gemini language model.
#     """

#     def __init__(self):
#         api_key = os.getenv("GEMINI_API_KEY")

#         if not api_key:
#             raise ValueError(
#                 "GEMINI_API_KEY environment variable is not set."
#             )

#         self.client = genai.Client(api_key=api_key)
#         self.model = "gemini-3.6-flash"

#     def generate(self, prompt):
#         """
#         Send a prompt to the LLM and return its response.
#         """

#         response = self.client.models.generate_content(
#             model=self.model,
#             contents=prompt
#         )

#         return response.text

import os
from dotenv import load_dotenv

load_dotenv()

from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

client = Groq(api_key=api_key)

class LLMClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY environment variable is not set."
            )

        self.client = Groq(api_key=api_key)
        self.model = "openai/gpt-oss-20b"

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content