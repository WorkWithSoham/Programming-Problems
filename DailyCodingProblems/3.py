'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
------------------------------------------------------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
------------------------------------------------------------------------------


The following test should pass:
------------------------------------------------------------------------------
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
------------------------------------------------------------------------------
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Used to define object for a developer
    def __repr__(self):
        return ('Node(' + repr(self.val) + ', '
                + repr(self.left) + ', '
                + repr(self.right) + ')')

    # Used to define object for a non developer person
    # def __str__(self):
    #     return str(self.left) + " <- Node -> " + str(self.right)

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.val == other.val and
                    self.left == other.left and
                    self.right == other.right)
        return False


serialize = repr  # assign functions to the variables #python property
deserialize = eval  # assign functions to the variables #python property

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(node)  # Node('root', Node('left', Node('left.left', None, None), None), Node('right', None, None))

print(deserialize(serialize(node)).left.left.val == 'left.left')  # True
