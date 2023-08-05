# Problem: https://leetcode.com/problems/min-stack/

"""
I used a list to implement the stack instead of a linked list node because implementing getMin() is quite hard.
If you traverse the entire stack each time getMin() is called, it will take too much time.
My plan was to traverse the entire stack the first time, find the min and set a counter node to be the top item.
Then after subsequent pop() and push() if any, traverse the stack starting from the counter node, find the new min and set counter node again.
However, what happens if you pop() off the min? You will always need to check if the min exists in the stack, and to do that, you have to traverse again? Or traverse everything in stack to find new min?
"""

# My solution
class List_MinStack:
    def __init__(self, limit=1000):
        self.stack = []
        self.limit = limit

    def pop(self):
        if self.is_empty():
            print("Stack empty, cannot pop")
        else:
            return self.stack.pop()

    def push(self, value):
        if self.has_space():
            self.stack.append(value)
        else:
            print("Stack full, cannot push")

    def top(self):
        if self.is_empty():
            return "Stack empty, no value to display"
        else:
            return self.stack[-1]

    def getMin(self):
        if self.is_empty():
            return "Stack empty, no value to display"
        else:
            return min(self.stack)

    # Helper functions
    def has_space(self):
        return self.limit > len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


"""
# Failed linked list node implementation of stack
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class LL_MinStack:
    def __init__(self):
        self.top_item = None
        self.size = 0
        self.min = float('inf')         # Assign max int to min
        self.counter_node = Node(None)

    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
        self.size += 1

    def pop(self):
        if self.is_empty() == True:
            print("Stack empty, cannot pop")
        else:
            self.top_item = self.top_item.get_next_node()
            self.size -= 1

    def top(self):
        return self.top_item.get_value()

    def getMin(self):
            if self.is_empty() == True:
                print("Stack empty, cannot get min value")
            else:
                value = self.top_item.get_value()
                if value <= self.min:
                    self.min = value

                other_node = self.top_item.get_next_node()

                while self.other_node.get_value() != self.counter_node.get_value():
                    if other_node:
                        value = other_node.get_value()
                        if value <= self.min:
                            self.min = value

                        other_node = other_node.get_next_node()

                self.counter_node = self.other_node

        else:
            self.traversal_size = self.size - self.traversal_size

            value = self.top_item.get_value()
            if value <= self.min:
                self.min = value

            other_node = self.top_item.get_next_node()

            self.counter += 1

            while self.counter < self.traversal_size:
                if other_node:
                    value = other_node.get_value()
                    if value <= self.min:
                        self.min = value

                    other_node = other_node.get_next_node()

                self.counter += 1

        return self.min

    # Helper function
    def is_empty(self):
        return self.size == 0
"""


# Driver
s = List_MinStack()
s.push(-2)
s.push(0)
s.push(-3)
s.getMin()          # return -3
s.pop()
s.top()             # return 0
s.getMin()          # return -2
