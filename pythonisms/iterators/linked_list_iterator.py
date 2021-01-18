class Node:

    def __init__(self, value, next_=None):

        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator

    def __str__(self):
        out = ''
        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"
        
    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self,other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0 :
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError
        
    def insert(self,value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def append(self,value):
        node = Node(value)

        if not self.head:
            self.head = Node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

if __name__ == "__main__":

    ll = LinkedList([1,2,3])
    first_node = ll[0]

    for node in ll:
        print(node)

    def gen():
        i = 0 
        while True:
            yield i
            i += 1
    num_generator = gen()

    for i in range(100):
        print(next(num_generator))
