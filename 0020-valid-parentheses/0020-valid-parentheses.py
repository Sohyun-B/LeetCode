class Solution(object):
    def isValid(self, s):
        stack =[]
        for i in list(s):
            if i =="(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            else: # 닫는 괄호가 나오는 경우
                # 이미 스택이 존재하고 그 스택에 해당하는 괄호가 있어야한다
                if stack and stack.pop() == i:
                    continue
                # 없으면 False
                return False
        # 스택에 남아있는 경우: 
		# = 여는 괄호가 닫는 괄호보다 많은 경우
		# False 리턴
        if stack:
            return False
        return True