import ctypes
class DynArray:
    
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
    
    def __repr__(self):
        x = []
        
        for i in range(self.count):
            x.append(self.array[i])
        return "{}".format(x)
    
    def __len__(self):
        return self.count
    
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    
    def __getitem__(self,i):
        if isinstance(i, slice):
            return [self.array[x] for x in range(i.start, i.stop)]
        
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        
        return self.array[i]
    
    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        
    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1
    
    def insert(self, i, item):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        if i < 0 or i >= self.count:
            raise IndexError
        temp = self.array[i:self.count]
        self.array[i] = item
        
        for j in range(len(temp)):
            self.array[i+j+1] = temp[j]
        self.count+=1

    def delete(self, i):
        def cap():
            if self.count*2<self.capacity and self.capacity>32:                    
                self.resize(0.5*self.capacity)
                cap()
        cap()
        if i < 0 or i >= self.count:
            raise IndexError
        
        temp = self.array[i+1:self.count]
        for j in range(len(temp)):
            self.array[i+j] = temp[j]
        self.count-=1
            
    
"""
some tests
"""


da = DynArray()
def x():
    for i in range(16):
        da.append(i*8)
x()
print(da)
da.insert(3,999)
print(da)
da.delete(3)
print(da)