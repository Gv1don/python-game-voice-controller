import keyboard

pressed_keys = set()

def execute_command(key):
    """Нажимает клавишу, или отпускает все если 'stop'"""
    global pressed_keys
    if key == "stop":
        for k in pressed_keys:
            keyboard.release(k)
        pressed_keys.clear()
    else:
        # Отпускаем предыдущие, если хотим однонаправленное движение
        for k in pressed_keys:
            keyboard.release(k)
        pressed_keys.clear()
        keyboard.press(key)
        pressed_keys.add(key)
