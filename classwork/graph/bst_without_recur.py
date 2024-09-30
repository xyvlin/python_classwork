from bst import BinaryTreeNode
from bst import treeStart

def max_depth(root: BinaryTreeNode):
    if not root:
        return 0
    s=[]
    depth=0
    cur = (root,1)
    while cur[0] or s:
        while cur[0]:
            s.append(cur)
            cur = (cur[0].left,cur[1]+1)
        cur = s.pop()
        if cur[0]:
            depth = max(depth,cur[1])
        cur = (cur[0].right,cur[1]+1)
    return depth
    
def isValidBST(cur: BinaryTreeNode):
    if not cur:
        return False
    s=[]
    while cur or s:
        while cur:
            s.append(cur)
            cur = cur.left
        cur = s.pop()
        if cur:
            if cur.left and cur.left.value>cur.value:
                return False
            if cur.right and cur.right.value<cur.value:
                return False
        cur = cur.right
    return True