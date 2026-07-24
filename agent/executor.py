from tools.registry import TOOLS


def execute(action, parameters):

    tool = TOOLS.get(action)

    if tool is None:
        return f"Unknown action: {action}"

    try:
        return tool(**parameters)

    except TypeError as e:
        return f"Parameter error: {e}"

    except Exception as e:
        return f"Execution error: {e}"