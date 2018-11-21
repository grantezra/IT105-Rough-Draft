
# coding: utf-8

# In[11]:


import sympy #imports the Sympy library
from sympy.interactive import printing  #imports basicn functions that allow sympy to unteract with python
printing.init_printing(use_latex=True) #makes the output look pretty.
from sympy import Eq, solve_linear_system, Matrix #imports the equation and matrix functions
from sympy import * 
from sympy import Function, dsolve, Derivative # imports the function, dsolve, and dervative functions
import sympy as sp #renames the sympy libary for this function
import numpy as np #imports a linrary similar to sympy


# In[12]:


print("This calculator will provide you with prompt you to enter the a,b,c,and d values of a two by two matrix which was extracted from a system of differential equations. The calculator will provide a general solution to the system of diff eqs. It will also provide the eiganvalues and eiganvectors given that you are runnnig the proper software.")


# In[13]:


print("From your system of differental equations. Extract the 2x2 matrix.")


# In[22]:


a=float(input("input a value of a 2x2 matrix:")) #records the 4 parts of a 2x2 matrix
b=float(input("input b value of a 2x2 matrix:"))
c=float(input("input c value of a 2x2 matrix:"))
d=float(input("input d value of a 2x2 matrix:"))


# In[15]:


#establishes varibales as symbols
t,C1,C2 = symbols("t C1 C2")
x,y = symbols("x y", cls=Function, Function = True)


# In[17]:


M = Matrix([[a, b], [c, d]])
print("The eiganvalues are:") #prints the eigan system, but it is only readable in software such as jupyter. 
M.eigenvals()
print(M.eigenvals())


# In[18]:


print("The eiganvectors are:")
M.eigenvects()
print(M.eigenvects())


# In[23]:



eq1 = Eq(diff(x(t), t),a*x(t)+b*y(t))
eq2 = Eq(diff(y(t),t),c*x(t)+d*y(t))
soln = dsolve((eq1, eq2))  #provides a general solution to two differntal equations


# In[24]:

print("The general solutions in x and y components are:")
display(soln)


# In[10]:


print("Rememeber that the eiganvector associated with the solutin can be different as long as it has the same ratio. The solution produced may not be in a different form from the textbook or webassign. ")

