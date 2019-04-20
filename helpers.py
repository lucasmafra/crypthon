#!/usr/bin/env python
# coding: utf-8

# In[6]:


def extended_greatest_common_divisor(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

print(extended_greatest_common_divisor(10,15))


# In[7]:


def modular_inverse(a, b):
    """return x such x*a mod b = 1"""
    gcd, x, _ = extended_greatest_common_divisor(a, b)
    return x % b

print(modular_inverse(5, 72))


# In[8]:


def least_common_multiple(x, y):
   gcd, _, _ = extended_greatest_common_divisor(x,y)
   lcm = (x*y)//gcd
   return lcm

print(least_common_multiple(10, 15))


# In[10]:


def square_and_multiply(x, k, p=None):
    """
    Square and Multiply Algorithm
    Parameters: positive integer x and integer exponent k,
                optional modulus p
    Returns: x**k or x**k mod p when p is given
    """
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r**2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r

print(square_and_multiply(2, 3))

