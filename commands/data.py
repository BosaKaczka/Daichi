import json


def load(file: str):
    try:
        with open(file, 'r') as f:
            file_content = f.read()
            if file_content:
                return json.loads(file_content)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print("File not found. Using default settings.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return


def add_settings(file_path, add):
    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = {}
    existing_data.update(add)
    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=2)
    return


def remove_settings(file_path, remove):
    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        return

    for key in remove:
        existing_data.pop(key, None)

    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=2)
    return


def check_set(file_path, target_key):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            if target_key in data:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return False


def get_settings(file_path, target_key):
    with open(file_path, 'r') as file:
        settings_data = json.load(file)
    if target_key in settings_data:
        return settings_data[target_key]
    else:
        return None
