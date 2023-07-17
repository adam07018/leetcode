class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class solution:
    def removeNthFromEnd(self, head, n):
        fastptr = head
        slowptr = head
        # initialize
        for i in range(n):
            if fastptr == None: return head
            fastptr = fastptr.next
        # delete first node
        if fastptr is None:
            return slowptr.next
        # move both ptr
        while fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next
        # delete the next node of slowptr
        slowptr.next = slowptr.next.next
        return head

# helper method
def linkList(array):
    if len(array) == 1:
        return ListNode(array[0])
    preNode = ListNode(array[0])
    head = preNode
    for i in range(1, len(array)):
        curNode = ListNode(array[i])
        preNode.next = curNode
        preNode = curNode
    return head

def printList(obj):
    cur = obj
    while cur != None:
        print(cur.val)
        cur = cur.next

array = [0,1,2,3,4,5,6,7,8,9]
head = linkList(array)
head = solution.removeNthFromEnd(solution, head, 10)
printList(head)         
        