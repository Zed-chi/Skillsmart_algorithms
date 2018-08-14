"""
Set:
-put(value)
-remove(value)
-intersection(set)
-union(set)
-difference(set)
-issubset(set)
"""
from HashTable import HashTable

class PowerSet(HashTable):
    def put(self,value):
        if not self.find(value):
            id = self.seek(value)
            if id:
                self.slots[id] = value
        else:
            return None
    
    def remove(self, value):
        id = self.find(value)
        if id:
            self.slots[id] = None
        
    def intersection(self, someset):
        newset = PowerSet(self.size, self.step)
        for i in someset.slots:
            if self.find(i):
                newset.put(i)
        return newset

    def union(self, someset):
        newset = PowerSet(self.size+someset.size, self.step)
        for i in (self.slots+someset.slots):
            newset.put(i)
        return newset
        
        
    def difference(self, someset):
        newset = PowerSet(self.size, self.step)
        for i in self.slots:
            if someset.find(i) is None:
                newset.put(i)
        return newset
    
    def issubset(self, someset):
        for i in someset.slots:
            if i is not None:
                if not self.find(i) :
                    return False 
        return True

"""
test area
"""
import random

s1 = PowerSet(11,3)
s2 = PowerSet(5,1)
s3 = PowerSet(11,3)

def fill(s):
    for i in range(s.size):
        s.put(random.randint(1,30))

def rep(s):
    return [x for x in s if x is not None]

fill(s1)
fill(s2)
fill(s3)


print("s1-{}\ns2-{}\ns3-{}\n".format(rep(s1.slots), rep(s2.slots), rep(s3.slots)))
print("intersection s1/s2:", rep(s1.intersection(s2).slots))
print("intersection s1/s3:", rep(s1.intersection(s3).slots))
print("\n")
print("union s1/s2:", rep(s1.union(s2).slots))
print("union s1/s3:", rep(s1.union(s3).slots))
print("\n")
print("difference s1/s2:", rep(s1.difference(s2).slots))
print("difference s1/s3:", rep(s1.difference(s3).slots))
print("\n")
print("issubset s1/s2:", s1.issubset(s2))
print("issubset s3/s1:", s3.issubset(s1))

s4 = s1
for i in s4.slots:
    if i is not None:
        s4.remove(i)
        break
print("issubset s1/s4:", s1.issubset(s4))
