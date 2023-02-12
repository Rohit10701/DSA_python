
class Node:
    def __init__(self,value) -> None:
        self.val=value
        self.next=None
    
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=None

def printList(head):
    while head is not None:
        print(head.val)
        head=head.next

def reverse1(head):
    prev=None
    curr=head
    Next=None

    while curr is not None:
        Next=curr.next
        curr.next=prev
        prev=curr
        curr=Next

reverse1(n1)
printList(n5)


