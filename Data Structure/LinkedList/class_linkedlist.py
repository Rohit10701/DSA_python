class Node:
    val=None
    next=None
    def __init__(self,val) -> None:
        self.val=val
        self.next=None

def createLinkedList(node,ls):
    for i in range(ls):
        node.next=Node(ls[i])
        node=node.next



n1=Node(1)
n2=Node(2)
n3=Node(3)

n1.next=n2
n2.next=n3


ls=[]

curr=n1
while curr:
    ls.append(curr)
    print(curr)
    curr=curr.next
print(ls)
