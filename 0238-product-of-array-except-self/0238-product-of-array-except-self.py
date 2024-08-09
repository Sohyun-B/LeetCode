from typing import List
from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range (len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1 # 값 초기화
        # 오른쪽 곱셈
        for i in range(len(nums)-1, 0 -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out