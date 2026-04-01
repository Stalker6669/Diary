import os
import sys
from rich import print
from help_user import help_user
from rich.console import Console
from add_record import add_record
from view_records import view_records
from settings_menu import settings_menu

console = Console()


def menu(user, config):
    while True:
        try:
            os.system('cls')
            console.print("--- Дневник ----", justify="center")
            print(f"[green]Привет {user.name} ![/]\n")
            print("1. Новая запись")
            print("2. Старые записи")
            print("3. Назад в главное меню")
            print("4. Выйти")
            print("5. Помощь")
            print("6. Перезапуск программы")
            print("7. Настройки\n")

            choice = input(">>> ")

            if choice == "1":
                add_record(user.id)
            elif choice == "2":
                view_records(user.id, config)
            elif choice == "3":
                from main import main
                main()
            elif choice == "4":
                os.system('cls')
                sys.exit()
            elif choice == "5":
                help_user()
            elif choice == "6":
                from main import main
                main()
            elif choice == "7":
                settings_menu(config)
            elif choice == "":
                continue
            else:
                print("[red]Ошибка ! Введено неправильное число ![/]")
                input("\nНажмите Enter, чтобы вернуться...")
                return
        except KeyboardInterrupt:
            pass
