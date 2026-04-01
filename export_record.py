import os
from rich import print
from rich.console import Console
from SQL import SessionLocal, Record

console = Console()


def export_record(rec_id, user_id):
    session = SessionLocal()
    rec = session.query(Record).filter_by(id=rec_id, user_id=user_id).first()
    session.close()  # Так как данные уже в памяти, можно закрыть сессию

    if not rec:
        print(f"\n[red]Ошибка ! Запись {rec_id} не найдена.[/]")
        session.close()
        input("\nНажмите Enter, чтобы вернуться...")
        return

    os.system('cls')
    console.print(f"[red]--- Идёт экспорт записи {rec_id} ---[/]", justify="center")
    # Для начало показываем запись
    print(f"\n[yellow]Заголовок:[/][white] {rec.title}[/]")
    print(f"[blue]Текст:[/][white] {rec.content[:50]}...[/]")
    print(
        '\nВведите путь для сохранения файла (Пример: C:/Users/Admin)'
        ' или оставьте пустым для сохранения в папку с программой.')
    print("[red]Внимание ! Если указанного пути не будет, то вас вернёт обратно в меню ![/]")

    try:
        path = input("\n>>> ").strip()

        # Формируем имя файла (заменяем пробелы в заголовке, чтобы не было ошибок)
        # Спасибо gemini за это кусок кода, я бы сам его не написал
        safe_title = "".join([c for c in rec.title if c.isalnum() or c in (' ', '_')]).rstrip()
        file_name = f"record_{rec_id}_{safe_title}.txt"

        # Если пользователь ввёл путь, объединяем его с именем файла
        if path:
            if not os.path.exists(path):
                print(f"[red]Ошибка! Путь: '{path}' не существует.[/]")
                input("\nНажмите Enter...")
                return
            full_path = os.path.join(path, file_name)
        else:
            full_path = file_name

        # Проверка на то, что файл уже с таким именем существует
        if os.path.exists(full_path):
            print(f"[red]Внимание ! Файл '{file_name}' уже существует ![/]")
            print("1. Перезаписать")
            print("2. Сохранить с другим именем")
            print("3. Отмена")

            ov_choice = input(">>> ")

            if ov_choice == "2":
                new_name = input("Введите новое имя файла (без .txt): ").strip()
                if not new_name:
                    print("[red]Ошибка ! Имя не может быть пустым ![/]")
                    return

                # Формируем новое имя файла
                file_name = f"{new_name}.txt"
                # Пересобираем путь с новым именем
                if path:
                    full_path = os.path.join(path, file_name)
                else:
                    full_path = file_name
            elif ov_choice == "3":
                input("\nНажмите Enter для выхода...")
                return
            # Если выбрали "1", программа просто пойдёт дальше и перезапишет файл
        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(f"Заголовок: {rec.title}\n")
                f.write(f"Дата: {rec.created_at.strftime('%d.%m.%Y %H:%M')}\n")
                f.write("-" * 20 + "\n")
                f.write(rec.content)
            print(f"\n[green]Успешно! Файл сохранен как: {full_path}[/]")
        except Exception as e:
            print(f"[red]Ошибка при записи файла: {e}[/]")
    except KeyboardInterrupt:
        pass

    input("\nНажмите Enter для выхода...")
