# Tür Dönüşümleri

```python
# int, float, str dönüşümleri

>>> a = 10
>>> b = 3.4
>>> c = "20"
>>> d = "4.55"

>>> int(b)
3
>>> int(c)
20
>>> int(d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '4.55'

invalid literal for int() with base 10: '4.55'
    
>>> float(a)
10.0
>>> float(c)
20.0
>>> float(d)
4.55

>>> str(a)
'10'
>>> str(b)
'3.4'
```

```python
# str, bytes dönüşümleri

>>> a = "foo bar"
>>> type(a)
<class 'str'>

>>> b = a.encode()
>>> type(b)
<class 'bytes'>

>>> c = b.decode()
>>> type(c)
<class 'str'>

>>> bytes(a, "utf8")
b'foo bar'
>>> str(b)
"b'foo bar'"
```

```python
# boolean dönüşümleri

>>> x = "True"
>>> y = "False"
>>> t = 1
>>> f = 0
>>> z = 12
>>> k = -1

>>> bool(x)
True
>>> bool(y)
True
>>> bool(t)
True
>>> bool(f)
False
>>> bool(z)
True
>>> bool(k)
True
```

```python
# list, tuple, set, dict dönüşümleri

>>> a = [1,2,3]
>>> b = (1,2,3)
>>> c = {1,2,3}
>>> d = {1:"a", 2:"b", 3:"c"}

>>> list(b)
[1, 2, 3]
>>> list(c)
[1, 2, 3]
>>> list(d)
[1, 2, 3]

>>> tuple(a)
(1, 2, 3)
>>> tuple(c)
(1, 2, 3)
>>> tuple(d)
(1, 2, 3)

>>> set(a)
{1, 2, 3}
>>> set(b)
{1, 2, 3}
>>> set(d)
{1, 2, 3}
```