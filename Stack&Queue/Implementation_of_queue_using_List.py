from queue import Queue 

# class Queue():
#     def __init__(self) -> None:
#         self.arr = [0]*10
#         self.front = -1 
#         self.rear =  -1 
#         self.top = -1 

#     def isempty(self):
#         if self.front == self.rear:
#             return True 
#         else:
#             return False 
#     def push(self, n):
#         if self.top == len(self.arr):
#             return -1 
#         elif self.front == self.rear == -1 :
#             self.front=0 
#             self.rear = 0
#             self.top = 0 
#             self.arr[self.top] = n 
#         else:
#             self.rear += 1
#             self.arr[self.rear] = n

#     def pop_front(self):
#         if self.isempty():
#             return -1
#         else:
#             temp = self.arr[self.front] 
#             self.arr[self.front]= 0
#             self.front -= 1
#             return temp
# Q1 = Queue()
# Q2 = Queue()

class MyQueue():
    def __init__(self) -> None:
        self.Q = Queue()
    
    def push(self, n):
       l = self.Q.qsize()
       self.Q.put(n)
       for i in range(l):
           self.Q.put(self.Q.get()) 
    def pop(self):
        temp = self.Q.get()
        return temp

    def top(self):
        return self.Q.queue[0]
    def size(self):
        return self.Q.qsize()

obj = MyQueue()

obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())



    







            

        