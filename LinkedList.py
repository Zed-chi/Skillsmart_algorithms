"""
Linked List
- add(self, item)
- find(self, val)
- rem(self, val)
- rem_all(self, val)
- clear(self)
- find_all(self, val)
- insert(self, beforeNode, val)
"""
class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        all = []
        node = self.head
        while node != None:
            all.append(node.value)
            node = node.next
        return "{}".format(all)
    
    def get_arr(self):
        all = []
        node = self.head
        while node != None:
            all.append(node.value)
            node = node.next
        return all

    def add(self, item):
        if self.head is None:
            self.head = item
        else :
            self.tail.next = item
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def rem(self, val):
        before = None
        cur = self.head
        after = cur.next
        while cur != None:
            if cur.value == val:
                if before == None:
                    self.head = after
                else:
                    before.next = after
                return 0
            else :
                before = cur
                cur = after
                if cur != None:
                    after = cur.next

    def rem_all(self, val):
        before = self.head
        cur = self.head
        after = cur.next
        while cur != None:
            if cur.value == val:
                before.next = after
                cur = before.next
                if cur != None:
                    after = cur.next
                continue
            before = cur
            cur = after
            if cur != None:
                    after = cur.next

    def clear(self):
        self.head = None
        self.tail = None

    def find_all(self, val):
        all = []
        node = self.head
        while node != None:
            if node.value == val:
                all.append(node)
            node = node.next    
        return all

    def __len__(self):
        count = 0
        node = self.head
        while node != None:
            count += 1
            node = node.next
        return count

    def insert(self, beforeNode, val):
        node = beforeNode
        if node != None:
            after = node.next
            node.next = Node(val)
            node.next.next = after

def fill(what, to):
    for i in what:
        to.add(Node(i))

def list_sum(l1, l2):
    if len(l1) == len(l2) and len(l1) > 0:
        new_list = LinkedList()
        n1 = l1.head
        n2 = l2.head
        while n1 != None:
            new_list.add(Node(n1.value + n2.value))
            n1 = n1.next
            n2 = n2.next
        return new_list

###

if __name__ == "__main__":
    a = LinkedList()
    fill([1,2,3,4,3,2,1],a)
    
    print("#1 removing value 1,4")
    print(a)
    a.rem(1)
    a.rem(4)
    print(a)

    print("#2 removing values 3")
    print(a)
    a.rem_all(3)
    print(a)

    print("#3 clear")
    a.clear()
    print(a)

    print("#4 find all 3 values in [1,2,3,4,3,2,1]")
    fill([1,2,3,4,3,2,1],a)
    print(a.find_all(3))

    print("#5 length of [1,2,3,4,3,2,1]")
    print(len(a))

    print("#6 inserting 123 before 3")
    print(a)
    a.insert(a.find(3),123)
    print(a)
    
    print("testing list sum")
    x = LinkedList()
    y = LinkedList()
    fill([1,2,3],x)
    fill([2,3,4],y)
    print(list_sum(x,y))
