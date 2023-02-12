# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

def midPoint(head):
    slow=head
    fast=head
    count=0
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        count+=1
    return count

print(midPoint(n1))

def removeEle(new_head,n):
        node=Node(0)
        node.next=new_head
        
        curr=node
        count=0
        while count!=n-1:
            curr=curr.next
            count+=1
        curr.next=curr.next.next
        return node.next

def deleteMiddle(head):
    return removeEle(head,midPoint(head))

# print(deleteMiddle(n1))