from ollama import chat
import time

start = time.time()

response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain Python in one sentence."
        }
    ]
)

print(response["message"]["content"])
print(f"\nTime: {time.time() - start:.2f} seconds")