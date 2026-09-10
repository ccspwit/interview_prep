# -*- coding: utf-8 -*-
"""
Created on Fri May 5, 2017
LeetCode problem 155
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
@author: K Li
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack)==0:
            # stack is empty
            self.stack.append((x,x))
        else:
            curMin = self.getMin()
            if x<curMin:
                curMin = x
            self.stack.append((x,curMin))
        
    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            raise IndexError("Pop from empty stack")
        else:
            num = self.stack.pop()
            return num[0]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            N = len(self.stack)
            num = self.stack[N-1]
            return num[0]
        
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            N = len(self.stack)
            num = self.stack[N-1]
            return num[1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    a = MinStack()
    a.push(0)
    a.push(-2)
    a.push(-2)
    a.push(-3)
    print(a.getMin())
    a.pop()
    print(a.getMin())
    a.top()
    a.pop()
    a.pop()
    print(a.getMin())
    
    