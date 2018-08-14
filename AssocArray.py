"""
dict impl
-hash(key)
-seek(key)
-put(key,val)
-find(key, arr)
-is_key(key)
-get(key)
"""


class AssocArray:
    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash(self, value):
        sum = 0
        for i in value:
            sum += ord(i)
        return sum % self.size

    def seek(self, key):
        id = self.hash(key)
        counter = 0
        while counter < self.size:
            if self.keys[id] is not None:
                id = (id + self.step) % self.size
                counter += 1
                continue
            else:
                return id
        return None

    def put(self, key, value):
        id = self.seek(key)
        if id is not None:
            self.keys[id] = key
            self.values[id] = value
        else:
            return None

    def find(self, key, arr):
        id = self.hash(key)
        res = arr[id]
        if res == key:
            return id
        else:
            counter = 0
            while counter < self.size:
                id = (id + self.step) % self.size
                counter += 1
                if arr[id] == key:
                    return id
        return None

    def is_key(self, key):
        return True if self.find(key, self.keys) else False

    def get(self, key):
        id = self.find(key, self.keys)
        return self.values[id] if id else None
