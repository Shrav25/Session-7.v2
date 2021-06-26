# -*- coding: utf-8 -*-
"""session7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jIKikXW3sRnz-H41Ah93b2Zmu52gi8np
"""

def fibo():
  #Closure to generate next Fibonacci Number
  
  '''The first function will have two variables which takes the first two Fibonacci numbers starting from zero'''
  n1 = 0
  n2 = 1
  def fib():
    
    '''This function will generate next fibonacci number'''
    
    nonlocal n1, n2
    dump = n2
    n2 = n1 + n2
    n1 = dump
    return n2
  return fib

def doc_check(fn):
  #Closure to check for more than 50 characters in the Docstring
  '''The First function will take a free variable my_count which will give
  us the set count for the doc string'''

  my_count = 50

  def doc_check2():
    '''The second function will use the Free Variable my_count
    to check for the size of docstring in the function'''
    
    nonlocal my_count

    if len(fn.__doc__) >= my_count:
      return 'Doc String is enough for me to understand the function'
    else:
      return 'The guy Who wrote this Doc String is Lazy'
  return doc_check2

def add(a,b):

  '''Th function takes in two parameters
  and adds them both, the input parameters are integers'''

  return a+b

def mul(a,b):

  '''This function takes in two integers and multiplies them'''

  return a*b

def division(a,b):

  '''This function takes in two integers and divides them both'''

  if b == 0:
    raise ValueError('Cannot divide a number by zero')

  return a/b

def sub(a,b):

  '''This function will return the difference between the two inputs'''

  return a-b

def counter(fn):

  my_count = 0

  def counter2(*args, **kwargs):

    nonlocal my_count

    my_count += 1

    return my_count
  return counter2

fun_dict = {'add':0,'mul':0, 'division':0,'sub':0}

def global_dict(fn):

  '''This function will tell the number of times
  the function was called'''

  count = fun_dict[fn.__name__]

  def inner(a,b):

    '''This function takes in two positional arguments
    and applies any of the above called function'''

    nonlocal count

    print(fn(a,b))
    count += 1
    fun_dict[fn.__name__] = count
    return count
  return inner

def global_dict_2(fn, fun_dict:dict):
    """
        This function is used to calculate the number of times a function is being called and update the dictionary
        which is passed as a parameter.
        # params:
            fn: Function whose call will be counted
            mydict: Dictionary whose value we need to update
    """
    new_count = fun_dict[fn.__name__]
    def inner(a:int,b:int)->int:
        """
            This function updates the counter and returns it.
        """
        nonlocal new_count
        print(fn(a,b))
        new_count += 1
        fun_dict[fn.__name__] = new_count
        return new_count
    return inner

