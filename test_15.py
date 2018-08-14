import unittest
from BinaryTree import BinaryTree, Node

class TreeTest(unittest.TestCase):

  #===============Initial==========================
    def setUp(self):
        self.b = BinaryTree(Node(12))
        self.b.add(15)
        self.b.add(18)
        self.b.add(4)
        self.b.add(9)

    def tearDown(self):
        del self.b

  #==============Testing===================
    """
    BinaryTree
        -add(value):
        -del_node(value):
        -find(value, from_node=None)
        -min_max()
        -get_node_list()
    """
    
    def test_add(self):
        val = 8
        parent = self.b.root.left_child.right_child
        self.b.add(val)
        self.assertEqual(parent.left_child.value, val)
        print(self.b.display())
    
    def test_del(self):
        x = self.b.root.right_child.right_child
        self.assertNotEqual(x, None)
        self.b.del_node(x.value)
        self.assertTrue(self.b.root.right_child.right_child == None)
    
    def test_find(self):
        res = self.b.find(15)
        parent = self.b.root
        role = "right"
        self.assertNotEqual(res["node"], None)
        self.assertEqual(parent, res["parent"])
        self.assertEqual(role, res["role"])
    
    def test_min_max(self):
        self.b.add(1)
        self.b.add(17)
        self.b.add(88)
        self.assertTrue(self.b.min_max2() == [1,88])
         
        
        
if __name__ == "__main__":
    unittest.main()
