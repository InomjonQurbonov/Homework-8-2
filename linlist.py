class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        x = self.head
        while x:
            print(x.data)
            x = x.next

    def get_total(self):
        x = self.head
        total = 0
        while x:
            if isinstance(x.data, int):
                total += x.data
            x = x.next
        return total

    def get_numbers(self):
        x = self.head
        total = 0
        i = 0
        while x:
            if isinstance(x.data, int):
                total += x.data
                i += 1
            x = x.next
        if i == 0:
            return 0
        else:
            return total / i

    def add_node_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def remove_node_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None or temp.next is None:
            print("Position out of range")
            return
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node
