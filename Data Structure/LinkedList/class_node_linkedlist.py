from email import header


class Node:
    data=0
    next=None

    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    head=None
    def __init__(self,mylist) -> None:
        self.head=Node(mylist[0])
        prev=self.head
        for num in mylist[1:]:
            temp=Node(num)
            prev.next=temp
            prev=temp

    def printer(self):

        temp=self.head
        while temp is not None:
            print(temp.data,end='->')
            temp=temp.next


LList=LinkedList([1,2,3,4,5])
LList.printer()