#leetcode 112

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


flag=False
def find(root,target,sum):
    global flag
    if root is not None:
        sum=sum+root.val
    if root is None:
        if sum==target:
            flag=True
            return
        else:
            return
    find(root.left,target,sum)
    find(root.right,target,sum)

find(root,1,0)
print(flag)