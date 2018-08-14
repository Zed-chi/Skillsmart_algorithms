class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0,item)

    def removeFront(self):
        return self.queue.pop()

    def removeTail(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
    

deq = Deque()
deq.addFront("f1")
deq.addTail("t1")
deq.addFront("f2")
deq.addTail("t2")
while deq.size() > 0:
    print(deq.removeFront())
    print(deq.removeTail())
    
    
def pal(s):
    word = Deque()
    for i in s:
        if i != " ":
            word.addFront(i)
    for j in range(word.size()//2):
        if word.removeFront() != word.removeTail():
            return "- '{}' is not a Palindrome".format(s)
    return "+ '{}' is a Palindrome".format(s)
        
print(pal("qwerty")) #not
print(pal("qweewq")) #yep
print(pal("potop")) #yep
print(pal("oroq oro")) #yep
