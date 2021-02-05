#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Array:
    def __init__(self):
        self.a=[0 for i in range(1)]
        #'n' is the no_of elements 
        self.n=0
        
    def length(self):
        counter=0
        for i in self.a:
            counter+=1
        return counter
            
    def add(self,i,x):
        if self.n==self.length():
            self.resize()
            
        #here we are making a new tmporary array  "b" 
        b=[0 for e in range(self.length())]
        
        #this loop will copy elements of "a" to 'b' to same index 
        for q in range(0,i):
            b[q]=self.a[q]
            
        #adding element 'x' at i'th index    
        b[i]=x
        
        #this loop will push elements of "a" to 'b' with one
        #index increament 
        for w in range(i,self.n):
            b[w+1]=self.a[w]
        self.a=b
        
        #increasing number of elements 'n'  by 1
        self.n+=1
        return self.a
    
    def remove(self,i):
        #here we are making a new tmporary array  "b"
        b=[0 for e in range(self.length())]
        
        #this loop will copy elements of "a" to 'b' to same index 
        for j in range(0,i):
            b[j]=self.a[j]
            
        #this loop will pull back elements of "a" to 'b' with one
        #index back to fill the empty space left by removing an element
        for k in range(i+1,self.n):
            b[k-1]=self.a[k]
        self.a=b
        
        #decreasing number of elements 'n'  by 1
        self.n-=1
        
        #here we are checking that if length of array is
        #equal to 3xn. if it is; then resize will be called!
        if self.length()>=3*self.n:
            self.resize()
        return self.a
    
    def resize(self):
        #here we are making a new tmporary array  "b" whose length will be
        #2 times total no of elements
        b=[0 for e in range(max(1,2*self.n))]
        
        #this loop will copy elements of "a" to 'b' to same index
        for i in range(self.n):
            b[i]=self.a[i]
        self.a=b
        return self.a
    
    def Print(self):
        return self.a
    
    def Sort(self):
        #it's basically a buble sort but with some changings. it will not run
        #on whole array because we don't want to sort the whole array (since empty
        #boxex contain zeros and it'll make sort fnction malfunctioned)
        #but we want only totals no of elements to be sorted. 
        for i in range(self.n-1):
            for j in range(self.n-1-i):
                if self.a[j] > self.a[j+1]:
                    t = self.a[j]
                    self.a[j] = self.a[j+1]
                    self.a[j+1] = t
        return self.a
    
    
    
o1=Array()
o1.add(0,0)
o1.add(1,1)
o1.add(2,2)
o1.add(3,3)
o1.add(4,4)
o1.add(5,5)
o1.add(6,7)
o1.add(7,8)
o1.add(8,6)
o1.remove(2)
o1.remove(2)
o1.remove(2)
o1.remove(2)
o1.Sort()

