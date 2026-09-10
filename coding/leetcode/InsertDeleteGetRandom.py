# -*- coding: utf-8 -*-
"""
Created on June 9, 2017
LeetCode problem 380, 381 combined
---#380
Design a data structure that supports all following operations in average
O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each
element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();
// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);
// Returns false as 2 does not exist in the set.
randomSet.remove(2);
// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);
// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();
// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);
// 2 was already in the set, so return false.
randomSet.insert(2);
// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();


---#381
Design a data structure that supports all following operations in average
O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The
probability of each element being returned is linearly related to the number
of same value the collection contains.

Example:
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();
// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);
// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);
// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);
// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();
// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);
// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
@author: K Li
"""

class RandomizedSet(object):
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        self.len = 0
        self.map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.store.append(val)
            self.map[val] = self.len
            self.len += 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        :type val: int
        :rtype: bool
        """
        
        ind = self.map.get(val,-1)
        if ind!=-1:
            if ind < self.len-1:
                self.store[ind] = self.store[-1]
                self.store.pop()
                self.map.pop(val)
                self.map[self.store[ind]] = ind
                self.len -= 1
            else:
                # remove the last element from the lsit
                self.map.pop(val)
                self.store.pop()
                self.len -= 1
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.len>0:
            # NOTE!!! for python 2.x need to use 
            # random.randint(0,self.len-1)
            ind = random.randint(0,self.len)
            return self.store[ind]
        else:
            raise ValueError("The storage is empty")

class RandomizedCollection(object):
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        self.len = 0
        self.map = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection
        did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.store.append(val)
            self.map[val] = [self.len]
            self.len += 1
            return True
        else:
            self.map[val].append(self.len)
            self.store.append(val)
            self.len += 1
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection
        contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            if self.len==1:
                # last element to remove
                self.len=0
                self.map = {}
                self.store=[]
            elif self.store[-1]==val:
                #remove the last element
                self.store.pop()
                self.map[val].pop()
                if not self.map[val]:
                    self.map.pop(val)
                self.len -= 1
            else:
                # swap last element with the element to be deleted
                # update map index, remove last element
                lastVal = self.store[-1]                
                ind1 = self.map[val].pop()
                self.store[ind1] = lastVal
                self.map[lastVal].remove(self.len-1)
                self.map[lastVal].append(ind1)
                #lastInd = self.map[lastVal]
                if not self.map[val]:
                    self.map.pop(val)
                self.store.pop()
                self.len -= 1
                
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if self.len>0:
            # NOTE!!! for python 2.x need to use 
            # random.randint(0,self.len-1)
            ind = random.randint(0,self.len)
            return self.store[ind]
        else:
            raise ValueError("The storage is empty")
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    a = RandomizedSet()
    print("Insert Delete GetRandom O(1)")
    for n in range(5):
        a.insert(n)
    print(a.len)
    a.getRandom()
    a.getRandom()
    a.remove(3)
    a.remove(1)
    print(a.store, a.map, a.len)
    a.getRandom()
    a.remove(1)
    a.remove(2)
    a.remove(4)
    a.getRandom()
    a.insert(1)
    a.remove(0)
    a.remove(1)

    a = RandomizedCollection()
    print("Insert Delete GetRandom O(1) II")
    for n in range(5):
        a.insert(n)
    a.insert(1)
    a.insert(3)
    a.insert(1)
    a.getRandom()
    a.getRandom()
    a.remove(3)
    a.remove(1)
    print(a.len, a.store)
    print(a.map)
    a.getRandom()
    a.remove(1)
    a.remove(2)
    a.remove(4)
    a.getRandom()
    a.insert(1)
    a.remove(0)
    a.remove(1)
