import unittest
from tmdbFunctions import get_actor_id

class TestFunctions(unittest.TestCase):

    def test_get_id(self):
        correct = 500
        test = get_actor_id("Tom Cruise")
        self.assertEqual(test, correct)
   

if __name__ == '__main__':
    unittest.main()