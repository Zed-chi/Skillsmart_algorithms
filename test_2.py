"""
python -m unittest tests.py
"""
import unittest
from DoubleLinkedList import LinkedList2, Node2, fill

class TestList(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList2()
        fill([1,2,3,4,3], self.l)
    
    def tearDown(self):
        self.l = None
        
    ### tests
    def testRemoveOne(self):
        self.l.rem(1)
        self.assertEqual( str([2,3,4,3]), str(self.l) )
        self.l.rem(3)
        self.l.rem(3)
        self.l.rem(9)
        self.assertEqual( str([2,4]), str(self.l) )
    
    def testRemoveAll(self):
        self.l.rem_all(3)
        self.assertEqual( str([1,2,4]), str(self.l) )
        self.l.rem_all(5)
        self.assertEqual( str([1,2,4]), str(self.l) )
        
    def testClear(self):
        self.l.clear()
        self.assertTrue(self.l.head == None and self.l.tail == None)
        
    def testFindOne(self):
        self.assertEqual( Node2(2).value, self.l.find(2).value )
        self.assertEqual( None, self.l.find(123) )
        
    def testLength(self):
        self.assertEqual( len(self.l), 5)
        
    def testInsert(self):
        self.l.insert(self.l.find(4),Node2(5))
        self.assertEqual(str([1,2,3,4,5,3]), str(self.l))
        self.l.insert(self.l.find(6),Node2(5))
        self.assertEqual(str([1,2,3,4,5,3]), str(self.l))
        self.l.insert(self.l.find(5),Node2(4))
        self.assertEqual(str([1,2,3,4,5,4,3]), str(self.l))
    
    def testInsertHead(self):
        self.l.insHead(Node2(999))
        self.assertEqual(str([999,1,2,3,4,3]), str(self.l))
    

if __name__ == '__main__':
    unittest.main()    
