class ListNode:
    def __init__(self,value) -> None:
        self.val=value
        self.next=None
    
n1=ListNode(9)
n2=ListNode(9)
n3=ListNode(9)
n4=ListNode(9)
n5=ListNode(9)

l1=ListNode(9)
l2=ListNode(9)


n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=None

l1.next=l2
l2.next=None

def add(l1,l2):
        cur1=l1
        cur2=l2
        ans=ListNode(0)
        res=ans
        carry=0
        while cur1 and cur2:
            sum=cur1.val+cur2.val+carry
            if sum>=10:
                carry=int(sum/10)
                res.next=ListNode(int(sum%10))
            else:
                carry=0
                res.next=ListNode(sum)
            res=res.next
            cur1=cur1.next
            cur2=cur2.next
        
        
        if cur1 is not None:
            while cur1:
                sum=cur1.val+carry
            if sum>=10:
                carry=int(sum/10)
                res.next=ListNode(int(sum%10))
            else:
                carry=0
                res.next=ListNode(sum)
                res.next=ListNode
            res=res.next
            cur1=cur1.next
            
        
        if cur2 is not None:
            while cur2:
                sum=cur2.val+carry
            if sum>=10:
                carry=int(sum/10)
                res.next=ListNode(int(sum%10))
            else:
                carry=0
                res.next=ListNode(sum)
                res.next=ListNode
            res=res.next
            cur2=cur2.next
        return ans.next

print(add(n1,l1))