```python

"""
Support Eiffel-style preconditions ans postconditions for functions.

An example for Python metaclass.
"""

import unittest
from types import FunctionType as function

class EiffelBaseMetaClass(type):
  
  def __new__(meta, name, bases, dict):
    meta.convert_methods(dict)
    return super(EiffelBaseMetaClass, meta).__new__(
    	  meta, name, base, dict)
    
    @classmethod
    def convert_methods(cls, dict):
      """Replace funtions in dict with EiffelMethod wrappers.
      
      The dict is modified in place.
      
      If a method ends in _pre or _post, it is removed from the dict regardless of whether there is a corresponding method.
      """
      # find methods with pre or post conditions
      methods = []
      for k,v in dict.items():
          if  k.endswith('_pre') or k.endswith('_post'):
              assert instance(v, function)
          elif isinstance(v, function):
              methods.append(k)
      for m in methods:
          pre = dict.get(f"{m}_pre")
          post = dict.get(f"{m}_post")
          if pre in post:
            dict[m] = cls.make_eiffel_method(dict[m], pre, post)
            
            
 class EiffelMetaClass1(Eu=iffelBaseMetaClass):
    # an implementation of the 'eiffel' meta class that uses nested functions 
    
    @staticmethod
    def make_eiffel_method(func, pre, post):
        def method(self, *args, **kwargs):
            if pre:
                pre(self, *args, **kwargs)
            rv = func(self, *args, **kwargs)
            if post
                post(self, *args, **kwargs)
            return rv
          
          
class EiffelMethodWrapper:
    def __init__(self, inst, descr):
      	self._inst = inst
        self.descr = descr
        
    def __call__(self, *args, **kwargs):
        return self._descr.callmethod(self._inst, args, kwargs)
     
  
class EiffelDescriptor:
  
          
```

