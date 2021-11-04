# Döngü İfadeleri - For

- Programlama dillerinde `for` kullanımı 3 çeşittir:

**1. Numeric Range Loop**

- Başlangıç ve bitiş değeri verilen iki sayı arasında döngü gerçekleşir.
- BASIC, Algol, Pascal gibi programlama dillerinde kullanılır.

```basic
for i = 1 to 10
    <loop body>
```

**2. Three-Expression Loop**

- 3 ifadeyle oluşturulan döngü ifadesidir.
    - An initialization
    - An expression specifying an ending condition
    - An action to be performed at the end of each iteration.
- C, C#, C++, Java, PHP, Perl gibi dillerde kullanılır.

```c
for (i = 1; i <= 10; i++)
    <loop body>
```

**3. Collection-Based or Iterator-Based Loop**

- Herhangi bir koşul veya integeer tanımlamadan, var olan bir kolleksiyonu döndüren döngü ifadeleridir.
- Diğer dillerdeki `foreach` yapısına benzer.

```python
for i in <collection>
    <loop body>
```

- For döngüleri ile ilgil daha ayrıntılı bilgi için bkz: https://en.wikipedia.org/wiki/For_loop

## For ile Döngüler

```python
for <var> in <iterable>:
    <statement(s)>
```

- Pythonda for döngüsü her türlü `iterable` ifadeyi döndürebilir.

```python
# List
>>> for i in ['foo', 'bar', 'baz']:
...     print(i)

# Tuple
>>> for i in ("foo", "bar", "baz"):
...     print(i)

# String
>>> for i in "serhat":
...     print(i)

# Dictionary
>>> for i in {"a":1, "b":2, "c":3}:
...     print(i)

>>> for i, k in {"a":1, "b":2, "c":3}.items():
...     print(i, "-", k)

>>> a = {"a":1, "b":2, "c":3}
>>> b = a.items()
>>> type(a)
<class 'dict'>
>>> type(b)
<class 'dict_items'>
>>> b
dict_items([('a', 1), ('b', 2), ('c', 3)]) 

# b is List of tuple
# for loops list and every item (tuple) unpack to "i" an "k"
```

## The `range()` Function

- Verilen sayı aralığında bir liste oluşturmaya yarar.
    - `range([start,] stop [, step])`

```python
>>> range(5)
range(0, 5)

>>> list(range(5))
[0, 1, 2, 3, 4]

>>> list(range(2,6))
[2, 3, 4, 5]

>>> list(range(5, 20, 3))
[5, 8, 11, 14, 17]
```

- For ile birlikte kullanıldığında "Numeric Range Loop" oluşturmayı sağlar.

```python
>>> for i in range(3):
...     print(i)
0
1
2
```

- Aldığı parametreler negatif olabilir.

```python
>>> list(range(-5, 5))
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

>>> list(range(5, -5))
[]

>>> list(range(5, -5, -1))
[5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
```

- `range()` fonksiyonu `iterator` özelliğindedir.

    - Oluşturulduğu anda tüm elemanlarını RAM'de oluşturmaz. Bu sayede RAM'de min yer kaplar.

    - Sadece item çekildiğinde ilgili elaman hesaplanıp döndürür.

    - > The advantage of the [`range`](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#range) type over a regular [`list`](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#list) or [`tuple`](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#tuple) is that a [`range`](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#range) object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the `start`, `stop` and `step` values, calculating individual items and subranges as needed).

	    - https://docs.python.org/3.3/library/stdtypes.html?highlight=range#range

```python
>>> a = range(9999999999 * 9999999999 * 9999999999 * 9999999999 * 9999999999 * 9999999999)
>>> a[-1]
999999999400000000149999999980000000001499999999940000000000
>>> list(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: Python int too large to convert to C ssize_t

Python int too large to convert to C ssize_t

>>> l = []
>>> for i in a:
...     l.append(i)
# Program freezed!
KeyboardInterrupt
```

## `break` ve `continue` ifadeleri

```python
>>> for i in ['foo', 'bar', 'baz', 'qux']:
...     if 'b' in i:
...         break
...     print(i)
...
foo
```

```python
>>> for i in ['foo', 'bar', 'baz', 'qux']:
...     if 'b' in i:
...         continue
...     print(i)
...
foo
qux
```

##  `else` ifadesi

```python
>>> for i in ['foo', 'bar', 'baz', 'qux']:
...     print(i)
... else:
...     print('Done.')  # Will execute
...
foo
bar
baz
qux
Done.
```

```python
>>> for i in ['foo', 'bar', 'baz', 'qux']:
...     if i == 'bar':
...         break
...     print(i)
... else:
...     print('Done.')  # Will not execute
...
foo
```
