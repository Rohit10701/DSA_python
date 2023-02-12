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


root=Node(5)
root.left=Node(4)
root.right=Node(8)
root.left.left=Node(11)
root.left.left.left=Node(7)
root.left.left.right=Node(2)
root.right.left=Node(13)
root.right.right=Node(4)
root.right.right.left=Node(5)
root.right.right.right=Node(1)

flag=False
def find(root,target,curSum,ls,ans):
    if root is None:
        return
    curSum+=root.val
    ls.append(root.val)
    if root.left is None and root.right is None:
        if curSum==target:
            ans.append([ele for ele in ls])
    find(root.left,target,curSum,ls,ans)
    find(root.right,target,curSum,ls,ans)
    ls.pop()
    return
ls=[]
ans=[]
print(find(root,22,0,ls,ans))
print(ans)