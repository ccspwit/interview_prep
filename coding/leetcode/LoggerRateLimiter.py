# -*- coding: utf-8 -*-
"""
Created on June 2nd, 2017
LeetCode problem 359
Design a logger system that receive stream of messages along with its
timestamps, each message should be printed if and only if it is not printed
in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if
the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.

Example:
Logger logger = new Logger();
// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 
// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;
// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;
// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;
// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;
// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

@author: K Li
"""

class Logger(object):

    def __init__(self, block_window = 10):
        """
        Initialize your data structure here.
        """
        self.history = {}
        self.window = block_window  #time window in seconds
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp,
        otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.history:
            self.history[message] = timestamp
            return True
        else:
            if (timestamp-self.history[message])>=self.window:
                self.history[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

if __name__ == '__main__':
    testVector = [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
    a = Logger()
    print("Logger rate limit to %ds",a.window)
    for test in testVector:
        print('%s print %s'
              %("" if a.shouldPrintMessage(test[0],test[1]) else "Not", test))