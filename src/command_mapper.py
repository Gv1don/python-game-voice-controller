# Соответствие голосовых команд и клавиш
COMMAND_MAP = {
    "вперёд": "w",
    "назад": "s",
    "налево": "a",
    "направо": "d",
    "стоп": "stop"
}

def map_command(text):
    """Возвращает клавишу для команды или None"""
    return COMMAND_MAP.get(text)
