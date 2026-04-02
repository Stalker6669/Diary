import os
import getpass
from rich import print
from SQL import User, SessionLocal
from werkzeug.security import generate_password_hash


def add_user():
    try:
        os.system('cls')
        name_user = input("Введите имя: ")
        password_user = getpass.getpass("Введите пароль: ")

        if len(password_user) < 5:
            print("[red]Error ! Пароль маленький ! Повторите попытку ![/]")
            input("\nНажмите Enter, чтобы вернуться...")
            return

        hashed_password = generate_password_hash(password_user)

        session = SessionLocal()
        try:
            new_user = User(name=name_user, password=hashed_password)
            session.add(new_user)
            session.commit()
            print("[green]Регистрация успешна ! Теперь Войдите в систему.[/]")
            input("Для этого нажмите Enter...")
        except Exception as e:
            session.rollback()
            print(f"[red]Ошибка: {e}[/]")
            input("\nНажмите Enter, чтобы вернуться...")
            return
        finally:
            session.close()
    except KeyboardInterrupt:
        pass
