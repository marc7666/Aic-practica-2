class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

    def top(self):
        return self.list[len(self.list) - 1]

    def size(self):
        return len(self.list)


