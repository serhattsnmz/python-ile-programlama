# Python'da Fonksiyon Oluşturma

- Fonksiyon nedir?
- Built-in fonksiyonlar

```python
>>> s = 'foobar'
>>> id(s)
56313440

>>> a = ['foo', 'bar', 'baz', 'qux']
>>> len(a)
4
```

- Neden fonksiyon yazarız?
    - DRY prensibi
    - Abstraction and Reusability (Soyutlama ve yeniden kullanılabilirlik)
    - Clean code
    - Modularity

```python
# Main program

# Code to read file in
<statement>
<statement>

# Code to process file
<statement>
<statement>

# Code to write file out
<statement>
<statement>
```

```python
def read_file():
    # Code to read file in
    <statement>
    <statement>

def process_file():
    # Code to process file
    <statement>
    <statement>

def write_file():
    # Code to write file out
    <statement>
    <statement>

# Main program
read_file()
process_file()
write_file()
```

## Fonksiyon Tanımlama ve Kullanma

```python
def <function_name>([<parameters>]):
    <statement(s)>
    [return <result>]
    
foo = <function_name>([<parameters>])
```

```python
def f():
    s = '-- Inside f()'
    print(s)

print('Before calling f()')
f()
print('After calling f()')

# Before calling f()
# -- Inside f()
# After calling f()
```

- Taslak olarak boş bir fonksiyon tanımlamak için `pass` keyword'ü kullanılabilir.

```python
>>> def f():
...     pass
```

## Fonksiyon Türleri

- Parametre alan ve almayan fonksiyonlar
- Return değeri bulunduran ve bulundurmayan fonksiyonlar

## Parametre Kullanımı ve Özellikleri

- Arguments (Parametre) nedir?

> The terms *parameter* and *argument* can be used for the same thing: information that are passed into a function.
>
> From a function's perspective:
>
> - A parameter is the variable listed inside the parentheses in the function definition.
> - An argument is the value that is sent to the function when it is called.

### a. Positional Arguments (Required Arguments)

- Fonksiyonun istediği argümanları sırasıyla ve tam olarak vermek

```python
	# Definition

>>> def f(qty, item, price):
...     print(f'{qty} {item} cost ${price:.2f}')

	# Usage

>>> f(6, 'bananas', 1.74)
6 bananas cost $1.74

	# Too few arguments

>>> f(6, 'bananas')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    f(6, 'bananas')
TypeError: f() missing 1 required positional argument: 'price'
        
	# Too many arguments

>>> f(6, 'bananas', 1.74, 'kumquats')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    f(6, 'bananas', 1.74, 'kumquats')
TypeError: f() takes 3 positional arguments but 4 were given
```

### b. Keyword Arguments

- Fonksiyonun istediği argümanları keyword ile vermek. 

```python
	# Definition

>>> def f(qty, item, price):
...     print(f'{qty} {item} cost ${price:.2f}')

	# Usage

>>> f(qty=6, item='bananas', price=1.74)
6 bananas cost $1.74

>>> f(item='bananas', price=1.74, qty=6)
6 bananas cost $1.74

	# Unknown keyword
    
>>> f(qty=6, item='bananas', cost=1.74)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() got an unexpected keyword argument 'cost'
    
	# Too few arguments
    
>>> f(qty=6, item='bananas')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f(qty=6, item='bananas')
TypeError: f() missing 1 required positional argument: 'price'
```

- Positional ve keyword argümanları birlikte kullanılabilirler. Bununla birlikte keyword argümanları her zaman en son yazılmalıdır, aksi halde `SyntaxError` hatası alınır.

```python
>>> f(6, price=1.74, item='bananas')
6 bananas cost $1.74

>>> f(6, 'bananas', price=1.74)
6 bananas cost $1.74

>>> f(6, item='bananas', 1.74)
SyntaxError: positional argument follows keyword argument
```

### c. Default (Optional) Parameters

- Fonksiyon tanımlanırken bir ya da bir kaç parametre için default value atanabilir. Fonksiyon kullanılırken bu parametrelere argüman atanabilir, atanmazsa default verilen değerler dikkate alınır.
- İstenilirse default parametrelerden sadece bir veya bir kaçına da keyword argümanı olarak değer atanabilir.

```python
>>> def f(qty=6, item='bananas', price=1.74):
...     print(f'{qty} {item} cost ${price:.2f}')

>>> f(4, 'apples', 2.24)
4 apples cost $2.24
>>> f(4, 'apples')
4 apples cost $1.74
>>> f(4)
4 bananas cost $1.74
>>> f()
6 bananas cost $1.74

>>> f(item='kumquats', qty=9)
9 kumquats cost $1.74
>>> f(price=2.29)
6 bananas cost $2.29
```

### d. Mutable Default Parameter Values

- Fonksiyon parametrelerinde default value olarak mutable bir değer verildiğinde dikkatli olunması gerekir.
- Pythonda default fonksiyon parameterleri, fonksiyon tanımlanırken "sadece bir kere" oluşur, her fonksiyon çağrıldığında tekrar tekrar oluşmaz. Fonksiyon içinde bu default value üzerinde yapılan işlemler saklı kalır ve sonrasında tekrar fonksiyon bu default değeri kullanırsa, hafızadan son halini çekip işlem yapar.

```python
>>> def f(my_list=[]):
...     my_list.append('###')
...     return my_list

>>> f(['foo', 'bar', 'baz'])
['foo', 'bar', 'baz', '###']

>>> f([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5, '###']

>>> f()
['###']
>>> f()
['###', '###']
>>> f()
['###', '###', '###']
```

```python
>>> def f(my_list=[]):
...     print(id(my_list))
...     my_list.append('###')
...     return my_list

>>> f()
140095566958408
['###']        
>>> f()
140095566958408
['###', '###']
>>> f()
140095566958408
['###', '###', '###']
```

- Fonksiyonlarda default value olarak mutable değerler kullanılmaması en doğrusudur. Eğer kullanılması zorunluysa, best practice olarak, default değer olarak `None` alınıp default değer fonksiyon içinde oluşturulur.

```python
>>> def f(my_list=None):
...     if my_list is None:
...         my_list = []
...     my_list.append('###')
...     return my_list


>>> f()
['###']
>>> f()
['###']
>>> f()
['###']

>>> f(['foo', 'bar', 'baz'])
['foo', 'bar', 'baz', '###']

>>> f([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5, '###']
```

### e. Mutable Arguments

- Python'da argüman olarak mutable objeler verilirse ve fonksiyon içinde bu objeler içinde değişiklikler yapılırsa, argüman olarak verilen değişken de bu durumdan etkilenir. Mutable objelere yeni atamalar yapıldığında bu durum geçerli değildir. (Ayrıntılı bilgi için bkz: In-Deph : Function Pass-By-Assigment notu)

```python
def f1(l):
    print(id(l))
    l.append('###')
    print(id(l))
    return l

def f2(s):
    print(id(s))
    s += "#"
    print(id(s))
    return s

def f3(l):
    print(id(l))
    l = []
    print(id(l))
    return l

a = ["foo"]
f1(a)
print(a)
print(id(a), end="\n\n")

b = "foo"
f2(b)
print(b)
print(id(b), end="\n\n")

c = ["foo"]
f3(c)
print(c)
print(id(c), end="\n\n")

# 66329896
# 66329896
# ['foo', '###']
# 66329896

# 66459744
# 66525344
# foo
# 66459744

# 66490200
# 66490240
# ['foo']
# 66490200
```

## Return Kullanımı ve Özellikleri

- Fonksiyonlarda `return` iki amaç için kullanılır.
    1. Çalıştığı anda fonksiyonu durdurma ve çıkış yapma
    2. Fonksiyondan dışarıya veri döndürme

```python
# Using return for terminating function
>>> def f(x):
...     if x < 0:
...         return
...     if x > 100:
...         return
...     print(x)

>>> f(-3)
>>> f(105)
>>> f(64)
64
```

```python
# Error checking with return
def f():
    if error_cond1:
        return
    if error_cond2:
        return
    if error_cond3:
        return

    <normal processing>
```

```python
# Return value to caller
>>> def f():
...     return 'foo'

>>> s = f()
>>> s
'foo'
```

- Herhangi bir değer verilmeden `return` kullanılırsa veya hiç kullanılmazsa `None` döner.

```python
>>> def f():
...     return

>>> print(f())
None

>>> def f():
...     x = 10

>>> print(f())
None
```

## Argument Packing & Unpacking

### a. Argument Tuple Packing

- Fonksiyona sayısı önceden bilinmeyen kadar argüman almaya yarar. Tuple tipindedir.
    - `*` ile belirtilir.
    - Genelde `args` ismi kullanılır ama herhangi bir isim kullanılabilir.

```python
>>> def f(*args):
...     print(args)
...     print(type(args), len(args))
...     for x in args:
...             print(x)
...

>>> f(1, 2, 3)
(1, 2, 3)        
<class 'tuple'> 3
1
2
3

>>> f('foo', 'bar', 'baz', 'qux', 'quux')
('foo', 'bar', 'baz', 'qux', 'quux')
<class 'tuple'> 5
foo
bar
baz
qux
quux
```

```python
>>> def avg(a, b, c):
...     return (a + b + c) / 3

>>> avg(1, 2, 3)
2.0

>>> avg(1, 2, 3, 4)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    avg(1, 2, 3, 4)
TypeError: avg() takes 3 positional arguments but 4 were given

	# Argument tuple packing 
    
>>> def avg(*args):
...     return sum(args) / len(args)

>>> avg(1, 2, 3)
2.0

>>> avg(1, 2, 3, 4, 5)
3.0
```

### b. Argument Tuple Unpacking

- Herhangi bir koleksiyon tipindeki değişkenin elemanları tek tek fonksiyona argüman olarak vermeye yarar.

```python
>>> def f(x, y, z):
...     print(f'x = {x}')
...     print(f'y = {y}')
...     print(f'z = {z}')
...

>>> f(1, 2, 3)
x = 1
y = 2
z = 3

>>> t = ('foo', 'bar', 'baz')
>>> f(*t)
x = foo
y = bar
z = baz

>>> a = ['foo', 'bar', 'baz']
>>> f(*a)
x = foo
y = bar
z = baz

>>> s = {1, 2, 3}
>>> f(*s)
x = 1
y = 2
z = 3

>>> d = { "a": 1, "b":2, "c":3 }
>>> f(*s)
x = a
y = b
z = c
```

- Packing ve Unpacking işlemleri birlikte de kullanılabilir.

```python
>>> def f(*args):
...     print(type(args), args)

>>> a = ['foo', 'bar', 'baz', 'qux']
>>> f(*a)
<class 'tuple'> ('foo', 'bar', 'baz', 'qux')
```

### c. Argument Dictionary Packing

- Argument tuple packing yapısına benzerdir, sayısı önceden bilinmeyen argümanları almaya yarar. Farklı olarak argümanları `Key-Value Pair` yapısında alır ve `dict` yapısında bir değişken oluşturur.
    - `**` ile belirtilir.
    - Genelde `kwargs` (keyword args) ismiyle belirtilir ama herhangi bir isim kullanılabilir.

```python
>>> def f(**kwargs):
...     print(kwargs)
...     print(type(kwargs))
...     for key, val in kwargs.items():
...             print(key, '->', val)
...

>>> f(foo=1, bar=2, baz=3)
{'foo': 1, 'bar': 2, 'baz': 3}
<class 'dict'>
foo -> 1
bar -> 2
baz -> 3
```

### d. Argument Dictionary Unpacking

- `dict` tipindeki değişkenin elamanlarını, fonksiyona keyword argümanları olarak vermeyi sağlar.

```python
>>> def f(a, b, c):
...     print(F'a = {a}')
...     print(F'b = {b}')
...     print(F'c = {c}')

>>> d = {'a': 'foo', 'b': 25, 'c': 'qux'}
>>> f(**d)
a = foo
b = 25
c = qux
```

### e. Argument Tuple Packing ve Dictionary Packing İşlemlerinin Birlikte Kullanılması

- Python kütüphaneleri oluşturulurken, fonksiyon tanımlamalarında çoğu yerde bu iki yapı birlikte kullanılır.
- Dezavantaj olarak, Python dilinde bu yapıların çokça kullanılıyor olması, fonksiyon kullanırken signature açıklamalarının yetersiz kalmasına neden olur. 

```python
>>> def f(a, b, *args, **kwargs):
...     print(F'a = {a}')
...     print(F'b = {b}')
...     print(F'args = {args}')
...     print(F'kwargs = {kwargs}')
...

>>> f(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)
a = 1
b = 2
args = ('foo', 'bar', 'baz', 'qux')
kwargs = {'x': 100, 'y': 200, 'z': 300}
```

### f. Multiple Unpacking

```python
>>> def f(*args):
...     for i in args:
...         print(i)

>>> a = [1, 2, 3]
>>> t = (4, 5, 6)

>>> f(*a, *t)
1
2
3
4
5
6
```

```python
>>> def f(**kwargs):
...     for k, v in kwargs.items():
...         print(k, '->', v)
...

>>> d1 = {'a': 1, 'b': 2}
>>> d2 = {'x': 3, 'y': 4}

>>> f(**d1, **d2)
a -> 1
b -> 2
x -> 3
y -> 4
```

## Keyword-Only Arguments

- Sadece keyword değeriyle almak istediğimiz parametreleri belirttiğimiz yöntemdir.
- Keyword değeri `*args` ifadesinden sonra yazılır ve istenilirse default bir değer atanır.

```python
	# Optional Keyword-Only Argument

>>> def concat(*args, prefix='-> ', sep='.'):
...     print(f'{prefix}{sep.join(args)}')

>>> concat('a', 'b', 'c')
-> a.b.c
>>> concat('a', 'b', 'c', prefix='//')
//a.b.c
>>> concat('a', 'b', 'c', prefix='//', sep='-')
//a-b-c

	# Required Keyword-Only Argument

>>> def concat(*args, prefix):
...     print(f'{prefix}{".".join(args)}')

>>> concat('a', 'b', 'c', prefix='... ')
... a.b.c

>>> concat('a', 'b', 'c')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: concat() missing 1 required keyword-only argument: 'prefix'
```

## Bare Variable Argument Parameter

- Belirtildiği yerden sonra, artık herhangi bir positional argument gelmeyeceğini belirtir. Sonrasında yazılan Keyword-Only Arguments elamanlarının positional olarak alınmamasını sadece keyword olarak alınmasını sağlar.
- Sadece `*` kullanılarak belirtilir.

```python
>>> def f(x, y, z="foo"):
...     print(x, y, z)

>>> f(1,2)
1 2 foo
>>> f(1,2,3)
1 2 3
>>> f(1,2, z = 3)
1 2 3

>>> def f(x, y, *, z="foo"):
...     print(x, y, z)

>>> f(1,2)
1 2 foo

>>> f(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given

f() takes 2 positional arguments but 3 were given

>>> f(1, 2, z = 3)
1 2 3
```

## Positional-Only Arguments

- Verilecek argümanların sadece positional verilmesini sağlar, keyword olarak verilmesini engeller.
    - `/` ifadesiyle belirtilir. Kendinden önce gelen argümanların keyword olarak verilmesini engeller.
    - **NOT:** Python 3.8 ve sonrasında geçerlidir.

```python
>>> def f(x, y, /, z):
...     print(f'x: {x}')
...     print(f'y: {y}')
...     print(f'z: {z}')

>>> f(1, 2, 3)
x: 1
y: 2
z: 3

>>> f(1, 2, z=3)
x: 1
y: 2
z: 3
    
>>> f(x=1, y=2, z=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() got some positional-only arguments passed as keyword arguments:
'x, y'
```

- Positional-Only ve Keyword-Only argümanlar, aynı fonksiyon içinde kullanılabilir.

```python
>>> # This is Python 3.8
>>> def f(x, y, /, z, w, *, a, b):
...     print(x, y, z, w, a, b)
...

# x & y > positional only
# z & w > both positional and keyword
# a & b > keyword only

>>> f(1, 2, z=3, w=4, a=5, b=6)
1 2 3 4 5 6

>>> f(1, 2, 3, w=4, a=5, b=6)
1 2 3 4 5 6
```

## Docstring

- Fonksiyonun hemen girişinde tanımlanan açıklama (documentation) satırıdır. 
- Herhangi bir string belirteçiyle kullanılabilir, fakat genel olarak üç çift tırnak `"""` ile tanımlanır.

```python
>>> def avg(*args):
...     """Returns the average of a list of numeric values."""
...     return sum(args) / len(args)
```

- Fonksiyonlara yazılan docstring'ler, fonksiyon kullanılırken bazı IDE'ler tarafından gösterilir. Ayrıca;
    -  `__doc__` magic attribute'ü ile de ulaşılabilir.
    - Built-in `help()` metodu kullanılarak da erişilebilir.

```python
def foo(bar=0, baz=1):
    """Perform a foo transformation.

    Keyword arguments:
    bar -- magnitude along the bar axis (default=0)
    baz -- magnitude along the baz axis (default=1)
    """
    pass

print(foo.__doc__)

# Perform a foo transformation.
# 
#     Keyword arguments:
#     bar -- magnitude along the bar axis (default=0)
#     baz -- magnitude along the baz axis (default=1)

help(foo)

# Help on function foo in module __main__:
# 
# foo(bar=0, baz=1)
#     Perform a foo transformation.
#     
#     Keyword arguments:
#     bar -- magnitude along the bar axis (default=0)
#     baz -- magnitude along the baz axis (default=1)
```

## Python Function Annotations

- Fonksiyonun parametrelerine ve return değerine metadata/açıklama eklemeye yarar.
    - Annotation = Dipnot

```python
>>> def f(a: '<a>', b: '<b>') -> '<ret_value>':
...     pass
```

- `__annotations__` magic attribute'ü ile bilgilere ulaşılabilir.

```python
>>> f.__annotations__
{'a': '<a>', 'b': '<b>', 'return': '<ret_value>'}
```

- Annotation değerleri herhangi bir türde olabilir. 

```python
>>> def f(a: int, b: str) -> float:
...     print(a, b)
...     return(3.5)

>>> f(1, 'foo')
1 foo
3.5

>>> f.__annotations__
{'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}
```

- Eğer parametrelere default değerler atanacaksa, annotation tanımlamasından sonra atanır.

```python
>>> def f(a: int = 12, b: str = 'baz') -> float:
...     print(a, b)
...     return(3.5)

>>> f.__annotations__
{'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}

>>> f()
12 baz
3.5
```

- Annotation'lar, bilgi vermek dışında herhangi bir amaçları yoktur. Tür kısıtlaması yapmazlar.

```python
>>> def f(a: int, b: str) -> float:
...     print(a, b)
...     return 1, 2, 3
...

>>> f('foo', 2.5)
foo 2.5
(1, 2, 3)
```

## EXTRA : Enforcing Type-Checking

- Function annotation'lar ile type kontrolü yapmak için aşağıdaki gibi bir yöntem kullanılabilir.

```python
>>> def f(a: int, b: str, c: float):
...     import inspect
...     args = inspect.getfullargspec(f).args
...     annotations = inspect.getfullargspec(f).annotations
...     for x in args:
...         print(x, '->',
...             'arg is', type(locals()[x]), ',',
...             'annotation is', annotations[x],
...              '/', (type(locals()[x])) is annotations[x])

>>> f(1, 'foo', 3.3)
a -> arg is <class 'int'> , annotation is <class 'int'> / True
b -> arg is <class 'str'> , annotation is <class 'str'> / True
c -> arg is <class 'float'> , annotation is <class 'float'> / True

>>> f('foo', 4.3, 9)
a -> arg is <class 'str'> , annotation is <class 'int'> / False
b -> arg is <class 'float'> , annotation is <class 'str'> / False
c -> arg is <class 'int'> , annotation is <class 'float'> / False

>>> f(1, 'foo', 'bar')
a -> arg is <class 'int'> , annotation is <class 'int'> / True
b -> arg is <class 'str'> , annotation is <class 'str'> / True
c -> arg is <class 'str'> , annotation is <class 'float'> / False
```

- Bu yöntem decorator halinde de yazılabilir

```python
def type_check_decorator(func):
    def wrapper(*args, **kwargs):
        import inspect
        arguments = inspect.getfullargspec(func).args
        annotations = inspect.getfullargspec(func).annotations
        
        d = dict(zip(arguments, args))
        d.update(kwargs)
        
        if False in [type(d[x]) is annotations[x] for x in arguments]:
            raise Exception("Data validation error!")

        return func(*args, **kwargs)
    return wrapper

@type_check_decorator
def f(a: int, b: str, c: float):
    return (a, b, c)

print(f(1, "foo", 3.4))
# (1, 'foo', 3.4)

print(f(1, 2, 3))
# Traceback (most recent call last):
#   File "C:\Users\serhat\Desktop\test2.py", line 40, in <module>
#     print(f(1, 2, 3))
#   File "C:\Users\serhat\Desktop\test2.py", line 30, in wrapper
#     raise Exception("Data validation error!")
# Exception: Data validation error!
```

