import unittest
from src.command_mapper import map_command

class TestCommandMapper(unittest.TestCase):
    def test_known_commands(self):
        self.assertEqual(map_command("вперёд"), "w")
        self.assertEqual(map_command("назад"), "s")
        self.assertEqual(map_command("налево"), "a")
        self.assertEqual(map_command("направо"), "d")
        self.assertEqual(map_command("стоп"), "stop")

    def test_unknown_command(self):
        self.assertIsNone(map_command("прыжок"))
        self.assertIsNone(map_command(""))

if __name__ == "__main__":
    unittest.main()
