# Function to check if the brackets in a string are balanced
def is_balanced(s):
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their matching opening brackets
    mapping = {')': '(', ']': '[', '}': '{'}
    
    # Loop through each character in the input string
    for char in s:
        # If character is an opening bracket, push to stack
        if char in mapping.values():
            stack.append(char)  # Push opening bracket
        
        # If character is a closing bracket
        elif char in mapping:
            # Check if stack is empty or top of stack doesn't match
            if not stack or stack.pop() != mapping[char]:
                return False  # Mismatched or missing opening bracket
    
    # Return True if stack is empty (all brackets matched)
    return not stack  # Empty stack means balanced

# Test the function with an example
print(is_balanced("{[()]}"))  # True (brackets are balanced)
