import copy

class ToDoListItem:
    def __init__(self, title, due_date = None, tags = None, completed = False):
        self.title = title
        self.due_date = due_date
        self.tags = tags
        self.completed = completed

class ItemBuilder:
    def set_title(self, title):
        pass

    def set_due_date(self, due_date):
        pass

    def set_tags(self, tags):
        pass

    def set_completed(self, completed):
        pass

    def build(self):
        pass

class ToDoItemBuilder(ItemBuilder):
    def __init__(self):
        self.item = ToDoListItem("Unnamed Task", None, [], False)

    def set_title(self, title):
        self.item.title = title

    def set_due_date(self, due_date):
        self.item.due_date = due_date

    def set_tags(self, tags):
        self.item.tags = tags

    def set_completed(self, completed):
        self.item.completed = completed

    def build(self):
        return copy.deepcopy(self.item)
    
class ToDoListItemDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, title=None, due_date=None, tags=None, completed=None):
        if title:
            self.builder.set_title(title)

        if due_date:
            self.builder.set_due_date(due_date)

        if tags:
            self.builder.set_tags(tags)

        if completed:
            self.builder.set_completed(completed)

        return self.builder.build()