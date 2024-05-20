from queue import LifoQueue
class MyQueue:

    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()
        

    def push(self, x: int) -> None:
        self.s1.put(x)
        print(self.s1.queue)

    def pop(self) -> int:
        if not self.s2.empty():
            return self.s2.get()
        else:
            while not self.s1.empty():
                self.s2.put(self.s1.get())
            print(self.s2.queue)
            return self.s2.get()
        
    def peek(self) -> int:
        if not self.s2.empty():
            return self.s2.queue[-1]
        else:
            while not self.s1.empty():
                self.s2.put(self.s1.get())
            print(self.s2.queue)
            return self.s2.queue[-1]
        

    def empty(self) -> bool:
        if self.s1.empty() and self.s2.empty():
            return True
        else:
            return False  



    