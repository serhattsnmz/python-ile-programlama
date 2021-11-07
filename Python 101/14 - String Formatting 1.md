# String Formatting - 1

- String formatlama, oluşturulacak string içeriğinin dinamik olarak o anki başka değişken değerleriyle oluşturulması işlemidir. 
- String formatlamayı şu yöntemlerle yapabiliriz:
    - String Modulo Operator : %
    - String `.format()` method
    - Formatted string literal, or "f-string"

## 1. String Modulo Operator : "%"

- Matematik işlemlerinde modül almaya yarayan bu operatör, string değerlerle kullanıldığında formatlama yapar.

```python
<format_string> % <values>
```

- Modulo operatöründen sonra tek bir değer veya değişken gelebileceği gibi birden fazla değer tuple şeklinde de gelebilir.
- Her değer "sırasıyla" formatlanacak string değerin içine yazılır.

```python
>>> print('Hello, my name is %s.' % 'Graham')
Hello, my name is Graham.

>>> print('%d %s cost $%.2f' % (6, 'bananas', 1.74))
6 bananas cost $1.74
```

- Formatlanacak string ifadesinin alacağı değerlerle verilen değerlerin sayıları eşit olmak zorundadır. Aksi halde `TypeError` hatası alınır.

```python
>>> print('%d %s cost $%.2f' % (6, 'bananas'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not enough arguments for format string

not enough arguments for format string

>>> print('%d %s cost $%.2f' % (6, 'bananas', 1.74, "extra"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during string formatting

not all arguments converted during string formatting
```

### 1.1. Conversion Specifiers (Dönüşüm Belirticileri)

- Formatlanacak string içine yazılır ve gelecek değerin nasıl formatlanacağını belirtir.

```python
%[<flags>][<width>][.<precision>]<type>
```

| Component      | Meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| `%`            | Introduces the conversion specifier                          |
| `<flags>`      | Indicates one or more flags that exert finer control over formatting |
| `<width>`      | Specifies the minimum width of the formatted result          |
| `.<precision>` | Determines the length and precision of floating point or string output |
| `<type>`       | Indicates the type of conversion to be performed             |

#### 1.1.a - Conversion Type

- Verilen değerin hangi türde geleceğini belirtir. Farklı bir tür gelirse `TypeError` hatası verir.

| `<type>`      | Conversion Type               |
| ------------- | ----------------------------- |
| `d`, `i`, `u` | Decimal integer               |
| `x`, `X`      | Hexadecimal integer           |
| `o`           | Octal integer                 |
| `f`, `F`      | Floating point                |
| `e`, `E`      | Exponential                   |
| `g`, `G`      | Floating point or Exponential |
| `c`           | Single character              |
| `s`, `r`, `a` | String                        |
| `%`           | Single `'%'` character        |

```python
# INTEGEER
# d, i, and u are functionally equivalent. They all convert the corresponding argument to a string representation of a decimal integer
>>> '%d, %i, %u' % (42, 42, 42)
'42, 42, 42'
>>> '%d, %i, %u' % (-42, -42, -42)
'-42, -42, -42'

# x and X convert to a string representation of a hexadecimal integer value, and o converts to a string representation of an octal integer value
>>> '%x, %X' % (252, 252)
'fc, FC'
>>> '%o' % 16
'20'
```

```python
# FLOAT
>>> '%f, %F' % (3.14159, 3.14)
'3.141590, 3.140000'
>>> '%e, %E' % (1000.0, 1000.0)
'1.000000e+03, 1.000000E+03'

# The g and G conversion types choose between floating point or exponential output, depending on the magnitude of the exponent and the value specified for .<precision>. (See below.) Output is the same as e/E if the exponent is less than -4 or not less than .<precision>. Otherwise, it’s the same as f/F
>>> '%g' % 3.14
'3.14'
>>> '%g' % 0.00000003
'3e-08'
>>> '%G' % 0.00000003
'3E-08'
```

```python
# CHARACTER
>>> '%c' % 97
'a'
>>> '[%c]' % 'y'
'[y]'
# he c conversion type supports conversion to Unicode characters as well:
>>> '%c' % 8721
'∑'

# s, r, and a produce string output using the built-in functions str(), repr(), and ascii(), respectively:
>>> '%s' % 'foo'
'foo'
>>> '%r' % 'foo'
"'foo'"
>>> '%a' % 'foo'
"'foo'"
```

```python
# Inserting a '%' Character
>>> 'Get %d%% off on %s today only!' % (30, 'bananas')
'Get 30% off on bananas today only!'
```

#### 1.1.b - Width and Precision Specifiers

- `<width>` değeri , formatlanacak yapının minimum kaç karakter olması gerektiğini belirtir.
    - Eğer belirtilen değer, gelen değerin uzunluğundan büyükse, bu değer dikkate alınmaz.

```python
>>> '%5s' % 'foo'
'  foo'
>>> '%3d' % 4
'  4'

>>> '%2d' % 1234, '%d' % 1234
('1234', '1234')
>>> '%2s' % 'foobar', '%s' % 'foobar'
('foobar', 'foobar')
```

- `.<precision>` değeri 
    - Float ve üslü sayılarda(`f, F, e, E`), virgülden sonra kaç değerin geleceğini belirtir.
    - `g, G` ifadelerinde toplam digit sayısını belirler.
    - String ifadelerde (`s, r, a`) belirtilen sayı kadar karakteri keser.

```python
>>> '%.2f' % 123.456789
'123.46'

>>> '%.2e' % 123.456789
'1.23e+02'

>>> '%.2g' % 123.456789
'1.2e+02'

>>> '%.4s' % 'foobar'
'foob'

# using width and precision together
>>> '%8.2f' % 123.45678
'  123.46'

>>> '%8.3s' % 'foobar'
'     foo'
```

- `<width>` ve `.<precision>` değerleri, values tuple içinde dışarıdan da verilebilir. Bunun için verilecek değer için yıldız `*` konur. 

```python
>>> '%*d' % (5, 123)
'  123'
>>> '%5d' % 123
'  123'

>>> "%.*f %*.*s" % (1, 5, 3, 2, "foobar")
'5.0  fo'
>>> "%.1f %3.2s" % (5, "foobar")
'5.0  fo'
```

#### 1.1.c - Conversion Flags

| Character         | Controls                                                     |
| ----------------- | ------------------------------------------------------------ |
| `#`               | Display of base or decimal point for integer and floating point values |
| `0`               | Padding of values that are shorter than the specified field width |
| `-`               | Justification of values that are shorter than the specified field width |
| `+` `' '` (space) | Display of leading sign for numeric values                   |

- `#` işareti, format tiplerini ön plana çıkarmak için kullanılır.
    - `o, O, x, X` tiplerinde, format bilgisini de yazar.
    - `d, i, u` integeer tiplerinde herhangi bir değişiklik yapmaz.
    - `f, e` float tiplerinde her durumda nokta kullanılmasını sağlar.
    - Karakter tiplerinde herhangi bir değişiklik yapmaz.

```python
# For the octal and hexadecimal conversion types, the # flag causes base information to be included in the formatted output.

>>> "%o" % 16
'20'
>>> "%#o" % 16
'0o20'

>>> "%x" % 16
'10'
>>> "%#x" % 16
'0x10'

# For floating point values, the # flag forces the output to always contain a decimal point.

>>> '%.0f' % 123
'123'
>>> '%#.0f' % 123
'123.'

>>> '%.0e' % 123
'1e+02'
>>> '%#.0e' % 123
'1.e+02'
```

- `0` işareti, numerik tiplerde belirtilen width değerinin eksik kalan kısımları kadar `0` değeri yazılmasını sağlar. 

```python
>>> l = [1.255, 33.34, 102.1, 1.5, 0.599]
>>> for item in l:
...     print("%8.3f" % item)
   1.255
  33.340
 102.100
   1.500
   0.599
>>> for item in l:
...     print("%06f" % item)
1.255000
33.340000
102.100000
1.500000
0.599000
>>> for item in l:
...     print("%08.3f" % item)
0001.255
0033.340
0102.100
0001.500
0000.599
```

- `-` işareti, tüm alfa-numerik (karakter ve numerik) değerlerde, eğer yazılacak değerin boyutu verilen `<width>` değerinden küçükse, değerin sağına boşluk karakteri ekler.
    - Numerik tiplerde `0` ve   `-` birlikte kullanılmışsa, `0` değeri görmezden gelinir.

```python
>>> s = ["foo", "bar", "example", "test"]

>>> for i in s:
...     print("%s" % i, "=>", "item")
foo => item
bar => item
example => item
test => item

>>> for i in s:
...     print("%10s" % i, "=>", "item")
       foo => item
       bar => item
   example => item
      test => item
    
>>> for i in s:
...     print("%-10s" % i, "=>", "item")
foo        => item
bar        => item
example    => item
test       => item
```

- `+` karakteri, numerik ifadelerde pozitif ve negatif değerlerin yazılmasını sağlar. `" "` (boşluk) karakteri ise sadece negatiflerde negatif işaretini ekler, pozitif değerlerde boşluk ifadesini ekler.

```python
>>> '%5d' % 3
'    3'
>>> '%5d' % -3
'   -3'

>>> '%+5d' % 3
'   +3'
>>> '%+5d' % -3
'   -3'

>>> '% 5d' % 3
'    3'
>>> '% 5d' % -3
'   -3'
```

### 1.2. Modulo Operatörünün Dict ile Kullanımı

- Modulo ile formatlama yapılırken, `<values>` değerini `tuple` yerine `dict` türünde de alabiliriz. Bu tür kullanımlarda `<format_string>` içinde dict keylerinin belirtilmesi gerekir.

```python
>>> '%d %s cost $%.2f' % (6, 'bananas', 1.74)
'6 bananas cost $1.74'

>>> d = {'quantity': 6, 'item': 'bananas', 'price': 1.74}
>>> '%(quantity)d %(item)s cost $%(price).2f' % d
'6 bananas cost $1.74'
```

- Bu tip kullanımda dict içindeki elemanlarının veriliş sırası önemli değildir. 

```python
>>> d = {'quantity': 6, 'item': 'bananas', 'price': 1.74}

>>> '%(quantity)d %(item)s cost $%(price).2f' % d
'6 bananas cost $1.74'

>>> 'It will cost you $%(price).2f for %(item)s, if you buy %(quantity)d' % d
'It will cost you $1.74 for bananas, if you buy 6'
```

