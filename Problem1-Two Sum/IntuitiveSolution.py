class Solution(object):
    def twoSum(self, nums, target):
        """
        Two Sum solution with O(n) time complexity and O(n) space complexity
        Uses a hash map to find two numbers that sum to the target
        """
        # Initialize empty dictionary - O(1)
        Dictionary = {}
        
        # Iterate over all elements in the array - O(n)
        for i in range(len(nums)):        
            # Check if current number exists in dictionary - O(1)
            if nums[i] in Dictionary:
                # Return stored index and current index - O(1)
                return [Dictionary[nums[i]], i]
            else:
                # Calculate the required complement - O(1)
                complement = target - nums[i]
                # Insert complement as key and current index as value - O(1)
                Dictionary[complement] = i
        
        # If no solution found, returns None implicitly
        
def main():
    # Create solution instance
    sol = Solution()
    
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(nums, target)
    print(result)  # Output: [0, 1]
    
if __name__ == '__main__':  
    main()

"""
Example of Local test:
def main(target,nums,Dictionary):
    for i in range(len(nums)):   
        if nums[i] in Dictionary:
            return [Dictionary[nums[i]],i]
        else:
            complement=target-nums[i]
            Dictionary[complement]=i  
    
if __name__ == '__main__':  
    target=9
    nums=[2,7,11,15]
    Dictionary = {}
    print(main(target,nums,Dictionary))
"""