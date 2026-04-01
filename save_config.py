import json


# Сохранение настроек
def save_config(config):
    try:
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)  # dump пишет в файл, dumps — просто в строку
    except Exception as e:
        print(f"[red]Ошибка {e}[/]")
