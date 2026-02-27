class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str=str(x)
        total=len(x_str)
        for i in range(total//2):
            if (x_str[i])!=(x_str[total-1-i]):
                return False
        return True