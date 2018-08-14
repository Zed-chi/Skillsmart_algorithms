from Stack import Stack

class Queue:    
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
        
    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        while self.inbox.size()>0:
            self.outbox.push(self.inbox.pop())
        item = self.outbox.pop()
        while self.outbox.size()>0:
            self.inbox.push(self.outbox.pop())
        return item

    def size(self):
        return self.inbox.size()
    
    def __repr__(self):
        x = []
        for i in range(self.size()):
            item = self.dequeue()
            x.append(item)
            self.enqueue(item)
        return "{}".format(x)            
            
        
if __name__ == "__main__":
    qu = Queue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)

    print("queue:", qu)
        
    def roll(num, q):
        if num >= q.size():
            raise IndexError
        print("It was {}".format(q))
        for i in range(num):
            q.enqueue(q.dequeue())
        print("It now {}".format(q))

    roll(2,qu)
