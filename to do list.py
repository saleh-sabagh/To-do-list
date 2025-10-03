import csv
class Task:
    def __init__(self , name , details , priority):
        self.name = name
        self.details = details
        self.priority = priority
    
    def __str__(self):
        return f"\t{self.name} :\n\t{self.details}\n\twith {self.priority} priority"
    
    def get_name(self):
        return self.name
    
    def get_details(self):
        return self.details
    
    def get_priority(self):
        return self.priority
    
class ToDoList:
    def __init__(self):
        self.todolist = []
        self.task_csvfile = open("tasks-file.csv" , mode="w" , newline="")
        self.task_csvfile.close()


    def add_task(self , Task):
        self.todolist.append(Task)
        print(self.todolist)
        print("Task added succesfully!")
        self.store_task(Task)

    def delet_task(self , name):
        names_list = [task.get_name() for task in self.todolist]
        if name in names_list:
            i = names_list.index(name)
            task_to_del = self.todolist[i]
            self.todolist.remove(task_to_del)
            print("Task deleted succesfully!")
            self.delet_from_csv(name)
        
        else:
            print("There isnt task with this name in todolist!")

    def show_tasks(self):
        for task in self.todolist:
            print(f"Task{self.todolist.index(task)+1}:\n{task}")
        if self.todolist == []:
            print("there isnt any tasks to do!")

    def load_task_from_csv(self , path):
        
        with open(path , mode="r") as tasksfile:
            reader = csv.reader(tasksfile)
            files_lines = list(reader)
            for row in files_lines:
                new_task = Task(row[0] , row[1] , row[2])
                self.add_task(new_task)

            print("Taks loaded succesfully from csv file!")

    def delet_from_csv(self , name):
        rows = []
        with open("tasks-file.csv" , mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != name:
                    rows.append(row)
        with open("tasks-file.csv" , mode="w" , newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def store_task(self , Task):
        with open("tasks-file.csv" , mode = "a" , newline="" , encoding='utf-8') as opened_file:
            writer = csv.writer(opened_file)
            task_name = Task.get_name()
            task_detail = Task.get_details()
            task_priority = Task.get_priority()
            
            writer.writerow([task_name , task_detail , task_priority])
        



    


def use():
    start = input("Enter 1 to start: ")
    
    try:
        start = int(start)
    except ValueError:
        pass

    if start == 1:
        print("WELCOME TO MY TODOLIST APP!")
        my_todolist = ToDoList()
        while True:
            print("\n===Tasks manager menu===")
            print("1. Add new task")
            print("2. Delet a task")
            print("3. Show tasks list")
            print("4. Load tasks from CSV file")
            print("5. Exit")

            choice = input("Please select an option:")
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid option. try again!")

            if choice == 1:
                tasks_name = input("Enter task's name: ")
                tasks_details = input("Enter task's details: ")
                print("Choose the task's priority")
                print("1. High")
                print("2. Medium")
                print("3. Low")
                priority_selector = input("Please select an option:") 

                try:
                    priority_selector = int(priority_selector)
                except ValueError:
                    pass

                if priority_selector == 1:
                    my_todolist.add_task(Task(tasks_name,tasks_details,"High"))

                elif priority_selector == 2:
                    my_todolist.add_task(Task(tasks_name,tasks_details,"Medium"))
                
                elif priority_selector == 3:
                    my_todolist.add_task(Task(tasks_name,tasks_details,"low"))
                
                else:
                    print("Invalid option. try again!")
            elif choice == 2:
                task_name = input("Please enter task's name you want to delete:")
                my_todolist.delet_task(task_name)

            elif choice == 3:
                my_todolist.show_tasks()

            elif choice == 4:
                path = input("Please enter the csv path:")
                try :
                    my_todolist.load_task_from_csv(path)
                except FileNotFoundError:
                    print("Wrong path! CSV didnt found")

            elif choice == 5:
                break
            
            else:
                print("Invalid option. try again!")
                continue

if __name__ == "__main__":
    use()