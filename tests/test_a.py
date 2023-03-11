import unittest
from a import adder 

class TestClass(unittest.TestCase):
    def testAdder(self):
        self.assertEqual(adder(1,2),3)
        self.assertEqual(adder(0,0),0)
        self.assertEqual(adder(1,-1),0)
        self.assertEqual(adder(1,-2),-1)

if __name__ == '__main__':
    unittest.main()
