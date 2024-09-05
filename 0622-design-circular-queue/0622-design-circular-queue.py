class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p2] is None:
            self.q[self.p2] = value #rear이 가르키는 자리에 value삽입
            self.p2 = (self.p2 +1) % self.maxlen # 다음 자리로 p2포인터 이동. 길이가 넘어가면 나머지 연산자를 이용하여 한바퀴 돌아서 자리찾기
            return True
        else:
            return False
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p1] is None:
            return False #이미 내보낼것이 없는 상태 ->False
        else:
            self.q[self.p1] = None #삭제
            self.p1 = (self.p1+1) % self.maxlen
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        """
        # p1이 가르키는 맨앞의 요소를 반환
        return -1 if self.q[self.p1] is None else self.q[self.p1]
        

    def Rear(self):
        """
        Get the last item from the queue.
        """
        # 맨 뒤의 요소를 반환 (p2는 이미 뒤에 삽입될 자리를 가르키고 있기 때문에 p2-1이 맨 뒤의 요소를 가르키고 있습니다.)
        return -1 if self.q[self.p2 -1] is None else self.q[self.p2 -1] 
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        # p1,p2가 가르키는 자리가 같고, 그 안의 요소가 존재하지 않는다면 큐는 비어있습니다.
        return self.p1 == self.p2 and self.q[self.p1] is None
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        # p1,p2가 가르키는 자리가 같고, 그 안의 요소가 존재하면 공간이 다 찬것입니다.
        return self.p1 == self.p2 and self.q[self.p1] is not None