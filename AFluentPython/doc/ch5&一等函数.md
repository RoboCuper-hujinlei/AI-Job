### 第三部分 把函数视为对象

#### ch& 5 一等函数

- 认清一个概念，python中函数对象本身是function类的一个实例。拥有function类的实例和各种属性

```python
>>> def factorial(n):
    	'''returns n!'''
...     return 1 if n < 2 else n * factorial(n-1)		 # n的阶乘
... 
>>> factorial(5)
120
>>> factorial.__doc__		# function类中众多属性中的一个
returns n!
>>> type(factorial)
<class 'function'>
```

- 函数可以通过别的名称引用，可以作为参数传递

```python
>>> fact = factorial
>>> fact(5)
120
>>> fact.__doc__
'retundsda !'
>>> list(map(fact, range(11)))					# 函数式编程的特点是可以使用 高阶函数

[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

```

##### 函数式编程的特点是使用 高阶函数

接受函数作为参数，或者把函数作为结果返回的函数是**高阶函数**，例如map函数  







