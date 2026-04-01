import os
from rich.console import Console
from rich import print
from SQL import SessionLocal, Record

console = Console()


def add_record(user_id):
    try:
        os.system('cls')
        console.print("--- Новая запись ---", justify="center")

        title = input("\nЗаголовок: ")
        content = input("Текст записи:\n")

        session = SessionLocal()

        try:
            new_rec = Record(title=title, content=content, user_id=user_id)
            session.add(new_rec)
            session.commit()
            print("[green]\nЗапись успешно добавлена ![/]")
        except Exception as e:
            print(f"[red]Ошибка: {e}[/]")
        finally:
            session.close()
    except KeyboardInterrupt:
        pass
