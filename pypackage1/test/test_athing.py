import unittest
from pypackage1.main.doathing import makeMagicString

class MyTest(unittest.TestCase):

    def test_string(self):
        assert makeMagicString() == "banana", "should be banana"
        assert 1 == 1, "this is running"

suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
unittest.TextTestRunner(verbosity=2).run(suite)