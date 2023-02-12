class Node:
    val=None
    left=None
    right=None

    def __init__(self,val) -> None:
        self.val=val

class Tree:
    root=None

    def __init__(self,root) -> None:
        self.root=root


def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        return

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

def traverse(root,low,high,totalSum):
    if root is None:
        return totalSum
    print(root.val)
    if root.val>=low or root.val<=high:
        totalSum+=root.val
        traverse(root.left,low,high,totalSum)
        traverse(root.right,low,high,totalSum)
    


sum_=0
print(traverse(root,2,4,sum_))
print(sum_)