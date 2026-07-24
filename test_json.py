import json

from llm.ollama_client import generate_response

response = generate_response("Open Chrome")

print(response)

data = json.loads(response)

print("\nParsed JSON:")
print(data)