class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return ("Queue is empty")

    def size(self):
        return len(self.items)

# Creating a queue
queue = Queue()

# Checking if queue is empty
print("Queue is empty:", queue.is_empty())

# Enqueuing items into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeuing an item from the queue
print("Dequeued item:", queue.dequeue())

# Getting the size of the queue
print("Queue size:", queue.size())

