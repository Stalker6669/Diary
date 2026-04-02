import os
from rich import print
from rich.console import Console
from save_config import save_config

console = Console()


def settings_menu(config):
    while True:
        os.system('cls')
        console.print("[red]--- Настройки ---[/]", justify="center")
        print(f"1. Стиль команд: [{'старый' if config['view_mode'] == 1 else 'новый'}]")
        print("2. Сбросить сохранённого пользователя")
        print("3. Отмана")

        try:
            choice = input("\n>>> ")
            if choice == "1":
                config["view_mode"] = 2 if config["view_mode"] == 1 else 1
                save_config(config)
                print("[green]Настройка изменена![/]")
            elif choice == "2":
                config["saved_user_name"] = None
                save_config(config)
                print("[green]Пользователь сброшен. При следующем входе нужно будет авторизоваться.[/]")
            elif choice == "3":
                from main import main
                main()
            else:
                print("[red]Ошибка ! Повторите попытку[/]")
                input("\nНажмите Enter, чтобы вернуться...")
                return
        except KeyboardInterrupt:
            pass
