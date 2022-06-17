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

    def add_to_sorted_list(self, p):
        z = self
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

    def delete_maximum(self):
        first = self
        maximum = self
        maximum_prev=None
        while self.next is not None:
            prev = self
            self = self.next
            if self.val > maximum.val:
                maximum = self
                maximum_prev=prev
        if maximum == first:
            # print("tak")
            a = first
            first = first.next
            a.next = None
            return first
        maximum_prev.next = maximum.next
        # print("t")
        return first

    def insertion_sort(self):
        if self is None:
            return None
        sorted_list = self
        b = self.next
        sorted_list.next = None
        if b is None:
            return sorted_list
        while b is not None:
            a = b
            b = b.next
            a.next = None
            sorted_list = sorted_list.add_to_sorted_list(a)
        return sorted_list

    def write(self):
        x = self
        while x is not None:
            print(x.val)
            x = x.next

    def selection_sort(self):
        global prev_min
        first=self
        a=self
        a_prev=None
        curr_min=self
        while a.next is not None:
            while self.next is not None:
                prev=self
                self=self.next
                if self.val<curr_min.val:
                    curr_min=self
                    prev_min=prev
            if a_prev is None and curr_min!=a:
                first = a
                prev_min.next=a
                a.next,self.next=self.next,a.next
                a=self
            elif curr_min!=a:
                if a.next==curr_min:
                    a_prev.next=curr_min
                    a.next=curr_min.next
                    curr_min.next=a
                    a=curr_min
                else:
                    a.next,curr_min.next=curr_min.next,a.next
                    a_prev.next=curr_min
                    prev_min.next=a
                    a=curr_min
            prev_min=a
            a_prev=a
            a=a.next
            curr_min=a
            self=a
        return first


if __name__ == '__main__':
    list3 = Node(1)
    list3.add(Node(3))
    list3.add(Node(8))
    list3.add(Node(10))
    list3.add(Node(5))
    list3.add(Node(4))
    list3.add(Node(2))
    list3.add(Node(3))
    list3.add(Node(6))
    list3.add(Node(1))
    list3.write()
    print()
    list3=list3.selection_sort()
    list3.write()
