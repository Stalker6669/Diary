import os
import getpass
from rich import print
from SQL import User, SessionLocal
from werkzeug.security import check_password_hash


def login_user():
    try:
        os.system('cls')
        name_user = input("Введите имя: ")
        password_user = getpass.getpass("Введите пароль: ")

        session = SessionLocal()

        user = session.query(User).filter_by(name=name_user).first()
        session.close()

        if user and check_password_hash(user.password, password_user):
            print("[green]Вы успешно вошли[/]")
            return user, password_user
        else:
            print("[red]Ошибка ! Такого аккаунта нет ![/]")
            return None, None
    except KeyboardInterrupt:
        pass
