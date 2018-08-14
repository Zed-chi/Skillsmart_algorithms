"""
BinaryArray impl
-add(value):
-find(value)
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        
    def __repr__(self):
        return "{}".format(self.value)
    
class BinaryArray():
    def __init__(self,node):
        self.size = 15
        self.arr = ["null"]*self.size
        self.arr[0] = node
    
    def parent(self, node):
        id = self.arr.index(node)
        return (id-1)//2
    
    def left(self, node):
        id = self.arr.index(node)
        return 2*id + 1
    
    def right(self, node):
        id = self.arr.index(node)
        return 2*id + 2
    
    def add(self, key):
        res = self.find(key)
        child = Node(key)
        if res != None and res < 0:
            self.arr[-res] = child
        
    def find(self, key):
        id = 0
        node = self.arr[id]
        while id < self.size:
            parent = node
            if node.value == key:
                return self.arr.index(node)
            if node.value>key:
                id = self.left(node)
                if id < self.size:
                    node = self.arr[id]
            else:
                id = self.right(node)
                if id < self.size:
                    node = self.arr[id]
            if node == "null":
                return -id
        return None



if __name__ == "__main__":
    a = BinaryArray(Node(50))
##    заполнение из примера
    x = [25,75,62,84,37,31,55,43,92]
    for i in x:
        a.add(i)
    print(a.arr)
    
##дозаполнение
    y = [20,22,15,70,80]
    for i in y:
        a.add(i)
    print(a.arr)