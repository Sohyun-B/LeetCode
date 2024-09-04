class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
        

    def pop(self):
        self.peek() # 스택 가장 위의 원소 반환. 삭제X
        return self.output.pop()
        

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self):
        return self.input == [] and self.output == []
