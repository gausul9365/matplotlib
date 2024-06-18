#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
plt.plot([4,5,6], [5,3,6])
plt.show()


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
plt.plot([4,5,6], [5,3,6])
plt.title("KHurram's Data")
plt.show()


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
plt.plot([4,5,6], [5,3,6])
plt.title("KHurram's Data ")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# In[5]:


from matplotlib import pyplot as plt
x= [1,2,6]
y= [2,3,38]
x2= [5,4,6]
y2= [3,5,6]
plt.plot(x,y)
plt.plot(x2,y2)
plt.show()


# In[12]:


from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
x= [1,2,6]
y= [2,3,38]
x2= [5,4,6]
y2= [3,5,6]
plt.plot(x,y, linewidth=3, label="first")
plt.plot(x2,y2, label= "second")
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




