
# coding: utf-8

# In[1]:


import numpy as np
from scipy.spatial.distance import pdist, squareform


# In[2]:


x = np.array([[0, 1], [1, 0], [2, 0]])


# In[3]:


print(x)


# In[4]:


d = squareform(pdist(x, 'euclidean'))


# In[5]:


print(d)

