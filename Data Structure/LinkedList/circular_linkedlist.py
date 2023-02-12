
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
n5.next=n1

# def printList(head):
#     while head is not None:
#         print(head.val)
#         head=head.next``

def check(head):
    
    s=head
    f=head
    while f!=None and f.next!=None:
        s=s.next
        f=f.next.next
        if s==f:
            return True
    return False

check(n1)
print(check(n1))
