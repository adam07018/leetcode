class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(-1,head)
    preNode = dummy
    curNode = head
    while curNode != None:
        if curNode.val == val:
            preNode.next = curNode.next
            curNode = preNode.next
            continue    
        preNode = preNode.next
        if preNode == None:
            break
        curNode = preNode.next
    return dummy.next

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

array = [7,7,7,7]
head = linkList(array)
newhead = removeElements(head, 7)
cur = newhead
while cur!= None:
    print(cur.val)
    cur = cur.next




