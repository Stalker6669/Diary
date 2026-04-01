import getpass
import os
import sys
from menu import menu
from rich import print
from add_user import add_user
from rich.console import Console
from login_user import login_user
from save_config import save_config
from load_config import load_config
from settings_menu import settings_menu
from SQL import start_db, User, SessionLocal
from security import encrypt_name, decrypt_name

start_db()
console = Console()


def main():
    # Авто вход
    os.system('cls')
    config = load_config()

    if config.get("saved_user_name"):
        print("[red]Обнаружен сохраненный профиль.[/]")
        entry = input("Войти под этим профилем ? (y/n): ").lower()

        if entry == "y":
            master_pass = getpass.getpass("Введите пароль: ")

            real_name = decrypt_name(config["saved_user_name"], master_pass)

            if real_name:
                session = SessionLocal()
                user = session.query(User).filter_by(name=real_name).first()
                session.close()
                if user:
                    menu(user, config)
                    return  # Завершаем main после выхода из меню
            else:
                print("[red]Ошибка ! Неверный пароль ![/]")
                input("\nНажмите Enter, чтобы вернуться...")
                return
        elif entry == "n":
            # Основной вход
            while True:
                try:
                    os.system('cls')
                    console.print("--- Консольный дневник ---", justify="center")
                    print("1. Войти")
                    print("2. Зарегистрироваться")
                    print("3. Выйти")
                    print("4. Настройки")
                    question = input("\n>>> ")

                    if question == "1":
                        user, raw_password = login_user()
                        if user:
                            # После успешного входа спрашиваем: сохранить?
                            save_me = input("Запомнить вас на этом устройстве ? (y/n): ").lower()
                            if save_me == "y":
                                config["saved_user_name"] = encrypt_name(user.name, raw_password)
                                save_config(config)
                            menu(user, config)
                    elif question == "2":
                        add_user()
                    elif question == "3":
                        os.system('cls')
                        sys.exit()
                    elif question == "4":
                        settings_menu(config)
                    else:
                        print("[red]Ошибка ! Повторите попытку ![/]")
                        input("\nНажмите Enter, чтобы вернуться...")
                        return
                except KeyboardInterrupt:
                    pass
        else:
            print("\n[red]Ошибка ! Повторите попытку ![/]")
            input("Нажмите Enter, чтобы вернуться...")
            main()


if __name__ == '__main__':
    main()
