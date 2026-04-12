"""
In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications.
You will implement functions to add, update, delete, and view user settings.
"""


def add_setting(settings, new_setting):
    settings_keys = settings.keys()
    key = new_setting[0].lower()
    value = new_setting[1].lower()
    if key in settings_keys:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
    settings.update({key: value})
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, updated_setting):
    setting_keys = settings.keys()
    key = updated_setting[0].lower()
    value = updated_setting[1].lower()
    if key not in setting_keys:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    settings.update({key: value})
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key_element):
    setting_keys = settings.keys()
    key = key_element.lower()
    if key not in setting_keys:
        return "Setting not found!"
    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."
    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += key.capitalize() + ": " + value + "\n"
    return result


test_settings = {"theme": "dark", "notifications": "enabled"}

message = add_setting(test_settings, ("VOLUME", "high"))

print(message)
print(view_settings(test_settings))
