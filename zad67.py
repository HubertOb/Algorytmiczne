class BSTNode:

    def __init__(self, key):
        self.val = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        string = f"val: {self.val}, "
        if self.parent:
            string += f"parent: {self.parent.val}, "
        else:
            string += "parent: None, "
        if self.left:
            string += f"left: {self.left.val}, "
        else:
            string += "left: None, "
        if self.right:
            string += f"right: {self.right.val}"
        else:
            string += "right: None, "
        return string

    def printed(self):
        print(self)
        if self.left:
            self.left.printed()
        if self.right:
            self.right.printed()

    def insert(self, new_node_val):
        new_node = BSTNode(new_node_val)
        root = self
        while True:
            if root.val == new_node.val:
                print("Już jest taki element.")
                return
            if new_node.val > root.val:
                if root.right is None:
                    root.right = new_node
                    new_node.parent = root
                    break
                else:
                    root = root.right
            else:
                if root.left is None:
                    root.left = new_node
                    new_node.parent = root
                    break
                else:
                    root = root.left

    def find(self, key):
        root = self
        while root is not None:
            if root.val == key:
                return root
            elif root.val > key:
                root = root.left
            else:
                root = root.right
        return None

    def find_min(self):
        root = self
        while root.left:
            root = root.left
        return root

    def find_max(self):
        root = self
        while root.right:
            root = root.right
        return root

    def successor(self):
        root = self
        if root.right:
            return root.right.find_min()
        child = root
        root = root.parent
        while root and root.right == child:
            child = root
            root = root.parent
        return root

    def predecessor(self):
        root = self
        if root.left:
            return root.left.find_max()
        child = root
        root = root.parent
        while root and root.left == child:
            child = root
            root = root.parent
        return root

    def delete_node(self):
        root = self
        if not root.left and not root.right:
            if root.parent.left == root:
                root.parent.left = None
            else:
                root.parent.right = None
        elif not root.right and root.left:
            if root.parent.left == root:
                root.parent.left = root.left
            else:
                root.parent.right = root.left
        elif root.right and not root.left:
            if root.parent.left == root:
                root.parent.left = root.right
            else:
                root.parent.right = root.right
        else:
            a = root.successor()
            a.delete_node()
            a.parent = self.parent
            a.left = self.left
            a.right = self.right
            a.left.parent=a
            a.right.parent=a
            if a.parent:
                if a.parent.left==self:
                    a.parent.left=a
                else:
                    a.parent.right=a
            self.parent = None
            self.right = None
            self.left = None
            root=a
        while root.parent:
            root = root.parent
        return root


if __name__ == '__main__':
    a = BSTNode(100)
    a.insert(20)
    a.insert(35)
    a.insert(7)
    a.insert(500)
    a.insert(50)
    a.insert(22)
    a.insert(1000)
    a.insert(80)
    a.insert(1001)
    a.insert(200)
    a.insert(49)

    a.printed()
    print(a.find(500))
    print(f"\n{a.find_min()}")
    print(f"\n{a.find_max()}")
    print(f"\n {a.find(200).successor()}")
    print(f"\n {a.find(1001).predecessor()}")

    print("\n\n")
    a.find(100).delete_node().printed()
