import ToDoList

def add_task(ToDo_List, caretaker, task):
    #adding task to list
    ToDo_List.add_task(task)

    #adding the memento in caretaker
    caretaker.add_memento(ToDo_List.create_memento())

def remove_task(ToDo_List, caretaker, task):
    #adding task to list
    ToDo_List.remove_task(task)

    #creating memento for that action
    memento = ToDo_List.create_memento()

    #adding the memento in caretaker
    caretaker.add_memento(memento)

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

    #test code to check if function work

    print("adding task 'task 1'")
    add_task(ToDo_List=ToDo_List, caretaker=caretaker, task="task 1")
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List))

    print("adding task 'task 2'")
    add_task(ToDo_List=ToDo_List, caretaker=caretaker, task="task 2")
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List))

    print("adding task 'task 3'")
    add_task(ToDo_List=ToDo_List, caretaker=caretaker, task="task 3")
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List))

    print("undo action: ")
    undo(ToDo_List=ToDo_List, caretaker=caretaker)
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List))

    print("redo action: ")
    redo(ToDo_List=ToDo_List, caretaker=caretaker)
    print("current to do list:")
    print(get_tasks(ToDo_List=ToDo_List))
