from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = eval('*'.join([str(n) for n in nums]))
        return [sum//n for n in nums]