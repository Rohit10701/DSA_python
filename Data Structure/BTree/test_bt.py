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

root=Node(2)
root.left=Node(1)
root.right=Node(3)

def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        return

print(inorder(root))

def fun(root):
    if root is not None:
        fun(root.left)
        fun(root.right)
        root.left,root.right=root.right,root.left
    return root

fun(root)
print(inorder(root))
