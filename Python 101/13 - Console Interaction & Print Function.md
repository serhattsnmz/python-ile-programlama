# Console Interaction

## Konsoldan Veri Alma

- `input([<prompt>])` 
- Kullanıcıdan bir satır veri alır. Çalıştığı anda program durur ve kullanıcının input girmesini ve `Enter` tuşuna basmasını bekler. Alınan değer içinde `Enter` karakteri alınmaz.

```python
>>> s = input()
foo bar baz
>>> s
'foo bar baz'
```

- `input()` içine verilen değer, kullanıcıdan veri alınırken gösterilecek yazıyı belirler.

```python
>>> name = input('What is your name?: ')
What is your name?: Winston Smith
>>> name
'Winston Smith'
```

- Aldığı veri `string` yapısındadır. Veriyle herhangi bir sayısal işlem yapılmak isteniyorsa tür dönüşümü yapılmalıdır.

```python
>>> n = input('Enter a number: ')
Enter a number: 50
    
>>> print(n + 100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int

>>> n = int(input('Enter a number: '))
Enter a number: 50
    
>>> print(n + 100)
150
```

## Konsola Veri Yazdırma

- `print(<obj>, ..., <obj>)`
- Fonksiyona birden fazla parametre atanırsa, ön tanımlı olarak hepsinin arasına boşluk bırakarak yazdırır.

```python
>>> fname = 'Winston'
>>> lname = 'Smith'

>>> print('Name:', fname, lname)
Name: Winston Smith
```

- Verilen parametre string türünde değilse, `print` fonksiyonu otomatik olarak stringe çevirip yazdırır.

```python
>>> a = [1, 2, 3]
>>> b = -12
>>> d = {'foo': 1, 'bar': 2}

>>> print(a, b, d, len)
[1, 2, 3] -12 {'foo': 1, 'bar': 2} <built-in function len>
```

## Print Keyword Arguments

- `sep=<str=" ">`

```python
>>> print('foo', 42, 'bar')
foo 42 bar

>>> print('foo', 42, 'bar', sep='/')
foo/42/bar

>>> print('foo', 42, 'bar', sep='...')
foo...42...bar

>>> d = {'foo': 1, 'bar': 2, 'baz': 3}
>>> for k, v in d.items():
...     print(k, v, sep=' -> ')
...
foo -> 1
bar -> 2
baz -> 3

>>> print('foo', 42, 'bar', sep='')
foo42bar
```

- `end=<str="/n">`

```python
>>> if True:
...     print('foo', end='/')
...     print(42, end='/')
...     print('bar')
...
foo/42/bar

>>> for n in range(5):
...     print(n)
...
0
1
2
3
4

>>> for n in range(5):
...     print(n, end=(' ' if n < 4 else '\n'))
...
0 1 2 3 4
```