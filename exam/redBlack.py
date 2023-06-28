class Node:
    def __init__(self, value, color, left=None, right=None, parent=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value, "Red")
        if self.root is None:
            self.root = node
            self.root.color = "Black"
        else:
            self._insert_node(self.root, node)
            self._fix_insert(node)

    def _insert_node(self, root, node):
        if node.value < root.value:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self._insert_node(root.left, node)
        else:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self._insert_node(root.right, node)

    def _fix_insert(self, node):
        while node.parent is not None and node.parent.color == "Red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self._rotate_left(node.parent.parent)

        self.root.color = "Black"

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child


# Example usage:
tree = RedBlackTree()

# Initialize with the starting set of nodes
tree.insert(24)
tree.insert(18)
tree.insert(26)
tree.insert(5)
tree.insert(20)
tree.insert(27)
tree.insert(2)
tree.insert(7)
tree.insert(23)


# Print the tree in a visually appealing format
def print_tree(node, indent="", is_left=True):
    if node is not None:
        direction = "├── " if is_left else "└── "
        color = "B" if node.color == "Black" else "R"
        print(indent + direction + str(node.value) + " (" + color + ")")
        indent += "│   " if is_left else "    "
        print_tree(node.left, indent, True)
        print_tree(node.right, indent, False)

print('Starting Red-Black Tree:')
print_tree(tree.root)

# Insert a new node
tree.insert(21)

print('')
print("Red-Black Tree after inserting a new node:")
print_tree(tree.root)
