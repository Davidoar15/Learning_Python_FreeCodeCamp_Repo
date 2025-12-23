def add_setting(settings: dict, setting: tuple):
    key, value = setting
    lower_key = key.lower()
    lower_value = value.lower()

    if lower_key in settings:
        return f"Setting '{lower_key}' already exists! Cannot add a new setting with this name."
    
    settings[lower_key] = lower_value
    return f"Setting '{lower_key}' added with value '{lower_value}' successfully!"

def update_setting(settings: dict, setting: tuple):
    key, value = setting
    lower_key = key.lower()
    lower_value = value.lower()

    if lower_key in settings:
        settings[lower_key] = lower_value
        return f"Setting '{lower_key}' updated to '{lower_value}' successfully!"

    return f"Setting '{lower_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key: str):
    lower_key = key.lower()

    if lower_key in settings:
        del settings[lower_key]
        return f"Setting '{lower_key}' deleted successfully!"

    return "Setting not found!"

def view_settings(settings: dict):
    if not settings:
        return "No settings available."

    setting_lines = [print_setting(setting) for setting in settings.items()]
    return "Current User Settings:\n" + "\n".join(setting_lines) + "\n"

def print_setting(setting: tuple):
    key, value = setting
    return f"{key.capitalize()}: {value}"

test_settings = {}

add_setting(test_settings, ('theme', 'dark'))
add_setting(test_settings, ('NoTifications', 'disableD'))
add_setting(test_settings, ('vOlume', 'low'))

print(view_settings(test_settings))

# print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
