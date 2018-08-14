"""
Cache(size,step) - impl
-hash(i)
-seek(i)
-put(i,j)
-find(i)
-is_key(i)
-get(i)
-remove()
"""
from AssocArray import AssocArray


class Cache(AssocArray):
    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.hits = [None] * self.size

    def put(self, key, value):
        id = self.seek(key)
        if id is None:
            self.remove()
            id = self.seek(key)
        self.keys[id] = key
        self.values[id] = value
        self.hits[id] = 0

    def remove(self):
        id = self.hits.index(min(self.hits))
        if id is not None:
            self.keys[id] = None
            self.values[id] = None
            self.hits[id] = None

    def get(self, key):
        id = self.find(key, self.keys)
        if id != None:
            self.hits[id] += 1
            return self.values[id]
        else:
            return None