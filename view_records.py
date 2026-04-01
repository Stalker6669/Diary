from rich import print
from rich.console import Console
from prompt_toolkit import prompt
from show_detail import show_detail
from style import DiaryLexer, style
from SQL import SessionLocal, Record
from update_record import update_record
from delete_record import delete_record
from export_record import export_record

console = Console()


def view_records(user_id, config):
    session = SessionLocal()
    # Получаем все записи этого пользователя, свежие будут сверху
    records = session.query(Record).filter_by(user_id=user_id).order_by(Record.created_at.desc()).all()
    session.close()

    try:
        if not records:
            print("[red]У вас нет записей ![/]")
            input("\nНажмите Enter, чтобы вернуться...")
        else:
            console.print("--- Ваши записи ----", justify="center")
            for r in records:
                # Выводим ID, Дату и Заголовок
                date_str = r.created_at.strftime('%d.%m.%Y %H:%M')
                print(f"[{r.id}] {date_str} {r.title}")

        if config["view_mode"] == 1:
            print("\nВведите ID записи, чтобы прочитать её целиком.\n[red]Нажмите Enter для выхода.[/]\nВведите "
                  "[red]update[/] и ID"
                  "записи [purple]для изменений[/].(Пример: update 1)\nВведите [red]delete[/] и ID "
                  "записи [purple]для удаления[/].(Пример: delete 1)\nВведите [red]export[/] и ID "
                  "записи [purple]для экспорта[/] в .txt файл. (Пример: export 1)  ")
        else:
            console.rule("[#f7d125]Доступные команды")
            console.print(
                "[#bf25f7]ID[/] - читать | [blue]update[/] - изменить | [red]delete[/] - удалить | [cyan]export[/] - экспорт",
                justify="center")

            detail_id = prompt(">>> ", lexer=DiaryLexer(), style=style).strip().lower()
            if detail_id.isdigit():
                show_detail(int(detail_id), user_id)
            elif detail_id.startswith("update "):
                try:
                    # Берем всё, что после слова "update
                    rec_id = int(detail_id.split()[1])
                    update_record(rec_id, user_id)
                except (ValueError, IndexError):
                    print("[red]Ошибка ! Введите ID после слова update (например: update 1)[/]")
                    input("\nНажмите Enter, чтобы вернуться...")
            elif detail_id.startswith("delete "):
                try:
                    rec_id = int(detail_id.split()[1])
                    delete_record(rec_id, user_id)
                except (ValueError, IndexError):
                    print("[red]Ошибка ! Введите ID после слова delete (например: delete 1)[/]")
                    input("\nНажмите Enter, чтобы вернуться...")
            elif detail_id.startswith("export "):
                try:
                    rec_id = int(detail_id.split()[1])
                    export_record(rec_id, user_id)
                except (ValueError, IndexError):
                    print("[red]Ошибка ! Введите ID после слова export (например: export 1)[/]")
                    input("\nНажмите Enter, чтобы вернуться...")
            else:
                return  # При нажатии Enter
    except KeyboardInterrupt:
        pass
