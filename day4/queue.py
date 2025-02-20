import sys
class Queue:
    def __init__(self,size=5):
        self.que=[]
        self.size=size

    def enqueue(self):
        if len(self.que)==self.size:
            print("the queue is empty")
            return
        element=input("Enter the element to insert into queue:")
        self.que.insert(0,element)
    
    def dequeue(self):
        if not self.que:
            print('queue is empty')
            return
        length=len(self.que)-1
        print(f'Popped element is {self.que[length]}')
        del self.que[length]
    
    def list_queue(self):
        if not self.que:
            print("The queue is empty")
            return
        print("The elements of the queue are:",self.que)
    
class Menu:
    def get_menu(self, queue):
        menu = {
            1 : queue.enqueue,
            2 : queue.dequeue,
            3 : queue.list_queue,
            4 : self.end_of_program
        }
        return menu
    
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        queue = Queue()
        while True:
            choice = int(input('1: Enqueue 2:Dequeue 3:Display 4:Exit. Your choice: '))
            menu = self.get_menu(queue)
            menu.get(choice, self.invalid_choice)()
    
menu = Menu()
menu.run_menu()
