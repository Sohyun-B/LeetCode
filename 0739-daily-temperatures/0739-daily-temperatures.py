class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans, stack = [0]*len(temperatures), [] #0으로 초기화
        for i, day in enumerate(temperatures):
            while stack and day > temperatures[stack[-1]]: #가장 마지막 날이 해당 날보다 따뜻하면
                last = stack.pop()
                ans[last] = i-last
            stack.append(i)
        return ans
        