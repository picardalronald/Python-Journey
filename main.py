from todo_list import Todolist

def run():
       todo = Todolist();
       while True:
           
           
            print("---> Todo List <---")
            print("1. Add List")
            print("2. View List")
            print("3. Remove List")
            print("4. Exit Program")

            choice = input("Enter Your Choice[1-4] ")
    
            if choice == "1":
                  todo.addTask()

            elif choice == "2":
                todo.viewTask()
    
            elif choice == "3":
                todo.removeTask()

            elif choice == "4":
                todo.exitProgram()
                break
               

            else:  
                print("Invalid choice, please try again.")

run();
