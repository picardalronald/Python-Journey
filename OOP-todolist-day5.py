class Todolist:
    def __init__(self):
        self.task= []

    def addTask(self):
        task = input("Enter your Task: ")
        self.task.append(task)
        print(f"Task listed! {task}")


    def viewTask(self):
        if not self.task:
            print("No task available!")
        else:
            for i, task in enumerate(self.task, start=1):
                print(f"Your Task {i}. {task}")

    def removeTask(self):
        if not self.task:
            print("No task Available!")
        else:
           self.viewTask()
           try:
               task_move = int(input("Enter number you want to remove: "))
               if 1 <= task_move <= len(self.task):
                  removed = self.task.pop(task_move - 1)
                  print(f"Task '{removed}' removed!")
               else:
                    print("Invalid task number.")
           except ValueError:
                print("Please enter a valid number.")

    def exitProgram(self):
        if not self.task:
            print("Goodbye i hope you Enjoy it :)")
            exit


    def run(self):
       while True:
           
           
            print("---> Todo List <---")
            print("1. Add List")
            print("2. View List")
            print("3. Remove List")
            print("4. Exit Program")

            choice = input("Enter Your Choice[1-4] ")
    
            if choice == "1":
                  self.addTask()

            elif choice == "2":
                self.viewTask()
    
            elif choice == "3":
                self.removeTask()

            elif choice == "4":
                self.exitProgram()
                break
               

            else:  
                print("Invalid choice, please try again.")

todo = Todolist()
todo.run()




            

