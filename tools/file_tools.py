from pathlib import Path


def create_folder(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
    return f"Folder created: {path}"


def create_file(path: str):
    Path(path).touch(exist_ok=True)
    return f"File created: {path}"


def write_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    return f"Content written to {path}"


def read_file(path: str):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()