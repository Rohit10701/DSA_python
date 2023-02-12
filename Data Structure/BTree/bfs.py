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


ls=[]
def bfs(root):
    queue=[]
    if root is None:
        return
    queue.append(root)
    while queue:
        ls.append(queue[0].val)
        root=queue.pop(0)
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)

bfs(root)
print(ls)

