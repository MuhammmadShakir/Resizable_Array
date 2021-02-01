#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ctypes is a foreign function library for Python. It provides C compatible data types,
# and allows calling functions in DLLs or shared libraries.

import ctypes

class ResizableArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.array = self._CreateArray(self.capacity)
        
    def IsEmpty(self):
        if self.count == 0:
            return True
        else:
            return False
        
    def Length(self):
        return self.count
    
    def _CreateArray(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    
    def GetItem(self, index):
        if not 0 <= index < self.count:
            return "INVALID INDEX"
        return self.array[index]
    
    def _Resize(self, new_capacity):
        new_array = self._CreateArray(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def Append(self, element):
        if self.count == self.capacity:
            self._Resize(2*self.capacity) 
        self.array[self.count] = element
        self.count += 1
        
    def Pop(self):
        if self.IsEmpty == True:
            return "ARRAY IS EMPTY"
        self.array[self.count-1] = 0
        self.count -= 1
        
    def Insert(self, items, index):
        if index < 0 or index > self.count:
            return "INDEX OUT OF RANGE"
        if self.count == self.capacity:
            self._Resize(2*self.capacity)
        for i in range(self.count-1, index-1, -1): 
            self.array[i+1] = self.array[i] 
        self.array[index] = items 
        self.count += 1
        
    def Remove(self, index):
        if self.IsEmpty == True:
            return "ARRAY IS EMPTY"
        if index < 0 or index >= self.count:
            return "INDEX OUT OF RANGE"
        if index == self.count-1: 
            self.array[index] = 0
            self.count -= 1
        for i in range(index, self.count-1): 
            self.array[i] = self.array[i+1]             
        self.array[self.count-1] = 0
        self.count -= 1
        
    def Print(self):
         for i in range(self.count):
            print(self.array[i],end = " ")

