'''
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
'''
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dict = {}
        for val in nums:
            if val in dict:
                return True
            dict[val] = val   
        return False
    
if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,1]
    print(solution.containsDuplicate(nums))