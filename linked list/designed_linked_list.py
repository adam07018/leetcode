class MyLinkedList:
    # this version is with head
    def __init__(self):
        # dummy
        self.value = -1
        self.next = None

    def get(self, index):
        cur = self.next
        while cur != None:
            if index == 0:
                return cur.value
            index -= 1
            cur = cur.next
        return -1

    def addAtHead(self, val):
        nextNode = self.next
        newNode = MyLinkedList()
        newNode.value = val
        newNode.next = nextNode
        self.next = newNode

    def addAtTail(self, val):
        cur = self.next
        newNode = MyLinkedList()
        newNode.value = val
        if cur == None:
            self.next = newNode
            return
        while cur.next != None:
            cur = cur.next
        cur.next = newNode


    def addAtIndex(self, index, val) :
        pre = self
        cur = self.next
        if cur == None and index == 0:
            newNode = MyLinkedList()
            newNode.value = val
            newNode.next = None
            pre.next = newNode
        while pre != None:
            if index == 0:
                newNode = MyLinkedList()
                newNode.value = val
                newNode.next = cur
                pre.next = newNode
                return
            index -= 1
            pre = cur
            if cur == None:
                break
            cur = cur.next
                

    def deleteAtIndex(self, index: int) -> None:
        pre = self
        cur = self.next
        while cur!= None:
            aft = cur.next
            if index == 0:
                pre.next = aft
                return
            index -= 1
            pre = pre.next
            cur = cur.next 

    

# Parameter: head is dummy head
def reverseList(head):
    head = head.next # get the real head
    head.next = reverse(head,None)
    return head
    
def reverse(cur, pre):
    if cur == None:
        return pre
    aft = cur.next
    cur.next = pre
    return reverse(aft, cur)    


def printList(obj):
    cur = obj.next
    while cur != None:
        print(cur.value)
        cur = cur.next

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(4)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(1)
reverseList(obj)
printList(obj)
