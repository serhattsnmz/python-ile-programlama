# Lambda Functions

- Lambda fonksiyonları, tanımlayacağımız fonksiyonların içeriği sadece `return` adımından oluşuyorsa, tek satırda tanımlamamızı sağlar. 

```
lambda <bound_variables> : <body>
```

```python
>>> def add(a, b):
...     return a + b

>>> add = lambda a, b : a + b

>>> add(2,3)
5

>>> test = lambda : "serhat"
>>> test()
'serhat'
```

- Basit olarak yazılabilecek kodları daha düzenli yazmamızı sağlar.

```python
...
print_red       = lambda message, end="\n" : cprint(message, "red",     end=end, attrs=['blink'])
print_green     = lambda message, end="\n" : cprint(message, "green",   end=end, attrs=['blink'])
print_magenta   = lambda message, end="\n" : cprint(message, "magenta", end=end, attrs=['blink'])
print_yellow    = lambda message, end="\n" : cprint(message, "yellow",  end=end, attrs=['blink'])
print_cyan      = lambda message, end="\n" : cprint(message, "cyan",    end=end, attrs=['blink'])

print_error     = lambda message, end="\n" : print_red("[x] " + message, end)
print_info      = lambda message, end="\n" : print_yellow("[i] " + message, end)
print_success   = lambda message, end="\n" : print_green("[\u2713] " + message, end)
print_dialog    = lambda message, end="\n" : print_yellow("[>] " + message, end)
...
```

- IIFE (Immediately Invoked Function Expression)
    - Hafızada saklanmadan, bir kere yazılıp hemen kullanılan fonksiyonları tanımlar. Özellikle JS dilinde çok kullanılır. (source : https://developer.mozilla.org/en-US/docs/Glossary/IIFE)

```python
>>> (lambda a, b: a + b)(2, 3)
5

>>> (lambda x: x * x)(3)
9

>>> sum(map(lambda i: i*i, range(1000 * 1000 * 100)))
333333328333333350000000
```

- Lambda fonksiyonları istenilirse iç içe de kullanılabilr.

```python
# Sayının karakökünü al, eğer negatif ise pozitif yapıp karakökünü al.

>>> p = lambda x : (lambda y : y if y >= 0 else -1 * y)(x) ** (1/2)

>>> p(4)
2.0

>>> p(-4)
2.0
```

```python
>>> high_ord_func = lambda x, func: x + func(x)

>>> high_ord_func(2, lambda x: x * x)
6
>>> high_ord_func(2, lambda x: x + 3)
7
```

- Lambda fonksiyonları decorator'lar ile kullanılabilir.

```python
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
print(add_two(3))

# Applying decorator to a lambda
print((trace(lambda x: x + 2))(3))

# [TRACE] func: add_two, args: (3,), kwargs: {}
# 5
# [TRACE] func: <lambda>, args: (3,), kwargs: {}
# 5
```

- Lamda fonksiyonları özellikle bazı build-in fonksiyonlar içinde geçici olarak kullanılır.

```python
	# --- map()

>>> list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
['Cat', 'Dog', 'Cow']

	# --- filter()
    
>>> list(filter(lambda x: x % 2 == 0, range(11)))
[0, 2, 4, 6, 8, 10]

	# --- sorted()
    
>>> words = ['banana', 'pie', 'Washington', 'book']
>>> sorted(words)
['Washington', 'banana', 'book', 'pie']
>>> sorted(words, key = lambda x: x.lower())
['banana', 'book', 'pie', 'Washington']

	# --- min() ve max()

>>> words = ['banana', 'pie', 'Washington', 'book']
>>> max(words)
'pie'
>>> max(words, key = lambda x: x.lower())
'Washington'
>>> min(words)
'Washington'
>>> min(words, key = lambda x: x.lower())
'banana'

	# --- reduce()
    
>>> import functools
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
>>> functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
6
```

## Performance

- Lambda fonksiyonlarının normal fonksiyon tanımlamaktan herhangi bir farkı yoktur.

```python
>>> import dis

	# normal functions

>>> def add(x, y): return x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function add at 0x7f30c6ce9f28>

	# lambda functions
    
>>> add = lambda x, y: x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function <lambda> at 0x7f30c6ce9ea0>
```

- Traceback çıktılarında normal fonksiyonlardan farklı olarak `<lambda>` geçer. 

```python
>>> def div_zero(x): return x / 0
>>> div_zero(2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in div_zero		# function name
ZeroDivisionError: division by zero
    
>>> div_zero = lambda x: x / 0
>>> div_zero(2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in <lambda>		# lambda
ZeroDivisionError: division by zero
```
