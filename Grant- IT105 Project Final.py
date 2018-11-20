

import sympy #imports the Sympy library
from sympy.interactive import printing  #imports basicn functions that allow sympy to unteract with python
printing.init_printing(use_latex=True) #makes the output look pretty.
from sympy import Eq, solve_linear_system, Matrix #imports the equation and matrix functions
from sympy import * 
from sympy import Function, dsolve, Derivative # imports the function, dsolve, and dervative functions
import sympy as sp #renames the sympy libary for this function


# In[ ]:


a=float(input("input a value of a 2x2 matrix")) 
b=float(input("input b value of a 2x2 matrix"))
c=float(input("input c value of a 2x2 matrix"))
d=float(input("input d value of a 2x2 matrix"))


# In[15]:


#establishes varibales as symbols
t,C1,C2 = symbols("t C1 C2")
x,y = symbols("x y", cls=Function, Function = True)


# In[27]:


M = Matrix([[a, b], [c, d]])  #Displays the eiganvalues and eiganvectors
print("The eiganvalues are:")
M.eigenvals()
print("The eiganvectors are:")
M.eigenvects()


# In[5]:


print(a)


# In[25]:



eq1 = Eq(diff(x(t), t),a*x(t)+b*y(t))
eq2 = Eq(diff(y(t),t),c*x(t)+d*y(t))
soln = dsolve((eq1, eq2))  #provides a gneral solution to two differntal equations


# In[26]:


display(soln)

