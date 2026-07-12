# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head==None or head.next==None: return head
        temp=head
        count=1
        while temp.next!=None:
            temp=temp.next
            count+=1
        k=k%count
        for i in range(k):
            temp=head
            while (temp.next).next!=None:
                temp=temp.next
            (temp.next).next=head
            head=temp.next
            temp.next=None
        return head