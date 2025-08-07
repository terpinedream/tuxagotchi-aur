import os
import toml


def load_config():
    user_config_path = os.path.expanduser("~/.config/tuxagotchi/config.toml")

    default_config_path = os.path.join(os.path.dirname(__file__), "config.toml")

    config_path = (
        user_config_path if os.path.exists(user_config_path) else default_config_path
    )

    config = toml.load(config_path)

    # Provide fallback defaults for colors
    colors = config.get("colors", {})
    config["colors"] = {
        "accent": colors.get("accent", "red"),
        "background": colors.get("background", "transparent"),
        "foreground": colors.get("foreground", "red"),
        "highlight": colors.get("highlight", "red"),
        "todo_border": colors.get("todo_border", "red"),
    }
    return config
