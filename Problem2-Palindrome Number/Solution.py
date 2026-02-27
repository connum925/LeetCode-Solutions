
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    # Negative numbers can't be palindromes (e.g., -121 != 121-)
    if x < 0:
        return False
    
    # Convert number to string to access individual digits
    x_str = str(x)
    
    # Initialize left pointer at start
    most_left_index = 0
    
    # Initialize right pointer at end
    most_right_index = (len(x_str)) - 1
    
    # Two-pointer approach: compare from both ends toward center
    while most_left_index < most_right_index:
        
        # If characters don't match, not a palindrome
        if x_str[most_left_index] != x_str[most_right_index]:
            return False
        
        # Move left pointer right
        most_left_index += 1
        
        # Move right pointer left
        most_right_index -= 1
    
    # All characters matched - it's a palindrome
    return True

print(isPalindrome(1221))