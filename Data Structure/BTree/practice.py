from typing import List, Tuple
class TreeNode():
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self) -> str:
        queue = [self]
        res = ""
        while len(queue) > 0:
            curr = queue.pop(0)
            res += (str(curr.val) + "->")
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        
        return res
                

def main() -> None:
    root = TreeNode(1)
    l1 = TreeNode(2)
    r1 = TreeNode(2)
    root.left, root.right = l1, r1
    l1: List[int] = [1,2,3]
    t1: Tuple(int,str) = (1, "a")
    print(root)
    pass


if __name__ == "__main__":
    main()