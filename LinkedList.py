class ListNode(object):
    def __init__(self, elem = 0, next = None):
        self.elem = elem
        self.next = next
        return    
    
class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        return
    def add_item(self, item):
        if self.head == None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

