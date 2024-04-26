from linlist import LinkedList, Node

numbers = LinkedList()
numbers.head = Node(1)
numbers.head.next = Node(2)
numbers.head.next.next = Node(3)
numbers.head.next.next.next = Node(4)
numbers.head.next.next.next.next = Node(5)
numbers.head.next.next.next.next.next = Node(6)
numbers.head.next.next.next.next.next.next = Node(7)
numbers.head.next.next.next.next.next.next.next = Node(8)
numbers.head.next.next.next.next.next.next.next.next = Node(9)
numbers.head.next.next.next.next.next.next.next.next.next = Node(10)

numbers.print_list()
hisob = numbers.get_total()
hisob2 = numbers.get_numbers()

print("Barcha list ma'lumotlarini qo'shish:", hisob)  # agar integer bo'lsa
print("Listning O'rta arifmetigini topish:", hisob2)  # agar integer bo'lsa
# add data for node
num1 = int(input("Enter the number for adding node: "))
num2 = int(input("Enter the data for adding node: "))
numbers.add_node_at_position(num1, num2)
print("\nList after adding node at position 2:")
numbers.print_list()
# remove data in node
num = int(input("Enter a number for removing node: "))
numbers.remove_node_at_position(num)
print("\nList after removing node at position 1:")
numbers.print_list()
