class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(head):
        cur = head
        pre = ListNode()
        realHead = True
        while cur:
            aft = cur.next
            if not aft:
                break
            pre.next = aft
            cur.next = aft.next
            aft.next = cur
            pre = cur
            cur = pre.next
            if realHead:
                head = aft
                realHead = False
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

array = [1,2,3,4]
head = linkList(array)
head = Solution.swapPairs(head)
printList(head)
            