# Döngü İfadeleri - While

## While ile döngüler

```python
while <expr>:
    <statement(s)>
```

- While ifadelerinde, `doğru-yanlış` veya `doğru-yanlış benzeri` her türlü durum kullanılabilir.
    - `Doğru-Yanlış` : True veya False
    - `Doğru-Yalnış Benzeri` (`Truthy-Falsy Statments`) : Data objelerinin boş-dolu halleri, None objesi, sayısal 1-0 ifadeleri vs. 

```python
>>> n = 5
>>> while n > 0:
...     n -= 1
...     print(n)
4
3
2
1
0
```

```python
>>> a = ['foo', 'bar', 'baz']
>>> while a:
...     print(a.pop(-1))
baz
bar
foo
```

## `break` ve `continue` ifadeleri

## Sonsuz döngüler

- Sonsuz döngüler genellikle tek başlarına kullanılmaz, break ifadesi ile birlikte kullanılırlar.

```python
>>> a = ['foo', 'bar', 'baz']
>>> while True:
...     if not a:
...         break
...     print(a.pop(-1))
...
baz
bar
foo
```

## `else` ifadesi

- Python, while ile birlikte else ifadesinin kullanılmasına izin verir. 
- Bu durum, diğer bir çok dilde bulunmayan bir özelliktir.

```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

- else durumu, while döngüsü break ile durdurulmadığı her durumda çalışır.
- Bu nedenle, break durumlarının oluşup oluşmadığı kontrol edilmek istendiğinde kullanılır.

```python
>>> n = 5
>>> while n > 0:
...     n -= 1
...     print(n)
... else:
...     print('Loop done.')
...
4
3
2
1
0
Loop done.
```

```python
>>> n = 0
>>> while n > 0:
...     n -= 1
...     print(n)
... else:
...     print('Loop done.')
...
Loop done.
```

```python
>>> n = 5
>>> while n > 0:
...     n -= 1
...     print(n)
...     if n == 2:
...         break
... else:
...     print('Loop done.')
...
4
3
2
```

- Bir örnek olarak, while ile arama yaparken kullanabiliriz. Eğer item bulunursa break ile durdurulur, bulunmazsa else ile bulunmadığı yazılır.

```python
>>> a = ['foo', 'bar', 'baz', 'qux']
>>> s = 'corge'

>>> i = 0
>>> while i < len(a):
...     if a[i] == s:
...         # Processing for item found
...         break
...     i += 1
... else:
...     # Processing for item not found
...     print(s, 'not found in list.')
...
corge not found in list.
```

## Tek sıra while ifadeleri

```python
>>> n = 5
>>> while n > 0: n -= 1; print(n)

4
3
2
1
0
```

- Tek sıra while ifadeleri kullanılırken, başka while veya if ifadeleriyle birleştirme yapılamaz. 

```python
>>> while n > 0: n -= 1; if True: print('foo')
SyntaxError: invalid syntax
```