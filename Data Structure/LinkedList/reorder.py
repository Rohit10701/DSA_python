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
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow
def reverse(node):
    prev=None
    cur=node
    temp=node
    while cur!=None:
        cur=cur.next
        temp.next=prev
        prev=temp
        temp=cur
    return prev
        
# 1 2 3 4 5       
def reorderList(head) -> None:
    #find the midpoint of node:
        mid=midPoint(head)
        print("mid",mid.val)
        cur=head
        while cur.next!=mid:
            cur=cur.next
        node=reverse(mid)
        print(cur.val)
        print("node",node.val)
        
        
        temp=head
        new_cur=head.next
        cur_temp=node
        cur=node.next

        print("temp",temp.val)
        print("new_cur",new_cur.val)
        print("cur_temp",cur_temp.val)
        print("cur",cur.val)
        
        while temp!=None and cur!=None:
            temp.next=cur_temp
            # print("temp",temp.val)

            cur_temp.next=new_cur
            # print("cur_temp",cur_temp.val)
            # print("new_cur_val",new_cur.next.val)
            temp=new_cur
            # print("temp",temp.val)
            if new_cur:
                new_cur=new_cur.next
            # print("new_cur",new_cur.val)
            cur_temp=cur
            # print("cur_temp",cur_temp.val)
            if cur:
                cur=cur.next
            
        return head

print(reorderList(n1))
            
            
        
        
        
        
        
        
        
        
        
        
        