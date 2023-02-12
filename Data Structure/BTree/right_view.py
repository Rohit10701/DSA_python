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
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)


def right(root,ls,count):
    if root is None:
        return
    else:
        if count not in ls:
            ls[count]=root.val
        right(root.right,ls,count+1)
        right(root.left,ls,count+1)
    return ls.values()

print(right(root,{},0))


