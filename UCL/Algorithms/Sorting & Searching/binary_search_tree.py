class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self, root, val):
        if root == None:
            root = Node(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def query(self, root, val):
        if root == None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)

    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def findMax(self, root):
        if root.right:
            return self.findMax(root.right)
        else:
            return root

    def delNode(self, root, val):
        if root == None:
            return 
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)
        else:
            if root.left and root.right:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.delNode(root.right, temp.val)
            elif root.right == None and root.left == None:
                root = None
            elif root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
        return root

    def printTree(self, root): #inOrder
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, end = ' ')
        self.printTree(root.right)

