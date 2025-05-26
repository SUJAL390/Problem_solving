#Given an integer array nums, 
# return true if any value appears 
# more than once in the array,
# otherwise return false.

#Brute Force solution

from typing import List
class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False

nums=[1,4,7,7]
sol=Solution()
print(sol.hasDuplicate(nums))



                    
        