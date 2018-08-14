class Node2:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        
    def __lt_(self,y):
        return self.value < y
    
    def __gt__(self,y):
        return self.value > y

class OrderedList:

    def __init__(self,dir="asc"):
        self.dir = dir
        self.head = None
        self.tail = None
    
    def comp(self,node,item):
        if self.dir == "asc":
            return node.value<item.value
        else:
            return node.value>item.value
    
    def __str__(self):
        all = []
        node = self.head
        while node != None:
            all.append(node.value)
            node = node.next
        return "{}".format(all)

    def add(self, item):
        node = self.head
        
        if self.head == None:
            self.head = item
            self.head.prev = None
            self.head.next = None
            self.tail = item
        else:
            while node != None:
                if self.comp(node, item):
                    if node.next != None:
                        node = node.next
                    else:
                        break
                else:
                    before = node.prev
                    item.prev = before
                    item.next = node
                    node.prev = item
                    if before != None:
                        before.next = item
                    if node == self.head:
                        self.head = item
                    return None
            node.next = item
            item.prev = node
            self.tail = item
        
    def find(self, item):
        node = self.head
        while node is not None :
            if node.value == item.value:
                return node
            if self.comp(item, node):
                return "Item not found, interrupt"
            node = node.next
        return None

    def rem(self, nod):
        node = self.find(nod)
        if node != None:
            before = node.prev
            after = node.next
            if before != None:
                before.next = after
            else:
                self.head = after
            if after != None:
                after.prev = before
            else:
                self.tail = before

    def clear(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count = 0
        node = self.head
        while node != None:
            count += 1
            node = node.next
        return count


class OrderedStringList(OrderedList):
    def comp(self, node, item):
        if self.dir == "asc":
            return node.value.strip()<item.value.strip()
        else:
            return node.value.strip()>item.value.strip()

def fill(what, to):
    for i in what:
        to.add(Node2(i))


if __name__ == "__main__":
    od = OrderedList(dir="desc")
    oa = OrderedList(dir="asc")
    sd = OrderedStringList(dir="desc")
    sa = OrderedStringList(dir="asc")
    
    fill([1,5,0,4,23,4,6],oa)
    fill([1,5,0,4,23,4,6],od)
    fill(["a bta", "bc", "poiuy", "ceda", "eczxc", "zsasasd"],sa)
    fill(["a bta", "bc", "poiuy", "ceda", "eczxc", "zsasasd"],sd)

    print("asc =", oa)
    print("desc =", od)
    print(sa)
    print(sd)
    
    print(oa.find(Node2(2)))
    print(od.find(Node2(7)))
