class ToDoList:
    def __init__(self):
        self._tasks = []

    #basic to do list functions

    def add_task(self, task):
        self._tasks.append(task)

    def remove_task(self, task):
        self._tasks.remove(task)

    def get_tasks(self):
        return self._tasks
    
    #memento functions

    def create_memento(self):
        return ToDoListMemento(list(self._tasks))
    
    def restore_memento(self, memento):
        self._tasks = memento.get_state()


#Memento class for ToDoList

class ToDoListMemento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state
    
#Caretaker to manage and restore mementos

class ToDoListCaretaker:
    def __init__(self):
        self._mementos = []
        self._current_index = -1

    def add_memento(self, memento):
        self._mementos.append(memento)
        self._current_index += 1

    def get_memento(self, index):
        return self._mementos[index]
    
    def get_current_memento(self):
        if 0 <= self._current_index < len(self._mementos):
            return self._mementos[self._current_index]
        else:
            return None
        
    def undo(self):
        if self._current_index > 0:
            self._current_index -= 1
            return self._current_index

    def redo(self):
        if 0 <= self._current_index < len(self._mementos) - 1:
            self._current_index += 1
            return self._current_index
