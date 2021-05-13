'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

             2
            / \
           1   2
              / \
             1   2
            / \
           1   1

'''
def check_unival_node(root):
    if root.right and root.left:
        return root.right.val == root.left.val == root.val
    elif root.right is None and root.left is None:
        return True
    else:
        return False

def count_unival(root):
    if root is None:
        return 0

    if check_unival_node(root):
        return 1 + count_unival(root.right) + count_unival(root.left)
    else:
        return 0 + count_unival(root.right) + count_unival(root.left)

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# Let's take the given tree as an input
root = Node(2)
root.right = Node(2)  
root.left = Node(1)
root.right.right = Node(2)
root.right.left = Node(1)
root.right.left.right = Node(1)
root.right.left.left = Node(1)

print(count_unival(root))




