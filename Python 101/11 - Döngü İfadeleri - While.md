# Döngü İfadeleri - While

- `iterable (yinelenebilir)` ve  `iteration (yenileme)`

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

```python
>>> n = 5
>>> while n > 0:
...     n -= 1
...     if n == 2:
...         break
...     print(n)
>>> print('Loop ended.')
4
3
Loop ended.
```

```python
>>> n = 5
>>> while n > 0:
...     n -= 1
...     if n == 2:
...         continue
...     print(n)
>>> print('Loop ended.')
4
3
1
0
Loop ended.
```

- Break ifadesi, iç içe yazılmış döngülerde en yakın döngüyü kapatır.

```python
while <expr1>:
    statement
    statement

    while <expr2>:
        statement
        statement
        break  # Applies to while <expr2>: loop

    break  # Applies to while <expr1>: loop
```

## Sonsuz döngüler

- Sonsuz döngüler genellikle tek başlarına kullanılmaz, break ifadesi ile birlikte kullanılırlar.
- Çok nadir durumlarda, sonsuz döngüler break kullanılmadan yazılabilir.
    - Örneğin bir sensör durumunun düzenli olarak okunup raporlanması
    - Örneğin bir web sitesinin ayakta olup olmadığının düzenli araklıklarla kontrolü

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

```python
import requests
import time

# Request to url until get 200 response
# IMPORTANT: If server is down, the loop will never ends. Use "for" instead of "while"!
while True:
    r = requests.get("google.com")
    if r.status_code == 200:
        break
    time.sleep(1)
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
4
3
2
```

- Bir örnek olarak, while ile arama yaparken kullanabiliriz. Eğer item bulunursa break ile durdurulur, bulunmazsa else ile bulunmadığı yazılır.

```python
>>> a = ['foo', 'bar', 'baz', 'qux']
>>> s = 'corge'

# Search in list with using "while"
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

# There are better ways to do that job...
>>> if s in a:
...     print(s, 'found in list.')
... else:
...     print(s, 'not found in list.')
...
corge not found in list.

>>> try:
...     print(a.index('corge'))
... except ValueError:
...     print(s, 'not found in list.')
...
corge not found in list.
```

- Yukarıda bahsettiğimiz örneğe `else` kullanarak hata denetimi ekleyebiliriz.

```python
import requests
import time

# Request to url until get 200 response
# IMPORTANT: If server is down, the loop will never ends. Use "for" instead of "while"!
a = 5
while a != 0:
    r = requests.get("google.com")
    if r.status_code == 200:
        break
    time.sleep(1)
    a -= 1
else:
    raise Exception("Invalid status code!")
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