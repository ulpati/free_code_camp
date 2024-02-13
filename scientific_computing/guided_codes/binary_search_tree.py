class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        # insertion function for adding a new key to the tree
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # recursive function to insert a key in the tree
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        # search function to find a key in the tree
        return self._search(self.root, key)

    def _search(self, node, key):
        # recursive function to search for a key in the tree
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        # delete function to remove a key from the tree
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # recursive function to delete a key from the tree
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)
        return node

    def _min_value(self, node):
        # helper function to find the minimum value in a subtree
        while node.left is not None:
            node = node.left
        return node.key

    def inorder_traversal(self):
        # function to perform an inorder traversal of the tree
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        # recursive function to perform inorder traversal
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

# testing the BST
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# insert nodes into the binary search tree
for node in nodes:
    bst.insert(node)
print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))

# delete a key from the binary search tree
bst.delete(40)

print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))