class Node:

    def __init__(self, data):
        self.value = data
        self.l = None
        self.r = None

class Solution:

    def depth(self, root):
        if not root:
            return 0
        elif not root.l and not root.r:
            return 1
        else:
            return 1 + max(self.depth(root.l), self.depth(root.r))

    def maxDepth(self, A):
        return self.depth(A)

sol= Solution()
tree = Node(1)
tree.l = Node(2)
tree.r = Node(3)
tree.l.l = Node(4)
tree.l.r = Node(5)
tree.l.l.l = Node(6)
tree.l.l.r = Node(7)
tree.l.l.l.l = Node(66)
tree.l.l.l.l.l = Node(44)
x = input("enter the string ")

print("Height of tree is %d" % (sol.depth(tree)))
