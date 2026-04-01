import os
import json
from save_config import save_config


# Чтение настроек
def load_config():
    default_config = {"view_mode": 1, "saved_user_name": None}
    if not os.path.exists("config.json"):
        save_config(default_config)
        return default_config
    with open("config.json", "r") as f:
        return json.load(f)
