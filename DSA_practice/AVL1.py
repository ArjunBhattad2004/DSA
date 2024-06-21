#without parent pointer
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def balance(self, node):
        if node is None:
            return None

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Heavy
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Heavy
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed

        return self.balance(root)

    def add(self, key):
        self.root = self.insert(self.root, key)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        return self.balance(root)

    def remove(self, key):
        self.root = self.delete(self.root, key)

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

    def display(self):
        result = self.inorder_traversal(self.root)
        print(result)

# Example Usage
avl_tree = AVLTree()
avl_tree.add(9)
avl_tree.add(5)
avl_tree.add(10)
avl_tree.add(0)
avl_tree.add(6)
avl_tree.add(11)
avl_tree.add(-1)
avl_tree.add(1)
avl_tree.add(2)

print("Original AVL Tree:")
avl_tree.display()

avl_tree.remove(10)
print("\nAVL Tree after removing 10:")
avl_tree.display()