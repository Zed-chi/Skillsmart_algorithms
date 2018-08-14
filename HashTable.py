import random, time


class HashTable:
    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.slots = [None] * self.size
    
    def hash(self, value):
        value = value if isinstance(value, str) else str(value)
        return sum(map(lambda x:ord(x),value)) % self.size
    
    def seek(self,value):
        id = self.hash(value)
        counter = 0
        while counter < self.size :
            if self.slots[id] != None:
                id = (id + self.step) % self.size
                counter += 1
                continue
            else:
                return id
        return None
    
    def put(self,value):
        id = self.seek(value)
        if id != None:
            self.slots[id] = value
        else:
            return None
    
    def find(self, key):
        id = self.hash(key)
        if self.slots[id] == key:
            return id
        else:
            counter = 0
            while counter < self.size:
                id = (id + self.step) % self.size
                counter += 1
                if self.slots[id] == key:
                    return id
        return None
    
def getstr():
    s = ""
    for i in range(10):
        s += str(chr(random.randint(97, 122)))
    return s


"""
проверка
"""

h = HashTable(30,2)

for i in range(h.size+1):
    s = getstr()
    print("===item", i,"===")
    print(" value:", s )
    h.put(s)
    print(" Find index, result is:", h.find(s))
    print("\n")

print(h.slots)