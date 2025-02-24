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

    def append(self,position,data):
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

        if not current_node:
            print("Doesn't exists")
            return
        
        previous_node=current_node
        current_node=current_node.next
        previous_node.next=current_node.next
        print("Deleted",current_node.data)

        return
    
linked_list=LinkedList()
while (True):
    choice=int(input("1.insert, 2.display, 3.delete. Enter your choice:"))
    if choice==1:
        data=input("Enter the data to insert:")
        position=int(input("Enter position to insert:"))
        linked_list.append(position,data)
    elif choice==2:
        print("Displaying in reverse order")
        linked_list.display()
    elif choice==3:
        position=int(input("Enter position to delete:"))
        linked_list.delete(position)
    else:
        print("Invalid choice")
        break