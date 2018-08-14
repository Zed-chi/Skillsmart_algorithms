"""
python -m unittest tests.py
"""
import unittest
from Stack import Stack

class DynArrayTest(unittest.TestCase):
    def setUp(self):
        self.S = Stack()
        self.S.push(1)
        self.S.push(2)
        self.S.push(3)
    
    def tearDown(self):
        del self.S
    
    def test_push(self):
        beforeLength = self.S.size()
        item = 123
        self.S.push(item)
        afterLength = self.S.size()
        self.assertFalse(beforeLength == afterLength)
    
    def test_pop(self):
        self.assertEqual(1, self.S.pop())
    
    def test_peak(self):
        beforeLength = self.S.size()
        self.assertEqual(3, self.S.peak())        
        afterLength = self.S.size()
        self.assertEqual(beforeLength,afterLength)
    
if __name__ == "__main__":
    unittest.main()

