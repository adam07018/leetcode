class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        slowptr = head
        fastptr = head
        while fastptr != None and fastptr.next != None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                while head != slowptr:  
                    head = head.next
                    slowptr = slowptr.next
                return head
        return None

        