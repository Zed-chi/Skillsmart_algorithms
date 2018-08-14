"""
Heap impl
-add(value):
-del_top()
"""

class Heap():
    def __init__(self,val):
        self.size = 1
        self.arr = [val,]
    
    def add(self, val):
        self.size += 1
        self.arr.append(val)
        id = self.size - 1
        while id>0:
            if self.arr[id]>self.arr[(id-1)//2]:
                x = self.arr[(id-1)//2]
                self.arr[(id-1)//2] = self.arr[id]
                self.arr[id] = x
                id = (id-1)//2
            else:
                break
    
    def del_top(self):
        x = self.arr.pop()
        self.size -= 1
        id = 0
        self.arr[id] = x
        while (2*id + 2)<self.size:
            if self.arr[2*id + 1] > self.arr[2*id + 2]:
                childId = 2*id + 1
            else:
                childId = 2*id + 2
                
            if self.arr[childId] > self.arr[id]:
                x = self.arr[id]
                self.arr[id] = self.arr[childId]
                self.arr[childId] = x
                id = childId
                continue
            else:
                break
            
                

##if __name__ == "__main__":
h = Heap(20)
for i in [10,19,7,8,12,14,5,3,13,11]:
    print("adding {}=>".format(i))
    h.add(i)
    print(h.arr)

print("del_top {}=>".format(h.arr[0]))    
h.del_top()
print(h.arr)
print("del_top {}=>".format(h.arr[0]))
h.del_top()
print(h.arr)
h.add(15)
print(h.arr)
h.add(15)
print(h.arr)