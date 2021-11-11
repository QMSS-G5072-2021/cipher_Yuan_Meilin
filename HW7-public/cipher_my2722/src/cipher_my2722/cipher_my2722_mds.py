#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cipher(text, shift, encrypt=True):
    """
    One of the simplest and most widely known encryption techniques 
    
    Inputs
    ----------
    a word / words / text contains symbols / a sentence
    
    Outputs
    -------
    each letter in inputs is replaced by a letter some fixed number of positions down the alphabet
    
    Examples
    --------
    >>> example = 'hello'
    
    >>> encrypting = cipher(example, 1, True)
    >>> print(encrypting)
    ifmmp
    
    >>> decrypting = cipher(encrypting, 1, False)
    >>> print(decrypting)
    hello
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

