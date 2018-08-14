"""
BinaryTree impl
-add(value):
-del_node(value):
-find(value)
-min_max(node=None)
-get_node_list()
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        
    def __str__(self):
        return "Node{}".format(self.value)
    
class BinaryTree():
    def __init__(self,node):
        self.root = node
    
    def add(self, key):
        res = self.find(key)
        child = Node(key)
        if res["node"] == None:
            if key > res["parent"].value:
                res["parent"].right_child = child
            else:
                res["parent"].left_child = child
            child.parent = res["parent"]
            
    def del_node(self, key):
        res = self.find(key)
        node = res["node"]
##        защита от дурака
        if node == self.root:
            return None
        parent = res["parent"]
        if node != None:
            left = node.left_child
            right = node.right_child
            if right != None:
                new_node = self.get_node_list(right)[0]
                if new_node.right_child != None:
                    self.del_node(new_node.value)
            elif left != None:
                new_node = left
            else:
                new_node = None
            if new_node != None:
                r = self.find(new_node.value)
                if r["role"] == "left":
                    new_node.parent.left_child = None
                else:
                    new_node.parent.right_child = None
                new_node.parent = parent
                new_node.left_child = left
                if left != None:
                    left.parent = new_node
                if new_node != right:
                    new_node.right_child = right
                    right.parent = new_node
                else:
                    new_node.right_child = None
            if res["role"] == "left":
                parent.left_child = new_node
            else:
                parent.right_child = new_node
        
    def get_node_list(self, from_node=None):
        if from_node == None:
            from_node = self.root
        all = []
        def process(node):
            if node != None:
                arr = [node]
                right = process(node.right_child)
                if right != None:
                    arr = arr + right
                left = process(node.left_child)
                if left != None:
                    arr = left + arr
            else:
                return None
            return arr
        all+= process(from_node)
        return all
            
    def min_max(self):
        temp = self.get_node_list()
        return [temp[0].value,temp[len(temp)-1].value]

    def min_max2(self, node = None):
        if node == None:
            node = self.root
        left = node.left_child
        right = node.right_child
        while True:
            if left.left_child != None:
                left = left.left_child
            else:
                break
        while right != None:
            if right.right_child != None:
                right = right.right_child
            else:
                break
        return [left.value, right.value]
        
    def find(self, key):
        result = {"node":None, "parent":None, "role":None}
        node = self.root
        while node is not None:
            parent = node
            if node.value == key:
                result["node"] = node
                break
            if node.value<key:
                result["role"] = "right"
                node = node.right_child
            else:
                result["role"] = "left"
                node = node.left_child
            result["parent"] = parent
            if node == None:
                result["role"] = None
        return result
    
    def get_level(self, node, level=0):        
        if node != None:
            level+=1
            left = self.get_level(node.left_child, level)
            right = self.get_level(node.right_child, level)
            return max(left, right)
        else:
            return level
        
    def display(self):
        level = self.get_level(self.root)
        all = [""]*level
        def process(node, lev=0, i=1):
            if (level-lev)>0:
                if node != None:                
                    all[lev]+=("  "*i)+str(node.value)+("  "*i)
                    process(node.left_child, lev+1, i//2)
                    process(node.right_child,lev+1, i//2)
                else:
                    all[lev]+=("  "*i)+"   "+("  "*i)                
        process(self.root, 0, level*2)
        return "".join(list(map(lambda x:x+"\n\n", all)))



if __name__ == "__main__":
    t = BinaryTree(Node(8))
    t.add(4)
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(6)
    t.add(12)
    t.add(10)
    t.add(14)
    t.add(13)
    t.add(15)
    print(t.display())
    print(t.min_max2(t.find(4)["node"]))