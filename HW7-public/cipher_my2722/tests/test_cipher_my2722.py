#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from cipher_my2722 import cipher_my2722

def test_cipher():
    result=cipher(text ='hi',1,True)
    assert result == 'ij'

