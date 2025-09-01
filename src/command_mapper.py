# Соответствие голосовых команд и клавиш
COMMAND_MAP = {
    "forward": "w",
    "back": "s",
    "on left": "a",
    "on right": "d",
    "stop": "stop"
}

def map_command(text):
    """Возвращает клавишу для команды или None"""
    return COMMAND_MAP.get(text)
