import unittest

class TestStr(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
    def test_split(self):
        s = 'hot dog'
        self.assertEqual(s.split(), ['hot', 'dog'])
        with self.assertRaises(TypeError):
            s.split('f')


if __name__ == '__main__':
    unittest.main()