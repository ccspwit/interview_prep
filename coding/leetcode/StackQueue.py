# -*- coding: utf-8 -*-
"""
Created on Mon May 8, 2017
LeetCode problem 225, 232 combined
---#225
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push
to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may
simulate a queue by using a list or deque (double-ended queue), as long as
you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top
operations will be called on an empty stack).

---#232
mplement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push
to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may
simulate a stack by using a list or deque (double-ended queue), as long as
you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
@author: K Li
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sReverse = []
        self.sizeR = 0
        self.sReverseBottom = 0
        self.sInorder = []
        self.sizeIn = 0
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.sizeR == 0:
            self.sReverseBottom = x
        self.sReverse.append(x)
        self.sizeR += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.sizeIn == 0:
            n = self.sizeR
            if n==0:
                raise ValueError("FIFO empty.")
            while n>1:
                val = self.sReverse.pop()
                self.sInorder.append(val)
                n -= 1
                self.sizeR -= 1
                self.sizeIn += 1
            val = self.sReverse.pop()
            self.sizeR -= 1
            return val
        else:
            val = self.sInorder.pop()
            self.sizeIn -= 1
            return val

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.sizeIn!=0:
            return self.sInorder[-1]
        elif self.sizeR!=0:
            return self.sReverseBottom
        else:
            raise ValueError("FIFO empty")

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        if (self.sizeR==0) & (self.sizeIn==0):
            return True
        else:
            return False

    def size(self):
        return self.sizeR+self.sizeIn

class MyStack(object):
   
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qIn = MyQueue()
        self.qOut = MyQueue()
        return

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.qIn.push(x)
        return

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            raise ValueError("Can not pop. Stack is empty")
        n,m = self.qIn.size(), self.qOut.size()
        #print(n,m)
        while n>1:
            self.qOut.push(self.qIn.pop())
            n -= 1
        val = self.qIn.pop()
        self.qIn, self.qOut = self.qOut, self.qIn
        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            raise ValueError("Can not pop. Stack is empty")
        n = self.qIn.size()
        while n>0:
            val = self.qIn.pop()
            self.qOut.push(val)
            n -= 1
        self.qIn, self.qOut = self.qOut, self.qIn
        return val
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.qIn.empty() & self.qOut.empty():
            return True
        else:
            return False
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    #a = MyQueue()
    a = MyStack()
    print(a.empty())
    a.push(1)
    a.push(2)
    #print('peeking...',a.peek())
    print('poping...',a.pop())
    print(a.empty())
    a.push(3)
    print('poping...',a.pop())
    a.push(4)
    a.push(5)
    #print('peeking...',a.peek())
    print(a.empty())
    print('poping...',a.pop())
    print('poping...',a.pop())
    #print('peeking...',a.peek())
    #print('poping...',a.pop())
    
    