import unittest
from src import keyboard_controller as kc

class TestKeyboardController(unittest.TestCase):
    def test_execute_command_stop(self):
        kc.pressed_keys = {"w", "a"}
        kc.execute_command("stop")
        self.assertEqual(len(kc.pressed_keys), 0)

    def test_execute_command_press(self):
        kc.pressed_keys = set()
        kc.execute_command("s")
        self.assertIn("s", kc.pressed_keys)
        # С предыдущих нажатий больше не должно быть
        kc.execute_command("d")
        self.assertEqual(kc.pressed_keys, {"d"})

if __name__ == "__main__":
    unittest.main()
