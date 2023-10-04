import ToDoList
import ToDoListItem
from menu import menu

def if_exists(ToDo_List, title):
    for task in get_tasks(ToDo_List=ToDo_List):
        if task.title == title:
            return (True, task)
    return (False, )

def add_task(ToDo_List, caretaker, director, task_title, due_date = None, tags = None, completed = False):
    #adding task to list
    if(not if_exists(ToDo_List=ToDo_List, title=task_title)[0]):
        task = director.construct(task_title, due_date, tags, completed)
        ToDo_List.add_task(task)
        #adding the memento in caretaker
        caretaker.add_memento(ToDo_List.create_memento())
        return True
    else:
        print("error: the title is duplicate please rename it")
        return False

def remove_task(ToDo_List, caretaker, task_title):
    check = if_exists(ToDo_List=ToDo_List, title=task_title)
    if(check[0]):
        ToDo_List.remove_task(check[1])
        #adding the memento in caretaker
        caretaker.add_memento(ToDo_List.create_memento())
        return True
    else:
        print("item not found")
        return False

def get_tasks(ToDo_List):
    return ToDo_List.get_tasks()

def undo(ToDo_List, caretaker):
    #undo in caretaker to move the index to previous location
    caretaker.undo()

    #check if there was something to undo or not
    if(caretaker.get_current_memento() != None):
        #get the current state after undo moved the index to previous location
        ToDo_List.restore_memento(caretaker.get_current_memento())
        return True
    else:
        #print is nothing was there to undo
        print("Nothing to undo")
        return False

def redo(ToDo_List, caretaker):
    #redo in caretaker to move the index to next location
    caretaker.redo()

    #check if there was something to redo or not
    if(caretaker.get_current_memento() != None):
        #get the current state after redo moved the index to next location
        ToDo_List.restore_memento(caretaker.get_current_memento())
        return True
    else:
        #print is nothing was there to redo
        print("Nothing to redo")
        return False

def mark_completed(ToDo_List, caretaker, task_title):
    check = if_exists(ToDo_List=ToDo_List, title=task_title)
    if(check[0]):
        if(check[1].completed == False):
            check[1].completed = True
            #adding the memento in caretaker
            caretaker.add_memento(ToDo_List.create_memento())
            return True
        else:
            print("Item already marked as completed")
            return False
    else:
        print("item not found")
        return False

if __name__ == "__main__":

    ToDo_List = ToDoList.ToDoList()
    caretaker = ToDoList.ToDoListCaretaker()

    todo_item_builder = ToDoListItem.ToDoItemBuilder()
    director = ToDoListItem.ToDoListItemDirector(todo_item_builder)
    
    menu(add_task=add_task, get_tasks=get_tasks, remove_task=remove_task, undo=undo, redo=redo, mark_completed=mark_completed, ToDo_List=ToDo_List, caretaker=caretaker, director=director)