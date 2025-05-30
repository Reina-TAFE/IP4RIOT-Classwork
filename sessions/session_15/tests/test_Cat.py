import unittest
from sessions.session_15.src.Cat import Cat

class MyTestCase(unittest.TestCase):
    def test_speak(self):
        my_cat = Cat("Meowser", "Tabby")
        self.assertEqual(my_cat.speak(), "Meowser with Tabby Meows.")  # True


if __name__ == '__main__':
    unittest.main()
