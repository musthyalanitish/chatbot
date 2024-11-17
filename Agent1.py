import gemini_content
import task1

def parse_function_response(message):
    try:
        function_call = message[0].get("functionCall")
        if not function_call:
            raise ValueError("No function call found in the message")

        function_name = function_call["name"]
        print(f"Bujji: Calling function: {function_name}")

        arguments = function_call.get("args", {})
        print(f"Bujji: Arguments are: {arguments}")

        if arguments:
            function = getattr(task1, function_name)
            return function(**arguments)
        else:
            return "No Arguments are present"
    except Exception as e:
        print(f"Error while executing function: {e}")
        return f"Invalid function or arguments: {e}"

def run_conversation(user_message):
    return gemini_content.generate_response(user_message)
