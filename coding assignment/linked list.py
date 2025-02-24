class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            return 
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert(self,position,data):
        new_node=Node(data)

        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        
        current_node=self.head
        current_position=0

        while current_node and current_position < position-1:
            current_node=current_node.next
            current_position+=1
        
        if not current_node:
            print("Not found")
            return
        
        new_node.next=current_node.next
        current_node.next=new_node
        print("Inserted",new_node.data)

    def display(self):
        current_node=self.head
        list1=[]
        while current_node:
            list1.append(current_node.data)
            current_node=current_node.next
        for i in list1[::-1]:
            print(i)
    
    def delete(self,position):
        current_node=self.head
        current_position=0

        if position==0:
            self.head=self.head.next
            return

        while current_node and current_position < position-1:
            current_node=current_node.next
            current_position+=1

        if not current_node or not current_node.next:
            print("Doesn't exists")
            return
        
        previous_node=current_node
        current_node=current_node.next
        previous_node.next=current_node.next
        print("Deleted",current_node.data)

        return
    
    def insert_list_at_position(self, position, second_list):
      
        if not second_list.head:
            print("The second list is empty.")
            return

        current_node = self.head
        current_position = 0

        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1

        if not current_node:
            print("Position out of bounds")
            return

       
        temp = current_node.next 
        current_node.next = second_list.head  
        second_list_tail = second_list.head
        while second_list_tail.next:
            second_list_tail = second_list_tail.next

        second_list_tail.next = temp



class Menu:
    def __init__(self):
        self.linked_list = LinkedList()

    def display_menu(self):
        print("1. Insert at Position")
        print("2. Display List")
        print("3. Delete at Position")
        print("4. Insert another linked list")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Enter your choice: "))
            if choice==1:
                data = input("Enter the data to insert: ")
                position = int(input("Enter position to insert: "))
                self.linked_list.insert(position,data)
            elif choice == 2:
                print("Displaying the list in reverse order:")
                self.linked_list.display()
            elif choice == 3:
                position = int(input("Enter position to delete: "))
                self.linked_list.delete(position)
            elif choice == 4:
                    second_list = LinkedList()
                    second_list_data = input("Enter elements for the second list (comma-separated): ").split(',')
                    for data in second_list_data:
                        second_list.append(data.strip())
                    position = int(input("Enter position to insert the second list: "))
                    self.linked_list.insert_list_at_position(position, second_list)
            elif choice==5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

menu = Menu()
menu.run()