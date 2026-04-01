import os
from rich import print
from SQL import SessionLocal, Record


# Показ полного текста конкретной записи
def show_detail(rec_id, user_id):
    session = SessionLocal()
    # Ищем запись по ID И по user_id (чтобы никто не читал чужие записи, просто подбирая ID)
    rec = session.query(Record).filter_by(id=rec_id, user_id=user_id).first()
    session.close()

    if rec:
        os.system('cls')
        print(f"\n{rec.title}")
        print(f"\nДата: {rec.created_at}")
        print("-" * 20)
        print(rec.content)
        print("-" * 20)
        input("\nНажмите Enter, чтобы закрыть запись...")
    else:
        print("[red]Ошибка ! Запись не найдена ![/]")
        input("\nНажмите Enter...")
