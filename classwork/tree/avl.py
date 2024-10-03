class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height is initially 1 when the node is inserted

class AVL:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, a):
        aL = a.left
        aLR = aL.right
        aL.right=a
        a.left=aLR
        a.height = max(self.get_height(a.left),self.get_height(a.right))+1
        aL.height = max(self.get_height(aL.left),self.get_height(aL.right))+1
        return aL

    def left_rotate(self, a):
        aR = a.right
        aRL = aR.left
        aR.left=a
        a.right=aRL
        a.height = max(self.get_height(a.left),self.get_height(a.right))+1
        aR.height = max(self.get_height(aR.left),self.get_height(aR.right))+1
        return aR

    def insert(self, root, n):
        # bst insert
        if not root:
            return Node(n)
        elif n < root.key:
            root.left = self.insert(root.left,n)
        elif n >= root.key:
            root.right = self.insert(root.right,n)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # avl rotation 
        b = self.get_balance(root)
        #LL
        if b > 1 and n < root.left.key:
            return self.right_rotate(root)
        # RR
        if b < -1 and n > root.right.key:
            return self.left_rotate(root)
        # LR
        if b > 1 and n > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # RL
        if b < -1 and n < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def delete(self, root, n):
        #bst
        if root is None:
            return root
        elif root.key > n:
            root.left = self.delete(root.left,n)
        elif root.key < n:
            root.right = self.delete(root.right,n)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left 
            else:
                replace = self.find_min(root.right)
                root.key = replace.key
                root.right = self.delete(root.right,replace.key)
        #avl
        if root is None:
            return root
        root.height = max(self.get_height(root.left),self.get_height(root.right))+1
        b=self.get_balance(root)
        # LL
        if b > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        # LR
        if b > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # RR
        if b < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        # RL
        if b < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    
    def find_min(self,curLeaf):
        if curLeaf.left is None:
            return curLeaf
        else: 
            return self.find_min(curLeaf.left)

    def pre_order(self, root):
        if root:
            print(f"{root.key} ", end="")
            self.pre_order(root.left)
            self.pre_order(root.right)

def display(root, level=0):
    # Display the binary tree structure starting from this node
    print(' ' * level * 2 + str(root.key))  # Indentation for levels
    if root.left:  # If the left child exists, display it
        display(root.left,level + 1)
    if root.right:  # If the right child exists, display it
        display(root.right,level + 1)

# Example usage
if __name__ == "__main__":
    tree = AVL()
    root = None

    nodes = [10, 20, 30, 40, 50, 25]
    for node in nodes:
        root = tree.insert(root, node)

    print("Pre-order traversal after insertions:")
    tree.pre_order(root)
    print("\ndisplay")
    display(root)
    
    print("delete 20:")
    tree.delete(root,20)
    tree.pre_order(root)
    print("\ndisplay")
    display(root)

    print("insert 20,5,11,12,7:")
    tree.insert(root,20)
    tree.insert(root,5)
    tree.insert(root,11)
    tree.insert(root,12)
    tree.insert(root,7)
    tree.pre_order(root)
    print("\ndisplay")
    display(root)

