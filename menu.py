import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task_menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director):
    clear_screen()
    print("ADDING TASK")
    title = input("Enter task title: ")
    due_date = input("Enter task due date (hit enter key to skip): ")
    tags = input("Enter task tags seperated by space (hit enter key to skip): ").split()

    if(len(due_date) == 0):
        due_date = None
    if(len(tags) == 0):
        tags == None
    if(add_task(ToDo_List, caretaker, director, title, due_date, tags)):
        print("task added successfully")
    time.sleep(2)
    menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director)

def remove_task_menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director):
    clear_screen()
    print("REMOVING TASK")
    title = input("Enter title of task to be removed: ")
    if(remove_task(ToDo_List, caretaker, title)):
        print("task removed successfully")
    time.sleep(2)
    menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director)
    
def display_items(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director):
    clear_screen()
    tasks = get_tasks(ToDo_List)
    print("DISPLAYING TASKS")
    print("1. Enter 1 to show all tasks")
    print("2. Enter 2 to show completed tasks")
    print("3. Enter 3 to show pending tasks")
    choice = input("Choice: ")

    match choice:
        case "1":
            for index, task in enumerate(tasks):
                print(f"{index + 1}. Title: {task.title}, Due-Date: {task.due_date}, tags: {task.tags}, completed?: {task.completed}")
        case "2":
            for index, task in enumerate(tasks):
                if(task.completed == True):
                    print(f"{index + 1}. Title: {task.title}, Due-Date: {task.due_date}, tags: {task.tags}")
        case "3":
            for index, task in enumerate(tasks):
                if(task.completed == False):
                    print(f"{index + 1}. Title: {task.title}, Due-Date: {task.due_date}, tags: {task.tags}")

    print()
    input("press enter to go back to menu")
    menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director)

def undo_menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director):
    if(undo(ToDo_List, caretaker)):
        undo(ToDo_List, caretaker)
        print("Undo Successful")
    time.sleep(2)
    menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director)

def redo_menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director):
    if(redo(ToDo_List, caretaker)):
        redo(ToDo_List, caretaker)
        print("Redo Successful")
    time.sleep(2)
    menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director)

def mark_completed_menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director):
    task_title = input("Enter Task Title: ")
    if(mark_completed(ToDo_List, caretaker, task_title)):
        print("Task marked as completed")
    time.sleep(2)
    menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director)

def menu(add_task, remove_task, get_tasks, undo, redo, mark_completed, ToDo_List, caretaker, director):

    clear_screen()
    print("---------------To-Do LIST---------------")
    print("1. Enter 1 to add task to ToDoList")
    print("2. Enter 2 to remove task from ToDoList")
    print("3. Enter 3 to display tasks from ToDoList")
    print("4. Enter 4 to undo previous action")
    print("5. Enter 5 to redo")
    print("6. Enter 6 to mark a task as completed")
    print()
    choice = input("Choice: ")

    match choice:
        case "1":
            add_task_menu(add_task=add_task, remove_task=remove_task, get_tasks=get_tasks, undo=undo, redo=redo, mark_completed=mark_completed, ToDo_List=ToDo_List, caretaker=caretaker, director=director)
        case "2":
            remove_task_menu(add_task=add_task, remove_task=remove_task, get_tasks=get_tasks, undo=undo, redo=redo, mark_completed=mark_completed, ToDo_List=ToDo_List, caretaker=caretaker, director=director)
        case "3":
            display_items(add_task=add_task, remove_task=remove_task, get_tasks=get_tasks, undo=undo, redo=redo, mark_completed=mark_completed, ToDo_List=ToDo_List, caretaker=caretaker, director=director)
        case "4":
            undo_menu(add_task=add_task, remove_task=remove_task, get_tasks=get_tasks, undo=undo, redo=redo, mark_completed=mark_completed, ToDo_List=ToDo_List, caretaker=caretaker, director=director)
        case "5":
            redo_menu(add_task=add_task, remove_task=remove_task, get_tasks=get_tasks, undo=undo, redo=redo, mark_completed=mark_completed, ToDo_List=ToDo_List, caretaker=caretaker, director=director)
        case "6":
            mark_completed_menu(add_task=add_task, remove_task=remove_task, get_tasks=get_tasks, undo=undo, redo=redo, mark_completed=mark_completed, ToDo_List=ToDo_List, caretaker=caretaker, director=director)