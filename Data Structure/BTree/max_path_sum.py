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

def find(root,curSum,ls,ans):
    if root is None:
        return
    curSum+=root.val
    ls.append(root.val)
    if root.left is None and root.right is None:
        ans.append([ele for ele in ls])
    find(root.left,curSum,ls,ans)
    find(root.right,curSum,ls,ans)
    ls.pop()
    return

ls=[]
ans=[]
find(root,0,ls,ans)
res=[]
for ele in ans:
    res.append(sum(ele))
print(max(res))

