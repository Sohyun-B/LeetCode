from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 리스트를 정렬합니다.
        ans = []
        length = len(nums)
        
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 중복된 값을 피하기 위해
                continue
            
            left, right = i + 1, length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # 합이 0일 때 결과를 저장
                    ans.append([nums[i], nums[left], nums[right]])
                    # 중복된 값을 피하기 위해
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return ans