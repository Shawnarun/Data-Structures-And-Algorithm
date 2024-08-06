class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):

        new_node = Node(data)

        if not self.head:
            self.head= new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next=new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data ,end="->")
            cur=cur.next

        print(None)


li = LinkedList()
li.append(15)
li.append(25)
li.append(32)
li.append(28)

li.print_list()
