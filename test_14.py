import unittest
from Tree import Tree, Node

class TreeTest(unittest.TestCase):

  #===============Initial==========================
    def setUp(self):
        self.t = Tree(Node("root"))
        self.t.add(Node("A"))
        self.t.add(Node("B"))
        self.t.add(Node("Aa"), self.t.root.children[0])
        self.t.add(Node("Ab"), self.t.root.children[0])
        self.t.add(Node("Ba"), self.t.root.children[1])

    def tearDown(self):
        del self.t

  #==============Testing===================
    def test_add_to_root(self):
        before = len(self.t.root.children)
        self.t.add(Node("value"))
        after = len(self.t.root.children)
        self.assertTrue(before+1 == after)
        
    def test_add_to_node(self):
        node = self.t.root.children[0]
        before = len(node.children)
        self.t.add(Node("subvalue"), node)
        after = len(node.children)
        self.assertTrue(before+1 == after)
    
    def test_del_from_node(self):
        before = len(self.t.root.children)
        self.t.del_node(self.t.root.children[0])
        after = len(self.t.root.children)
        self.assertTrue(before == after+1)
    
    def test_get_nodes(self):
        self.assertEqual(len(self.t.get_node_list()), 6)
    
    def test_find(self):
        self.assertEqual(self.t.find("Ab").value, "Ab")
    
    def test_find_by_value(self):
        self.assertEqual(len(self.t.find_nodes("A")), 1)
        self.t.add(Node("A"))
        self.assertEqual(len(self.t.find_nodes("A")), 2)
    
    def test_move(self):
        b = len(self.t.root.children[1].children)
        a = len(self.t.root.children[0].children)
        node_to_move = self.t.root.children[0].children[0]
        new_parent = self.t.root.children[1]
        self.t.move_to(node_to_move, new_parent)
        self.assertEqual(b+1, len(self.t.root.children[1].children))
        self.assertEqual(a-1, len(self.t.root.children[0].children))
    
    def test_nodes_and_leafs(self):
        d = self.t.get_nodes_and_leafs()
        self.assertEqual(len(d["nodes"]), 3)
        self.assertEqual(len(d["leafs"]), 3)
        
    def test_marks(self):
        self.assertEqual(self.t.find("A").level, None)
        self.assertEqual(self.t.find("Ab").level, None)
        self.t.mark_nodes()
        self.assertEqual(self.t.find("A").level, 1)
        self.assertEqual(self.t.find("Ab").level, 2)
        
        
if __name__ == "__main__":
    unittest.main()