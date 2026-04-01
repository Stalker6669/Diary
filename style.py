from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles import Style

# Определяем стили. Имена ключей — это "классы".
style = Style.from_dict({
    'diary-delete': '#ff0000',  # Красный
    'diary-update': 'ansiblue',  # Голубой
    'diary-export': '#00ffff',  # Жёлтый
})


class DiaryLexer(Lexer):
    def lex_document(self, document):
        def get_line(lineno):
            line = document.lines[lineno]
            result = []

            # Красим первое слово, если это команда
            words = line.split(' ', 1)
            command = words[0]

            # Здесь мы сопоставляем команду с классом из словаря выше
            if command == 'delete':
                result.append(('class:diary-delete', command))
            elif command == 'update':
                result.append(('class:diary-update', command))
            elif command == 'export':
                result.append(('class:diary-export', command))
            else:
                result.append(('', command))

            if len(words) > 1:
                result.append(('', ' ' + words[1]))

            return result

        return get_line
