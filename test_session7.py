# -*- coding: utf-8 -*-
"""test_session7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ldF3nhZ8In0-HONIKvDKL_26w0MQ7gY5
"""

import os,inspect,re,random
import session7 as s7
import pytest

README_CONTENT_CHECK_FOR = [
    'fib',
    'my_count',
    'doc_check',
    'fibo',
    'closure',
    'global',
    'count',
    'dictioanry',
    'variable'
]
def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(s7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 25, 'You are not writing proper heading'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_doc_check():
    # more than 50
    f1 = s7.doc_check(s7.fibo)
    assert f1() == True,'just do a character by character count..it is easy'

    # zero
    f1 = s7.doc_check(test_readme_exists)
    assert f1() == False,'Please update me in the Readme'

    #less than 50
    f1 = s7.doc_check(test_function_name_had_cap_letter)
    assert f1() == False,'There are less than 50 characters'

def test_fibo():
    mylist = [1,2,3,5,8,13]
    f1 = s7.fibo()
    for i in mylist:
        assert i ==f1(),'Please generate the Right Fibonacci List'

def test_counter():
    f1 = s7.counter(s7.add)
    for i in range(1,11):
        assert f1(random.randint(1,100),random.randint(1,100)) == i ," Count it Properly.... Will you !!"

def test_division():
    for _ in range(10):
        number1 = random.randint(-100,100)
        number2 = random.randint(1,100)
        assert(s7.division(number1,number2)==number1/number2),'Get your division proper' 
        number2 = random.randint(-100,-1)
        assert(s7.division(number1,number2)==number1/number2),'Get your division proper' 
    
def test_div_for_error():
    number1 = random.randint(-100,100)
    number2 = 0
    with pytest.raises(ValueError, match=r".* divide .*"):
        s7.division(number1,number2),"Something is wrong, please check"

def test_add():
    for _ in range(10):
        number1 = random.randint(-100,100)
        number2 = random.randint(-100,100)
        assert(s7.add(number1,number2)==number1+number2),'Check your addition Skills' 


def test_mul():
    for _ in range(10):
        number1 = random.randint(-100,100)
        number2 = random.randint(-100,100)
        assert(s7.mul(number1,number2)==number1*number2),'Check your multiplication skills' 

def test_sub():
    for _ in range(10):
        number1 = random.randint(-100,100)
        number2 = random.randint(-100,100)
        assert(s7.sub(number1,number2)==number1-number2),'Go back to Primary School!' 

def test_check_annot():

    assert bool(s7.add.__annotations__)==True,"Annotations missing"
    assert bool(s7.sub.__annotations__)==True,"Annotations missing"
    assert bool(s7.mul.__annotations__)==True,"Annotations missing"
    assert bool(s7.division.__annotations__)==True,"Annotations missing"
    assert bool(s7.global_dict_2.__annotations__)==True,"Annotations missing"

def test_check_docs():

    assert bool(s7.doc_check.__doc__)==False,"Docstring missing"
    assert bool(s7.fibo.__doc__)==False,"Docstring missing"
    assert bool(s7.add.__doc__)==False,"Docstring missing"
    assert bool(s7.sub.__doc__)==False,"Docstring missing"
    assert bool(s7.mul.__doc__)==False,"Docstring missing"
    assert bool(s7.division.__doc__)==False,"Docstring missing"
    assert bool(s7.counter.__doc__)==False,"Docstring missing"
    assert bool(s7.global_dict.__doc__)==False,"Docstring missing"
    assert bool(s7.global_dict_2.__doc__)==False,"Docstring missing"

def test_check_closure():
    f1 = s7.doc_check(s7.fibo)
    assert bool(f1.__closure__ ) ==True, "Please check if this is a closure or not....!!!"
    f1 = s7.fibo()
    assert bool(f1.__closure__ ) ==True, "Please check if this is a closure or not....!!!"
    f1 = s7.counter(s7.add)
    assert bool(f1.__closure__ ) ==True, "Please check if this is a closure or not....!!!"
    fn = s7.add
    f1 = s7.global_dict(fn)
    assert bool(f1.__closure__ ) ==True, "Please check if this is a closure or not....!!!"
    mypersonaldict= {'add':0,'mul':0,'division':0,'sub':0}
    fn = s7.add
    f1 = s7.global_dict_2(fn,mypersonaldict)
    assert bool(f1.__closure__ ) ==True, "Please check if this is a closure or not....!!!"