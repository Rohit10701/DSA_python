from heapq import heapify


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(2)
n5=Node(34)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=None
def printList(head):
    while head is not None:
        print(head.val)
        head=head.next
    
def palin(head):
    s=head
    f=head
    while f.next and f.next.next:
        s=s.next
        f=f.next.next
    cur1=s.next
    s.next=None

    