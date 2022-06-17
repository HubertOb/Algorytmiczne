class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def write(self):
        x = self
        while x is not None:
            print(x.val)
            x = x.next

    def add_to_sorted_list(self, p):
        z = self
        p=Node(p)
        if p.val < z.val:
            p.next = z
            return p
        prev = None
        while z is not None:
            if z.val >= p.val:
                if prev is None:
                    p.next = z
                    return p
                else:
                    prev.next = p
                    p.next = z
                    return self
            prev = z
            z = z.next
        prev.next = p
        return self


def merge(w1, w2):
    if w1.val < w2.val:
        node = w1
        w1 = w1.next
    else:
        node = w2
        w2 = w2.next
    first = node
    while w1 is not None and w2 is not None:
        if w1.val < w2.val:
            node.next = w1
            node = node.next
            w1 = w1.next
        else:
            node.next = w2
            node = node.next
            w2 = w2.next
    if w1 is None:
        node.next = w2
    else:
        node.next = w1
    return first


if __name__ == '__main__':
    list1 = Node(1)
    list1.add_to_sorted_list(3)
    list1.add_to_sorted_list(6)
    list1.add_to_sorted_list(8)
    list1.add_to_sorted_list(9)
    list1.add_to_sorted_list(10)
    list1.add_to_sorted_list(12)
    list2 = Node(2)
    list2.add_to_sorted_list(4)
    list2.add_to_sorted_list(5)
    list2.add_to_sorted_list(7)
    list2.add_to_sorted_list(11)
    list2.add_to_sorted_list(13)
    merged_list = merge(list2, list1)
    merged_list.write()
