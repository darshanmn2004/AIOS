import json

from llm.ollama_client import generate_response
from agent.executor import execute

response = generate_response("Open Notepad")

print(response)

data = json.loads(response)

result = execute(
    data["action"],
    data["parameters"]
)

print(result)