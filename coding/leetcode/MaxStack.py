# -*- coding: utf-8 -*-
"""
Created on June 4, 2019
LeetCode problem 716
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
@author: K Li
"""
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def push(self, x: int) -> None:
        if self.store:
            max_val = max(self.store[-1][1], x)
            self.store.append((x, max_val))
        else:
            self.store.append((x, x))

    def pop(self) -> int:
        if self.store:
            return self.store.pop()[0]
        else:
            return None

    def top(self) -> int:
        if self.store:
            return self.store[-1][0]
        else:
            return None

    def peekMax(self) -> int:
        if self.store:
            return self.store[-1][1]
        else:
            return None

    def popMax(self) -> int:
        temp = []
        val, max_val = self.store.pop()
        while val < max_val:
            temp.append(val)
            val = self.pop()
        # re-push
        for val in temp[::-1]:
            self.push(val)
        return max_val

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()