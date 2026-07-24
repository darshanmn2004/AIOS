from ollama import chat
from agent.system_prompt import SYSTEM_PROMPT

MODEL = "qwen2.5:3b"


def generate_response(prompt: str):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0,
            "num_predict": 250
        }
    )

    return response["message"]["content"]