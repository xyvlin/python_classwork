
class BinaryTreeNode:
    def __init__(self, value):
        # Initialize a node with a given value and set left and right children to None
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, node):
        # Set the left child of the current node
        self.left = node

    def add_right(self, node):
        # Set the right child of the current node
        self.right = node

    def display(self, level=0):
        # Display the binary tree structure starting from this node
        print(' ' * level * 2 + str(self.value))  # Indentation for levels
        if self.left:  # If the left child exists, display it
            self.left.display(level + 1)
        if self.right:  # If the right child exists, display it
            self.right.display(level + 1)        
    
def insert(curLeaf,n):
    if curLeaf is None: 
        return BinaryTreeNode(n)
    elif n < curLeaf.value:
        curLeaf.left = insert(curLeaf.left,n)
    elif n >= curLeaf.value:
        curLeaf.right = insert(curLeaf.right,n)
    return curLeaf

def find_min(curLeaf):
    if curLeaf.left is None:
        return curLeaf
    else: 
        return find_min(curLeaf.left)

def find_max(curLeaf):
    if curLeaf.right is None:
        return curLeaf
    else: 
        return find_min(curLeaf.right)

def search(curLeaf,key):
    # print(curLeaf.value,key)
    if curLeaf is None:
        return None
    elif curLeaf.value==key:
        return curLeaf
    elif curLeaf.value < key:
        return search(curLeaf.right,key)
    else:
        return search(curLeaf.left,key)

def delete(curLeaf,n):
    if curLeaf is None:
        return curLeaf
    elif curLeaf.value > n:
        curLeaf.left = delete(curLeaf.left,n)
    elif curLeaf.value < n:
        curLeaf.right = delete(curLeaf.right,n)
    else:
        if curLeaf.left is None:
            return curLeaf.right
        elif curLeaf.right is None:
            return curLeaf.left 
        else:
            replace = find_max(curLeaf.left)
            curLeaf.value = replace.value
            curLeaf.left = delete(curLeaf.left,replace.value)
    return curLeaf

def inorderTraversal(root: BinaryTreeNode):
    l = []
    if root.left is not None:
        l.extend(inorderTraversal(root.left))
    l.append(root.value)
    if root.right is not None:
        l.extend(inorderTraversal(root.right))
    return l

def max_depth(root: BinaryTreeNode):
    left=0
    right=0
    if root.left is not None:
        left=max_depth(root.left)
    if root.right is not None:
        right=max_depth(root.right)
    return max(left,right)+1

def isValidBST(root: BinaryTreeNode):
    if root is None:
        return True
    if root.left and root.left.value>root.value:
        return False
    if root.right and root.right.value<root.value:
        return False
    return isValidBST(root.left) and isValidBST(root.right)
def sortedArrayToBST(nums: list) -> BinaryTreeNode:
    if len(nums)==0:
        return None
    mid = len(nums)//2
    root = BinaryTreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

treeStart = BinaryTreeNode(8)
insert(treeStart,3)
insert(treeStart,10)
insert(treeStart,1)
insert(treeStart,6)
insert(treeStart,4)
insert(treeStart,7)
insert(treeStart,14)
insert(treeStart,13)
insert(treeStart,100)
insert(treeStart,0)
treeStart.display()
print("search for 14")
search(treeStart,14).display()
print("delete 14")
delete(treeStart,14)
treeStart.display()
print("delete 10")
delete(treeStart,10)
treeStart.display()
print("inorderTraversal:",inorderTraversal(treeStart))
print("max_depth:",max_depth(treeStart))
print("isValidBST:",isValidBST(treeStart))
treeStart.left.left.left.value=2
print("changed 1's left 0 to 2:",isValidBST(treeStart))
treeStart.left.left.left.value=0
print("sorted array:",inorderTraversal(treeStart))
print("balanced bst: ")
newRoot = sortedArrayToBST(inorderTraversal(treeStart))
newRoot.display()