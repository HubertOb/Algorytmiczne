class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, p):
        z = self
        while z.next is not None:
            z = z.next
        z.next = p
        return self

    def write(self):
        x = self
        while x is not None:
            print(x.val)
            x = x.next

    def reverse_list_recursively(self, counter=0):
        if self.next is None:
            return self
        if counter == 0:
            z = self
            while z.next is not None:
                z = z.next
        p = self.next
        self.next = None
        p.reverse_list_recursively(counter + 1).next = self
        self.next = None
        if counter == 0:
            return z
        return self

    def reverse_list_iteratively(self):
        prev = None
        curr = self
        next_item = self.next
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = next_item
            if next_item is not None:
                next_item = next_item.next
        return prev


if __name__ == '__main__':
    list1 = Node(1)
    list1.add(Node(2))
    list1.add(Node(3))
    list1.add(Node(4))
    list1.add(Node(5))
    list1.add(Node(6))
    list1.add(Node(7))
    list1.add(Node(8))
    list1.write()
    print()
    list1 = list1.reverse_list_recursively()
    list1.write()
    print()
    list1 = list1.reverse_list_iteratively()
    list1.write()
