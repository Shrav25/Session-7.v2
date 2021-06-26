<h1 align="center">Closures</h1>

<h2 align="center"> Assignment Question </h2>

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable
2. Write a closure that gives you the next Fibonacci number
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries

No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 

<h2 align="center"> Assignment Solution </h2>


### Assignment 1

#### **Assignment 1**
In the first assignment, using the function 'doc_check' we need to write a closure that will check if the doc string within the function passed has enough characters, here its set to 50 chracters. So we need to write a function which takes in another function as input and check if that function has DocString with more than 50 characters.


#### **Assignment 2**

In the second assignment we need a function to calculate the next 	onacci number, here we define `n1` and `n2` number as free variables i.e. will be used by `fib` closure and that closure will add these numbers and then will update the value of these numbers and then will return the added result

#### **Assignment 3**

In the third assignment we need to calculate how many times a function is being called, so to do that we define a `counter` function with `my_count` as free variable. Then we defined `counter2` function which updates the `my_count` value and returns it. Here we also add few extra functions such as addition, multiplication, subtraction and division and see if how many times they have been called.

#### **Assignment 4**

This Assignment is slight addition to the previous Assignment, here we define 4 functions i.e. `add`, `mul`, `sub`, and `division`. in this Assignment we keep a global dictionary `fun_dict` to have a check on how many times each operation is being called. so here we define a function `global_dict` which takes in function as a parameter, the    free variable `count` is the value obtained from the key of the global dictioanry as function name. Here we define a closure called inner which takes in  `a` and `b` as parameters, which are the numbers over which each operation will be perfomed. The function updated the global dictionary and returns the count

#### **Assignment 5**

This Assignment is and upgraded version of Assignment 4, The only difference is that instead of updating in global variable we pass a dictionay as a parameter and that gets updated. 

### Test Cases

There are test case for to check the working of each Assignment function. There are some general test cases of checking documentation of the project and the python files,There are testcases to check to whether they are acutally closures or not.

---