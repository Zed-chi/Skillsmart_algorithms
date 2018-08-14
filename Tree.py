"""
Tree impl
-add(child, node=None):
-del_node(node):
-get_node_list(from_node=None)
-find(value, from_node=None)
-find_nodes(value, from_node=None)
-move_to( child_node, new_parent_node=None)
-get_nodes_and_leafs()
-mark_nodes( node=None, level=0)
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = list()
        self.level = None
        
    def __repr__(self):
        role = "Node" if len(self.children)>0 else "Leaf"
        return "{}:{} level {}".format(role,self.value,self.level)

class Tree():
    def __init__(self,node):
        self.root = node
    
    def add(self, child, node=None):
        if node is not None:
            child.parent = node
            node.children.append(child)
        else:
            child.parent = self.root
            self.root.children.append(child)
    
    def del_node(self, node):
        if node == self.root:
            return None
        if node != None:
            parent = node.parent
            if parent is not None:
                parent.children.pop(parent.children.index(node))
                
    def get_node_list(self, from_node=None):
        if from_node is None:
            from_node = self.root
        all = [from_node]
        for i in from_node.children:
            all += self.get_node_list(i)
        return all
        
    def find(self, value, from_node=None):
        all = self.get_node_list(from_node)
        for i in all:
            if i.value == value:
                return i
        return None
    
    def find2(self, value, from_node=None):
        if from_node is None:
            from_node = self.root
        if from_node.value == value:
            return from_node
        for i in from_node.children:
            res = self.find2(value, i)
            if res is None:
                continue
            else:
                return res
        return None
    
    def find_nodes(self, value, from_node=None):
        all = self.get_node_list(from_node=None)
        res = []
        for i in all:
            if i.value == value:
                res.append(i)
        return res
           
    def move_to(self, node, to):
        parent = node.parent
        self.del_node(node)
        node.parent = to
        to.children.append(node)
        
    def get_nodes_and_leafs(self):
        all = {"nodes": [],"leafs":[]}
        def process(node=None):
            if node is None:
                node = self.root
            if len(node.children)>0:
                all["nodes"].append(node)
            else:
                all["leafs"].append(node)
            for i in node.children:
                process(i)
        process()
        return all
    
    def mark_nodes(self, node=None, level=0):
        if node is None:
            node = self.root
        node.level = level
        for i in node.children:
            self.mark_nodes(i,level+1)



if __name__ == "__main__":
    t = Tree(Node("root"))

    t.add(Node("A"), t.root)
    t.add(Node("B"), t.root)
    t.add(Node("Aa"), t.find("A"))
    t.add(Node("Ab"), t.find("A"))
    t.add(Node("Aba"), t.find("Ab"))
    t.add(Node("Ba"), t.find("B"))
    t.del_node(t.find("Ba"))
    t.get_node_list(t.root)
    t.find_nodes("B")
    t.move_to(t.find("Ab"),t.find("B"))
    t.mark_nodes()
    print(t.get_node_list(t.root))
    print(t.get_nodes_and_leafs())
    
    import time
    s = time.time()
     print(t.find("Aba"))
    x = time.time() - s
    print("{}".format(x,'.15f'))
    s2 = time.time()
    print(t.find2("Aba"), "time:", time.time()-s2)