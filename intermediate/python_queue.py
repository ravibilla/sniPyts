# Python queue
class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)
    
q = Queue()
q.enqueue(9)
q.enqueue("Nine")
q.enqueue(4.8)
q.enqueue("Hello World!")
print(q.items)
q.dequeue()
print(q.items)
print(q.size())