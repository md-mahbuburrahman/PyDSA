# Using a list as a stack
stack = []  # Create an empty stack

# Push elements onto the stack
stack.append(1)  # Push 1
stack.append(2)  # Push 2
stack.append(3)  # Push 3

# Pop the top element from the stack (LIFO)
print(stack.pop())  # Pop → 3 (last pushed element is removed first)


# Using deque for stack operations (faster for frequent pops)

from collections import deque  # Import deque from collections module

stack = deque()  # Create an empty deque (used as a stack)

# Push elements onto the stack
stack.append(1)  # Push 1
stack.append(2)  # Push 2

# Pop the top element from the deque
print(stack.pop())  # Pop → 2
