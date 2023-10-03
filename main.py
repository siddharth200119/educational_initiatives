import ToDoList
import ToDoListItem

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
    else:
        print("the title is duplicate please rename it")

def remove_task(ToDo_List, caretaker, task_title):
    check = if_exists(ToDo_List=ToDo_List, title=task_title)
    if(check[0]):
        ToDo_List.remove_task(check[1])
        #adding the memento in caretaker
        caretaker.add_memento(ToDo_List.create_memento())
    else:
        print("item not found")

def get_tasks(ToDo_List):
    return ToDo_List.get_tasks()

def undo(ToDo_List, caretaker):
    #undo in caretaker to move the index to previous location
    caretaker.undo()

    #check if there was something to undo or not
    if(caretaker.get_current_memento() != None):
        #get the current state after undo moved the index to previous location
        ToDo_List.restore_memento(caretaker.get_current_memento())
    else:
        #print is nothing was there to undo
        print("Nothing to undo")

def redo(ToDo_List, caretaker):
    #redo in caretaker to move the index to next location
    caretaker.redo()

    #check if there was something to redo or not
    if(caretaker.get_current_memento() != None):
        #get the current state after redo moved the index to next location
        ToDo_List.restore_memento(caretaker.get_current_memento())
    else:
        #print is nothing was there to redo
        print("Nothing to redo")

if __name__ == "__main__":

    ToDo_List = ToDoList.ToDoList()
    caretaker = ToDoList.ToDoListCaretaker()

    todo_item_builder = ToDoListItem.ToDoItemBuilder()
    director = ToDoListItem.ToDoListItemDirector(todo_item_builder)
    #test code to check if function work

    print("adding task 'task 1'")
    add_task(ToDo_List=ToDo_List, caretaker=caretaker, director=director, task_title="task 1")
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List)[0].title)

    print("adding task 'task 2'")
    add_task(ToDo_List=ToDo_List, caretaker=caretaker, director=director, task_title="task 2")
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List)[0].title)
    print(get_tasks(ToDo_List=ToDo_List)[1].title)

    print("removing task 'task 3'")
    remove_task(ToDo_List=ToDo_List, caretaker=caretaker, task_title="task 3")
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List)[0].title)
    print(get_tasks(ToDo_List=ToDo_List)[1].title)