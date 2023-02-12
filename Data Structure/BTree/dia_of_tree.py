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

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)


def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1

def find(root):
    if root is None:
        return 0
    left_dia=find(root.left)
    right_dia=find(root.right)
    cur_dia=height(root.left)+height(root.right)
    return max(cur_dia,max(left_dia,right_dia))

print(find(root))