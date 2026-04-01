import os
from rich import print
from rich.console import Console
from SQL import SessionLocal, Record

console = Console()


def update_record(rec_id, user_id):
    session = SessionLocal()
    rec = session.query(Record).filter_by(id=rec_id, user_id=user_id).first()

    if not rec:
        print(f"\n[red]Ошибка ! Запись {rec_id} не найдена.[/]")
        session.close()
        input("\nНажмите Enter, чтобы вернуться...")
        return

    os.system('cls')
    console.print(f"--- Редактирование {rec_id} записи ---", justify="center")
    print(f"Старый заголовок: {rec.title}")
    new_title = console.input("[yellow]Новый заголовок (Enter чтобы оставить прежний):[/]")

    print(f"Старый текст: {rec.content}")
    new_content = input("Новый текст (Enter чтобы оставить прежний): ")

    try:
        # Обновляем только если пользователь что-то ввёл
        if new_title:
            rec.title = new_title
        if new_content:
            rec.content = new_content

        session.commit()
        print("[green]Всё успешно обновлено ![/]")
    except Exception as e:
        session.rollback()
        print(f"[red]Ошибка {e}[/]")
    finally:
        session.close()
