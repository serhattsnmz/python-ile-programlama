# Namespaces and Scope in Python

- Python'da tanımlanan değişkenler ve onların değerlerini bulunduran sözlük yapılarına `namespace` denir.
- Pythonda 4 tür namespace bulunur:
    1. Built-In
    2. Global
    3. Enclosing
    4. Local
- Namespace'lerin farklı ömürleri vardır, gereksinim kalmadığında değişkenlerle birlikte silinirler ve ulaşılamazlar.

#### Built-in Namespace

- Python çalışmaya başladığında tanımlanan ve python durana kadar saklı kalan built-in objeleri bulundurur.
- Programın her yerinden ulaşılabilir durumdadırlar.

```python
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError',
 'BaseException','BlockingIOError', 'BrokenPipeError', 'BufferError',
 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
 'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt',
 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration',
 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__',
 '__doc__', '__import__', '__loader__', '__name__', '__package__',
 '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray',
 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex',
 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset',
 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input',
 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

#### Global Namespace

- Bir program modülü içinde, en dış katmanda tanımlanan objelerdir.
- Her modül için farklı namespace'ler oluşturulur. Bir modül `import` ile ana projeye dahil edildiğinde, import edilen global değişkenler de ana projeye eklenmiş olur. 
- Global değişkenler, bulunduğu modül içinde herhangi bir yerde kullanılabilir. Farklı modüller içinde kullanılmak istenildiğinde import edilmeleri gerekir.

#### The Local and Enclosing Namespaces

- Fonksiyonlar içinde tanımlanan objelerdir.
- Sadece bulunduğu fonksiyon içinde kullanılır, dışında kullanılmazlar.
- Fonksiyon çalıştığında tanımlanır, fonksiyon çalışması bittiğinde ulaşılamaz olur.

```python
>>> def f():
...     print('Start f()')
...
...     def g():
...         print('Start g()')
...         print('End g()')
...         return
...
...     g()
...
...     print('End f()')

>>> f()
Start f()
Start g()
End g()
End f()
```

- Yukarıdaki örnekte:
    - `f()` fonksiyonu, `enclosing (kapsayıcı) function`
    - `g()` fonksiyonu, `enclosed (kapsanan) function`
    - 13. satırda `f()` fonksiyonu çalıştğında bu fonksiyon için bir namespace oluşur (`enclosing namespace`)
    - 9. satırda `g()` fonksiyonu çalıştığında bu fonksiyon için de bir namespace oluşur (`local namespace`)
    - `g()` fonksiyonu, `global` ve `f()` fonksiyonunun namespace'ine ulaşabilir.
    - `f()` fonksiyonu sadece `global` namespace'e ulaşabilir.

## Variable Scope and LEGB Rule

- Ulaşılmaya çalışılan bir değişkenin anlamlandırıldığı (değerinin bulunduğu) alan `scope` olarak tanımlanır.
- Python bir değişkenin değerine bakarken sırayla şu yolları takip eder:
    1. Local
    2. Enclosing
    3. Global
    4. Built-in
- Bu sıralama `LEGB Rule` olarak adlandırılır.
    - https://realpython.com/python-namespaces-scope/#variable-scope
- Eğer değişken bu scope'lardan herhangi birinde bulunmazsa `NameError Exception` döner.

## Python Namespace Dictionaries

- Global ve local değişkenlere, dictionary halinda `globals()` ve `locals()` fonksiyonlarıyla ulaşabiliriz.

#### The `Globals()` Function

```python
>>> type(globals())
<class 'dict'>

>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None,
'__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None,
'__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}

>>> x = 'foo'

>>> globals()
{'__name__': '__main__', ..., 'x': 'foo'}
```

- Değişkenler ve global içindeki keyler, aynı değere referans verir.

```python
>>> x
'foo'
>>> globals()['x']
'foo'

>>> x is globals()['x']
True
```

- Değişkenler ve global içindeki keyler aynı yere referans verdiğinden, birinde yapılan değişiklik diğerini de etkiler.

```python
>>> globals()['y'] = 100

>>> globals()
{'__name__': '__main__', ..., 'y': 100}

>>> y
100

>>> globals()['y'] = 3.14159

>>> y
3.14159
```

#### The `locals()` function

```python
>>> def f(x, y):
...     s = 'foo'
...     print(locals())
...

>>> f(10, 0.5)
{'s': 'foo', 'y': 0.5, 'x': 10}
```

- `locals()` fonksiyonu fonksiyon dışında kullanılırsa, `global()` gibi davranır.
- `locals()` ve `globals()` fonksiyonları, genellikle bir değişkenin daha önce tanımlanıp tanımlanmadığını öğrenmek için kullanılır.

```python
>>> x = 10
>>> "x" in globals()
True
>>> "y" in globals()
False

>>> def test():
...     a = 20
...     print("x" in locals())
...     print("x" in globals())
...     print("a" in locals())
...     print("b" in locals())
>>> test()
False
True
True
False
```

- Bir fonksiyon içinde tanımlanan fonksiyonların hepsi bir dict içinde döndürülmek isteniyorsa, pratik olarak `locals()` fonksiyonu kullanılabilir.

```python
## Django View
def my_view(request):
    name = "Joe"
    surname = "Smith"
    age = 30

    return render_to_response('hello.html', locals())
```

> **Deep Dive: A Subtle Difference Between `globals()` and `locals()`**
>
> - `globals()` ve `locals()` fonksiyonları arasında küçük bir fark bulunur. 
> - `globals()` fonksiyonu bir değişkene atandığında, değişken, `globals()` fonksiyonunun temsil ettiği dictionary objesine referans verir. Doğal olarak global sözlüğündeki değişimler, değişkenin içeriğini de etkiler.
>
> ```python
> >>> g = globals()
> >>> g
> {'__name__': '__main__', ...}
> 
> >>> x = 'foo'
> >>> y = 29
> >>> g
> {'__name__': '__main__', ..., 'x': 'foo', 'y': 29}
> ```
>
> - Fakat bu durum `locals()` için farklıdır. Bu fonksiyon return olarak local sözlüğünün bir kopyasını döndürür. Doğal olarak local sözlük içinde sonradan yapılan değişiklikler, atanan değişkenin içeriğini değiştirmez.
>
> ```python
> >>> def f():
> ...     s = 'foo'
> ...     loc = locals()
> ...     print(loc)
> ...
> ...     x = 20
> ...     print(loc)
> ...
> ...     loc['s'] = 'bar'
> ...     print(s)
> 
> >>> f()
> {'s': 'foo'}
> {'s': 'foo'}
> foo
> ```
>
> 

## Modify Variables Out of Scope

-  (Ayrıntılı bilgi için bkz: In-Deph : Function Pass-By-Assigment notu)
- Değişkenleri, kendi alanları dışında kullanmanın ve değiştirmenin bazı limitleri vardır:
    - Global değişkenler, local scope içinde kullanılabilir. (a)
    - Local değişkenler, global scope içinde kullanılmaz. (b)
    - Global `immutable` değişkenler;
        - Local scope içinde tekrar tanımlanabilir, global değişkenden farklıdırlar. (c)
        - Local scope içinde direk olarak üzerinde değişiklik yapılamaz. (d)
    - Global `mutable` değişkenler;
        - Local scope içinde tekrar tanımlanabilir, global değişkenden farklıdırlar. (e)
        - Local scope içinde direk olarak üzerinde değişiklik yapılabilir. (f)

```python
	## (a)
    
>>> a = 10
>>> def f():
...     print(a)
>>> f()
10

	# (b)

>>> def f():
...     b = 20
>>> print(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined

name 'b' is not defined

	# (c)
    
>>> a = 10
>>> def f():
...     a = 20
...     print(a)
>>> f()
20
>>> a
10

	# (d)
    
>>> a = 10
>>> def f():
...     a += 5
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
UnboundLocalError: local variable 'a' referenced before assignment

local variable 'a' referenced before assignment

	# (e)
    
>>> a = [1,2]
>>> def f():
...     a = [3,4]
...     print(a)
>>> f()
[3, 4]
>>> a
[1, 2]

	# (f)

>>> a = [1,2]
>>> def f():
...     a.append(3)
...     a[0] = 0
>>> f()
>>> a
[0, 2, 3]
```

- **Best Practice** : Fonksiyonlar bağımsız birleşenlerdir, dışarıdan bilgileri parametreler ile alır ve dışarıya bilgiyi return ile gönderir. Parametreler ve return dışında dışarıdan bilgi alması veya bilgi göndermesi/değiştirmesi tercih edilmemelidir. Bu nedenle fonksiyonlar içinde nadir olsa da global değişkenler çekilip kullanılmakla beraber, genellikle dışarıdaki herhangi bir değişken değeri değiştirilmez veya yeni değer ataması yapılmaz.

#### The `global` Declaration

- Local scope içinde `global` keyword'ü kullanılarak global değişkenlerin referansı alınıp kullanılabilir. Local scope içinde yeni değişken yaratılmaz, var olan global değişken üzerinde işlemler yapılır.

```python
>>> a = 10

>>> def f():
...     a = 20
>>> f()
>>> a
10

>>> def g():
...     global a
...     a = 20
>>> g()
>>> a
20
```

- `global` keyword'ü kullanmak yerine, direk olarak `globals()` fonksiyonundan gelen dictionary üzerinde de işlem yapılabilir.

```python
>>> a = 10
>>> def f():
...     globals()["a"] = 20
>>> f()
>>> a
20
```

- Global scope içinde tutulan değişkenler dict yapısında olduğunda, daha önce tanımlanmamış bir değişken global keyword'ü ile oluşturulursa globalde de oluşmuş olur. 

```python
>>> y
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    y
NameError: name 'y' is not defined

>>> def g():
...     global y
...     y = 20

>>> g()
>>> y
20
```

- Araya virgül koyularak birden fazla global değişken tanımlanabilr.

```python
>>> x, y, z = 10, 20, 30

>>> def f():
...     global x, y, z
```

#### The `nonlocal` Declaration

- Enclosed function içinde enclosing namespace içindeki değişkenlere referans vermek için kullanılır. Local değişken yaratılmaz veya global değişkenler üzerinde değişiklik yapılmaz var olan enclosing scope içindeki değişkenler kullanılır, yoksa burda yeni değişken oluşturulur.

```python
>>> a = 10						# > Global scope    <------
														# |
>>> def f():											# |
...     a = 20					# > Enclosing scope		# |
...     def g():										# |
...         global a			# global declaration ------
...         a = 30				# > Local scope
...         print("g() :", a)
...     g()
...     print("f() :", a)

>>> f()
g() : 30
f() : 20
>>> print("global :", a)
global : 30
```

```python
>>> a = 10						# > Global scope

>>> def f():
...     a = 20					# > Enclosing scope    <-------
...     def g():											# |
...         nonlocal a			# nonlocal declaration  -------
...         a = 30				# > Local scope
...         print("g() :", a)
...     g()
...     print("f() :", a)

>>> f()
g() : 30
f() : 30
>>> print("global :", a)
global : 10
```

