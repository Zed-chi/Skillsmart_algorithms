"""
python -m unittest tests.py
"""

import unittest, ctypes
from DynamicArray import DynArray

class DynArrayTest(unittest.TestCase):
    def setUp(self):
        self.D = DynArray()
        for i in range(0,16):
            self.D.append(i)
    
    def tearDown(self):
        del self.D
    
    def test_insert(self):
        item = 1234
        pos = 3
        lengthBefore = len(self.D)
        self.D.insert(pos, item)
        lengthAfter = len(self.D)
        
        self.assertEqual(self.D[pos], item)
        self.assertTrue(lengthBefore < lengthAfter)
        self.assertRaises(IndexError, self.D.insert,-1,item)
        self.assertRaises(IndexError, self.D.insert,lengthAfter,item)
        
    def test_delete_item(self):
        beforeLength = len(self.D)
        pos = 7
        beforeItem = self.D[pos]
        self.D.delete(pos)
        afterLength = len(self.D)
        afterItem = self.D[pos]
        self.assertTrue(beforeLength>afterLength)
        self.assertNotEqual(beforeItem, afterItem)
        
    
if __name__ == "__main__":
    unittest.main()
