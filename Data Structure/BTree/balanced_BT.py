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




flag=True
def find(root):
    if root is None:
        return 0
    left=find(root.left)+1
    right=find(root.right)+1
    diff=abs(left-right)
    if diff>1:
        global flag
        flag=False
    h=max(left,right)
    return h
find(root)
print(flag)