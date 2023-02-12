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
inorder(root)