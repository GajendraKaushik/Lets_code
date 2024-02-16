class MyStack():
    stack =[]
    top = -1
    def isEmpty(self):
        if len(self.stack) == 0 :
            return True
        else:
            False
    
    def push(self, x):
        self.stack.append(x)
        self.top += 1 
            
    
    def pop(self):
        if self.isEmpty():
            return False
        else:
            temp = self.stack[self.top]
            print(self.top, temp, "check")
            self.top -= 1
            print(self.top, temp, "check")
            self.stack = self.stack[:self.top+1]
            return temp
    def get_top(self):
        print(self.top, "anshu")
        temp = self.stack[self.top]
        print(self.top, temp)
        return temp
    
obj = MyStack()
print(obj.isEmpty())
obj.push(12)
obj.push(13)
obj.push(14)
print(obj.stack)
print(obj.get_top())
print(obj.pop())
print(obj.pop())
print(obj.stack)