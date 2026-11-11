class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear =-1
        self.count = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        else:
            self.front = (self.front +1)% self.k
            self.count -= 1
            return True

    def Front(self) -> int:
        # return self.queue[(self.rear - self.count +1 + self.k) % self.k]
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        # return self.queue[(self.front + self.count - 1)% self.k]
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()