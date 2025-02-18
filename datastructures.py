# This module defines the classes Stack, Queue, and PriorityQueue
#----------------------------------------------------------------------

class Stack:
    """
    A simple list implementation of a stack.  Interface methods:
    s.is_empty() returns True if s is empty
    s.insert(x) inserts x into s at the front
    s.remove() removes and returns the first element from s
    s.contains(x) determines if x is contained in s

    """
    def __init__(self):
        self.contents = []

    def is_empty(self):
        return len(self.contents) == 0

    def remove(self):
        if self.is_empty():
            return None
        else:
            return self.contents.pop(0)

    def insert(self, new):
        self.contents.insert(0, new)
        
    def contains(self, elem):
        return elem in self.contents

#----------------------------------------------------------------------

class Queue:
    """
    A simple list implementation of a queue.  Interface methods:
    q.is_empty() returns True if q is empty
    q.insert(x) inserts x into q at the end
    q.remove() removes and returns the first element from q
    q.contains(x) determines if x is contained in q

    """
    def __init__(self):
        self.contents = []

    def is_empty(self):
        return len(self.contents) == 0

    def remove(self):
        if self.is_empty():
            return None
        else:
            return self.contents.pop(0)

    def insert(self, new):
        self.contents.append(new)
        
    def contains(self, elem):
        return elem in self.contents

#----------------------------------------------------------------------

class PriorityQueue:
    """
    This is a heap implementation of a priority queue.  The insert and
    remove operations each take O(log n) time.  To create a new priority
    queue, call the constructor with a function that maps queue elements
    to cost values.  Interface methods:
    q.is_empty() returns True if q is empty
    q.insert(x) inserts x into q according to the cost of x
    q.remove() removes and returns the lowest-cost element from q
    q.contains(x) determines if x is contained in q

    Example:
    q = PriorityQueue(lambda x: x)
    q.insert(5)
    q.insert(1)
    q.insert(3)
    q.insert(8)
    q.insert(2)
    print q.remove()  ==>  1
    print q.remove()  ==>  2
    print q.remove()  ==>  3
    print q.remove()  ==>  5
    print q.remove()  ==>  8
    print q.remove()  ==>  None

    """
    # costFunction is a function that maps queue elements to cost values
    def __init__(self, costFunction):
        # current number of elements in queue
        self.size = 0
        # current maximum size of queue (can be changed - see insert below)
        self.limit = 10
        # the elements themselves (position 0 is not used)
        self.contents = [None] * (self.limit + 1)
        # a function that returns the cost of the element at position i
        self.cost = lambda i: costFunction(self.contents[i])
        
    def contains(self, elem):
        return elem in self.contents
        
    def is_empty(self):
        # returns True if the queue is empty, or else False
        return self.size == 0

    def is_root(self, i):
        # returns True if element i is the root of the heap
        return i == 1
    
    def is_leaf(self, i):
        # returns True if element i is a leaf
        return self.left(i) == None and self.right(i) == None

    def parent(self, i):
        # returns the position of the parent of element i
        return i / 2

    def left(self, i):
        # returns the position of the left child of element i
        child = i * 2
        if child > self.size:
            return None
        else:
            return child

    def right(self, i):
        # returns the position of the right child of element i
        child = i * 2 + 1
        if child > self.size:
            return None
        else:
            return child

    def smallestChild(self, i):
        # returns the position of the smallest child of element i
        leftChild = self.left(i)
        rightChild = self.right(i)
        if leftChild == None:
            return rightChild
        elif rightChild == None:
            return leftChild
        elif self.cost(leftChild) < self.cost(rightChild):
            return leftChild
        else:
            return rightChild

    def swap(self, i, j):
        # swaps elements in positions i and j (using parallel assignment)
        self.contents[i], self.contents[j] = self.contents[j], self.contents[i]

    def insert(self, new):
        # inserts a new element into the heap
        if self.size == self.limit:
            # this doubles the amount of space available in self.contents
            self.contents.extend([None] * self.size)
            self.limit += self.size
        self.size += 1
        self.contents[self.size] = new
        # push new element up toward the root as far as possible
        current = self.size
        while not self.is_root(current):
            parent = self.parent(current)
            if self.cost(current) >= self.cost(parent):
                return
            self.swap(current, parent)
            current = parent

    def remove(self):
        # deletes the current element at the root of the heap and returns it
        if self.size == 0:
            return None
        else:
            min_val = self.contents[1]
            self.contents[1] = self.contents[self.size]
            self.size -= 1
            # push new root element down into the heap as far as possible
            current = 1
            while not self.is_leaf(current):
                child = self.smallestChild(current)
                if self.cost(current) <= self.cost(child):
                    return min_val
                self.swap(current, child)
                current = child
            return min_val