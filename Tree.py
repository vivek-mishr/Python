class Node:

    def __init__(self, data):
        self.value = data
        self.l = None
        self.r = None


def maxDepth(node):
    if node is None:
        return 0;

    else:

        lh = maxDepth(node.l)
        rh = maxDepth(node.r)

        if lh > rh:
            return lh + 1
        else:
            return rh + 1


tree = Node(1)
tree.l = Node(2)
tree.r = Node(3)
tree.l.l = Node(4)
tree.l.r = Node(5)
tree.l.l.l = Node(6)
tree.l.l.r = Node(7)
tree.l.l.l.l = Node(66)
tree.l.l.l.l.l = Node(44)

print("Height of tree is %d" % (maxDepth(tree)))
