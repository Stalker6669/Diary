import os
from rich import print
from rich.console import Console
from SQL import SessionLocal, Record

console = Console()


def delete_record(rec_id, user_id):
    session = SessionLocal()
    rec = session.query(Record).filter_by(id=rec_id, user_id=user_id).first()

    if not rec:
        print(f"\n[red]Ошибка ! Запись {rec_id} не найдена.[/]")
        session.close()
        input("\nНажмите Enter, чтобы вернуться...")
        return

    os.system('cls')
    console.print(f"[red]--- Идёт удаление записи {rec_id} ---[/]", justify="center")
    # Для начало показываем запись
    print(f"\n[yellow]Заголовок:[/][white] {rec.title}[/]")
    print(f"[blue]Текст:[/][white] {rec.content[:50]}...[/]")

    confirm = console.input("\n[red]Вы уверены, что хотите удалить запись ? (y/n): [/]").strip().lower()

    if confirm == "y":
        try:
            session.delete(rec)  # Помечаем объект на удаление
            session.commit()
            print("[green]Запись успешно удалена ![/]")
        except Exception as e:
            session.rollback()
            print(f"[red]Ошибка {e}[/]")
            input("\nНажмите Enter, чтобы вернуться...")
            return
    elif confirm == "n":
        print("\nУдаление отменено")
    else:
        print(f"[red]Ошибка ! Удалить запись {rec_id} не получилось[/]")
        input("\nНажмите Enter, чтобы вернуться...")
        return
    session.close()
    input("\nНажмите Enter для выхода...")
