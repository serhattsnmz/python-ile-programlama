# String Formatting - 3

## 3. The Python Formatted String Literal (f-String)

- Herhangi bir string değişkenin başına `f` veya `F` harfi getirilerek `f-string` oluşturulur. Normal durumda `string` türünden hiçbir farkı yoktur ve type olarak `str` döndürür.

```python
>>> f"foo bar"
'foo bar'
>>> type(f"foo bar")
<class 'str'>
```

- F-string içinde herhangi bir değişken `{}` karakterleri arasında tanımlanabilir ve verilen değişken string değere formatlanarak eklenir.

```python
>>> s = "bar"

>>> f"foo.{s}.baz"
'foo.bar.baz'

>>> "foo.{s}.baz"
'foo.{s}.baz'
```

```python
>>> quantity = 6
>>> item = 'bananas'
>>> price = 1.74

>>> print('{0} {1} cost ${2}'.format(quantity, item, price))
6 bananas cost $1.74

>>> print(f'{quantity} {item} cost ${price}')
6 bananas cost $1.74
```

- F-string içine verilen ifadeler karmaşık olabilir. 

```python
	# Can be variables...

>>> quantity, item, price = 6, 'bananas', 1.74
>>> f'{quantity} {item} cost ${price}'
'6 bananas cost $1.74'

	# Can be objects...

>>> a = ['foo', 'bar', 'baz']
>>> d = {'foo': 1, 'bar': 2}
>>> print(f'a = {a} | d = {d}')
a = ['foo', 'bar', 'baz'] | d = {'foo': 1, 'bar': 2}

	# Can be indexing, slicing or key reference...

>>> a = ['foo', 'bar', 'baz']
>>> d = {'foo': 1, 'bar': 2}

>>> print(f'First item in list a = {a[0]}')
First item in list a = foo

>>> print(f'Last two items in list a = {a[-2:]}')
Last two items in list a = ['bar', 'baz']

>>> print(f'List a reversed = {a[::-1]}')
List a reversed = ['baz', 'bar', 'foo']

>>> print(f"Dict value for key 'bar' is {d['bar']}")
Dict value for key 'bar' is 2

    # Function can be called in f-string...

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux']
>>> print(f'List a has {len(a)} items')
List a has 5 items

>>> s = 'foobar'
>>> f'--- {s.upper()} ---'
'--- FOOBAR ---'

	# Conditional expressions...

>>> x = 3
>>> y = 7
>>> print(f'The larger of {x} and {y} is {x if x > y else y}')
The larger of 3 and 7 is 7

>>> age = 13
>>> f'I am {"a minor" if age < 18 else "an adult"}.'
'I am a minor.'

	# Or attribues...

>>> z = 3+5j
>>> z
(3+5j)

>>> print(f'real = {z.real}, imag = {z.imag}')
real = 3.0, imag = 5.0
```

- F-string içinde köşeli parantezin kendisi kullanılmak isteniyorsa, karakter çift yazılır.

```python
>>> z = 'foobar'
>>> f'{{ {z[::-1]} }}'
'{ raboof }'
```

- Hata durumları:
    - F-string alanı boş olursa `SyntaxError` hatası alınır.
    - F-string içinde backslash(`\`) kullanılamaz, `SyntaxError` hatası alınır.
        - Eğer backslash kullanılacak bir durum varsa, bir değişkene atanarak kullanılabilir.
    - F-string içinde `#` işareti kullanılamaz, `SyntaxError` hatası alınır.
    - F-string içinde string ifade kullanılacaksa, ana string ile aynı string oluştma karakterini (`", ', """`) kullanamaz, `SyntaxError` hatası alınır.

```python
>>> f'foo{}bar'
  File "<stdin>", line 1
SyntaxError: f-string: empty expression not allowed
```

```python
>>> a = 5
>>> f"foo{' ' if a == 5 else '\n'}bar"
  File "<stdin>", line 1
SyntaxError: f-string expression part cannot include a backslash

>>> a = 5
>>> bs = "\n"
>>> f"foo{' ' if a == 5 else bs}bar"
'foo bar'
```

```python
>>> print(f'''foo{
... z    # Comment
... }''')
  File "<stdin>", line 3
SyntaxError: f-string expression part cannot include '#'
```

```python
>>> f"foo.{"baz"}.bar"
  File "<stdin>", line 1
    f"foo.{"baz"}.bar"
            ^
SyntaxError: f-string: expecting '}'
>>> f"foo.{'baz'}.bar"
'foo.baz.bar'
```

### 3.1. Dönüşüm Belirteçleri

- F-string dönüşüm belirteçleri, `.format()` belirteçleriyle birebir aynıdır.

```python
>>> s = 'foo'

>>> '{0!r}'.format(s)
"'foo'"
>>> f'{s!r}'
"'foo'"

>>> n = 123
>>> '{:=+8}'.format(n)
'+    123'
>>> f'{n:=+8}'
'+    123'

>>> s = 'foo'
>>> '{0:*^8}'.format(s)
'**foo***'
>>> f'{s:*^8}'
'**foo***'

>>> n = 0b111010100001
>>> '{0:#_b}'.format(n)
'0b1110_1010_0001'
>>> f'{n:#_b}'
'0b1110_1010_0001'
```

- F-string belirteçleri, `.format()` metodunda olduğu gibi dışarından değer almayı destekler (Nesting).

```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux']
>>> w = 4
>>> f'{len(a):0{w}d}'
'0005'

>>> n = 123456789
>>> sep = '_'
>>> f'{(n * n):{sep}d}'
'15_241_578_750_190_521'
```