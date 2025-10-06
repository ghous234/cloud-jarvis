stack = []

# Push operation
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after push operations:", stack)

# Pop operation
pop_item = stack.pop()
print("Popped item:", pop_item)
print("Stack after pop operation:", stack)

# Peek operation
peek_item = stack[-1]
print("Peeked item:", peek_item)
print("Stack after peek operation:", stack)

# Check if stack is empty
is_empty = len(stack) == 0
print("Is stack empty?", is_empty)

# Size of the stack
stack_size = len(stack)
print("Size of the stack:", stack_size)

# Clear the stack
stack.clear()
print("Stack after clearing:", stack)