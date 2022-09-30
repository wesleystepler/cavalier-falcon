class PriorityQueue:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, queue=[]):
        self.queue = queue

    def add(self, item):
        self.queue.append(item)

    def remove(cur_node): # Removes the node-edge pair with the lowest cost that stems from cur_node
        
