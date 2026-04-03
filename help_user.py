import os
from rich import print


def help_user():
    os.system('cls')
    print("[yellow]1. Перенос строки:[/]")
    print(
        "Текст будет отображаться корректно и выравниваться сам.\n[red]Не надо нажимать ENTER для переноса строки ![/]")
    print("\n[yellow]2. Команды:[/]")
    print("\t[#bf25f7]ID записи[/] - читать запись")
    print("\t[blue]update[/] - обновление записи")
    print("\t[red]delete[/] - удаление записи")
    print("\t[cyan]export[/] - экспорт записи в .txt")
    input("\nНажмите Enter для возврата...")
