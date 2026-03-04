class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Early exit: odd length strings can't be valid
        if len(s) % 2 != 0:
            return False
        
        stack = []  # Initialize empty stack
        mapping = {'(': ')', '{': '}', '[': ']'}  # Map opening to closing brackets
        
        for char in s:  # Iterate directly over characters (no index needed)
            if char in mapping:  # If opening bracket found
                stack.append(mapping[char])  # Push expected closing bracket
            else:  # If closing bracket found
                if not stack or stack[-1] != char:  # Check if stack empty or mismatch
                    return False  # Invalid string
                stack.pop()  # Remove matched closing bracket
        
        return not stack  # Valid if stack is empty