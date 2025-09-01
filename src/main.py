from recognizer import listen_command
from command_mapper import map_command
from keyboard_controller import execute_command

print("Голосовое управление запущено. Скажите команду (вперёд/назад/налево/направо/стоп)")

while True:
    cmd_text = listen_command()
    if cmd_text:
        key = map_command(cmd_text)
        if key:
            execute_command(key)
