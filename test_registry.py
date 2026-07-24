import json

from llm.ollama_client import generate_response
from agent.executor import execute

prompt = "Create hello.py and write a Hello World program into it"
response = generate_response(prompt)

print(response)

data = json.loads(response)

print("\nExecuting Plan...\n")

for step in data["plan"]:

    result = execute(
        step["action"],
        step["parameters"]
    )

    print(result)

print("\nDone.")