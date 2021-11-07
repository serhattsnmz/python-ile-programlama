# String Formatting - 2

## 2. String `.format()` Methodu

```python
<template>.format(<positional_argument(s)>, <keyword_argument(s)>)
```

- Modulo operatöre benzer şekilde çalışır, fakat daha esnek bir kullanım sağlar. 
- Belirteç olarak `%` değil `{}` kullanılır.

```python
>>> '%d %s cost $%.2f' % (6, 'bananas', 1.74)
6 bananas cost $1.74

>>> '{} {} cost ${}'.format(6, 'bananas', 1.74)
'6 bananas cost $1.74'
```

- Format içinde, argümanlar index sayılarıyla verilebilir. Bu şekilde, verilen argümanlar farklı sırayla kullanılabilirler.
    - Indexler => `positional arguments`
    - Index kullanmadan yazma => `Automatic replacement`
    - Index kullanarak yazma => `Explicit replacement`

```python
>>> '{0} {1} cost ${2}'.format(6, 'bananas', 1.74)
6 bananas cost $1.74

>>> '${2} => {0} {1}'.format(6, 'bananas', 1.74)
'$1.74 => 6 bananas'
```

- Automatic rep. ve explicit rep. birlikte kullanılmaz. `ValueError` hatası alınır.

```python
>>> '{1}{}{0}'.format('foo','bar','baz')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    '{1}{}{0}'.format('foo','bar','baz')
ValueError: cannot switch from manual field specification to automatic field
 numbering
```

- İstenilirse index yerine keyword'ler de kullanılabilir.

```python
>>> print('{quantity} {item} cost ${price}'.format(
...     quantity=6,
...     item='bananas',
...     price=1.74))
6 bananas cost $1.74
```

- Formatlanacak keywordlerin hepsi tanımlanmak zorundadır, aksi durumda `KeyError` hatası alınır.

```python
>>> '{x}/{y}/{w}'.format(x='foo', y='bar', z='baz')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'w'
```

- Verilen argümanlar, formatlanacak text içinde birden fazla kullanılabilirler.

```python
>>> '{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}'.format('foo', 'bar', 'baz')
'baz.bar.foo/foofoo.barbar.bazbaz'
```

- Formatlanacak text içinde verilen belirteçler, argümanlardan az olabilir ama fazla olamaz. Aksi durumda `IndexError` hatası alınır. 

```python
>>> '{0} {1}'.format(6, 'bananas', 1.74)
'6 bananas'

>>> '{0} {1} cost ${2} {3}'.format(6, 'bananas', 1.74)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 3 out of range for positional args tuple

Replacement index 3 out of range for positional args tuple

>>> '{} {} cost ${} {}'.format(6, 'bananas', 1.74)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 3 out of range for positional args tuple

Replacement index 3 out of range for positional args tuple
```

- Positional ve Keywod argümanları birlikte kullanılabilir ama keyword argümanları her zaman sonda olmak zorundadır. 

```python
>>> '{0}{x}{1}'.format('foo', 'bar', x='baz')
'foobazbar'
>>> '{0}{x}{1}'.format('foo', x='baz', 'bar')
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

### 2.1. Replacement Fields (Dönüşüm Belirticileri)

- Formatlanacak string içine yazılır ve gelecek değerin nasıl formatlanacağını belirtir.

```python
{[<name>][!<conversion>][:<format_spec>]}
```

| Component       | Meaning                                                      |
| --------------- | ------------------------------------------------------------ |
| `<name>`        | Specifies the source of the value to be formatted            |
| `<conversion>`  | Indicates which standard Python function to use to perform the conversion |
| `<format_spec>` | Specifies more detail about how the value should be converted |

#### 2.1.a. `<name>` Belirteci

- Verilen `positional argument` veya `keyword argument` değerlerinin nereye geleceğini belirtir.
    - Keywod ismi veya sayısal değer olabilir.
    - Argüman sayısı ile belirteç sayıları eşitse ve argümanlar belirteçlere sırayla gelecekse, hiç verilmeyebilir.

```python
>>> x, y, z = 1, 2, 3

>>> '{0}, {1}, {baz}'.format(x, y, baz=z)
'1, 2, 3'

>>> '{}, {}, {}'.format(x, y, z)
'1, 2, 3'
```

- Argümanlar koleksiyon tipindeyse (list, tuple veya dict), index numarası veya key ismi bulundurabilirler. Argüman eğer class yapısındayda, class attribute'lerini alabilirler.

```python
>>> a = ['foo', 'bar', 'baz']

>>> '{0[0]}, {0[2]}'.format(a)
'foo, baz'

>>> '{my_list[0]}, {my_list[2]}'.format(my_list=a)
'foo, baz'

>>> d = {'key1': 'foo', 'key2': 'bar'}

>>> '{0[key1]}'.format(d)
'foo'

>>> '{my_dict[key2]}'.format(my_dict=d)
'bar'

>>> z = 3+5j
>>> type(z)
<class 'complex'>
>>> 'real = {0.real}, imag = {0.imag}'.format(z)
'real = 3.0, imag = 5.0'
```

#### 2.1.b. `<conversion>` Belirteci

- `.format()` fonksiyonu, genel olarak verilen argümanları `str()` ile dönüştürerek formatlama yapar. Bazı durumlarda bu dönüşümü zorla gerçekleştirmek için bu belirteçler kullanılabilir.
- Genel olarak ihtiyaç duyulmazlar ama gerektiği yerde kullanılabilmesi için bilinmesinde fayda vardır.

| Value | Meaning                |
| ----- | ---------------------- |
| `!s`  | Convert with `str()`   |
| `!r`  | Convert with `repr()`  |
| `!a`  | Convert with `ascii()` |

```python
>>> '{0!s}'.format(42)
'42'
>>> '{0!r}'.format(42)
'42'
>>> '{0!a}'.format(42)
'42'
```

#### 2.1.c. `<format_spec>` Belirteçi

- Formatlama için genel dönüşüm kontrolünün yapıldığı yerdir.
- Genel form yapısı şu şekildedir:

```
:[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]
```

| Subcomponent | Effect                                                       |
| ------------ | ------------------------------------------------------------ |
| `:`          | Separates the `<format_spec>` from the rest of the replacement field |
| `<fill>`     | Specifies how to pad values that don’t occupy the entire field width |
| `<align>`    | Specifies how to justify values that don’t occupy the entire field width |
| `<sign>`     | Controls whether a leading sign is included for numeric values |
| `#`          | Selects an alternate output form for certain presentation types |
| `0`          | Causes values to be padded on the left with zeros instead of ASCII space characters |
| `<width>`    | Specifies the minimum width of the output                    |
| `<group>`    | Specifies a grouping character for numeric output            |
| `.<prec>`    | Specifies the number of digits after the decimal point for floating-point presentation types, and the maximum output width for string presentations types |
| `<type>`     | Specifies the presentation type, which is the type of conversion performed on the corresponding argument |

##### 2.1.c.1 - `<type>` belirteci

- Modulo operatörde olduğu gibi, verilen değerin hangi tipe çevrileceğinin belirtildiği kısımdır.

| Value      | Presentation Type             |
| ---------- | ----------------------------- |
| `b`        | Binary integer                |
| `c`        | Single character              |
| `d`        | Decimal integer               |
| `e` or `E` | Exponential                   |
| `f` or `F` | Floating point                |
| `g` or `G` | Floating point or Exponential |
| `o`        | Octal integer                 |
| `s`        | String                        |
| `x` or `X` | Hexadecimal integer           |
| `%`        | Percentage                    |

- Modulo operatör ile arasındaki farklar:

| Type     | `.format()` Method                                           | String Modulo Operator                                       |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **b**    | Designates binary integer conversion                         | Not supported                                                |
| **i, u** | Not supported                                                | Designates integer conversion                                |
| **c**    | Designates character conversion, and the corresponding value must be an integer | Designates character conversion, but the corresponding value may be either an integer or a single-character string |
| **g, G** | Chooses between floating point or exponential output, but the rules governing the choice are slightly more complicated | Chooses between floating point or exponential output, depending on the magnitude of the exponent and the value specified for `<prec>` |
| **r, a** | Not supported (though the functionality is provided by the `!r` and `!a` conversion components in the replacement field) | Designates conversion with `repr()` or `ascii()`, respectively |
| **%**    | Converts a numeric argument to a percentage                  | Inserts a literal `'%'` character into the output            |

```python
>>> '%d' % 42
'42'
>>> '{:d}'.format(42)
'42'

>>> '%f' % 2.1
'2.100000'
>>> '{:f}'.format(2.1)
'2.100000'

>>> '%s' % 'foobar'
'foobar'
>>> '{:s}'.format('foobar')
'foobar'

>>> '%x' % 31
'1f'
>>> '{:x}'.format(31)
'1f'
```

```python
>>> '{:b}'.format(257)
'100000001'
>>> '%b' % 257
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: unsupported format character 'b' (0x62) at index 1
    
>>> '%c' % 35
'#'
>>> '%c' % '#'
'#'
>>> '{:c}'.format(35)
'#'
>>> '{:c}'.format('#')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Unknown format code 'c' for object of type 'str'
    
>>> '%f%%' % 65.0
'65.000000%'
>>> '{:%}'.format(0.65)
'65.000000%'
```

##### 2.1.c.2 - `<width>` belirteçi

- Formatlanacak elemanın minimum ne kadar uzunlukta olması gerektiğini belirtir.

```python
>>> '{0:8s}'.format('foo')
'foo     '

>>> '{0:8d}'.format(123)
'     123'

>>> '{0:2s}'.format('foobar')
'foobar'
```

##### 2.1.c.3 - `<fill>` ve `<align>` belirteçleri

- `<width>` tanımlandığında, boş kalan kısımların nasıl doldurulacağını ve text'in nasıl hizalanacağını belirtir.
- Eğer `<width>` tanımlanmamışsa, görmezden gelinir ve hiçbir etkisi yoktur.
- `<aling>` değerleri şunlar olabilir:
    - `<` : Metni sola yasla
    - `>` : Metni sağa yasla
    - `^` : Metni ortala
    - `=` : İşareti olan sayısal ifadelerde kullanılır. İşaret ile sayı arasını açar.

```python
>>> '{0:<8s}'.format('foo')
'foo     '
>>> '{0:<8d}'.format(123)
'123     '

>>> '{0:>8s}'.format('foo')
'     foo'
>>> '{0:>8d}'.format(123)
'     123'

>>> '{0:^8s}'.format('foo')
'  foo   '
>>> '{0:^8d}'.format(123)
'  123   '

>>> '{0:+8d}'.format(123)
'    +123'
>>> '{0:=+8d}'.format(123)
'+    123'

>>> '{0:+8d}'.format(-123)
'    -123'
>>> '{0:=+8d}'.format(-123)
'-    123'
```

- `<fill>` ifadesi, varsayılan olarak boşlukla doldurulan alanları verilen karakter ile doldurur.

```python
>>> '{0:->8s}'.format('foo')
'-----foo'

>>> '{0:#<8d}'.format(123)
'123#####'

>>> '{0:*^8s}'.format('foo')
'**foo***'
```

##### 2.1.c.4 - `<sign>` belirteçi

- Numerik ifadelerin işaretini belirtir.
- `+` kullanıldığında pozitif ve negatif sayıların işaretini yazar.

```python
>>> '{0:+6d}'.format(123)
'  +123'
>>> '{0:+6d}'.format(-123)
'  -123'
```

- `-` kullanıldığında sadece negatif sayıların işareti yazılır.

```python
>>> '{0:-6d}'.format(123)
'   123'
>>> '{0:-6d}'.format(-123)
'  -123'
```

- `" "(boşluk)` kullanıldığında negatif sayıların işaretini yazar, pozitif sayılarda boşluk bırakır.

```python
>>> '{0:*> 6d}'.format(123)
'** 123'

>>> '{0:*>6d}'.format(123)
'***123'

>>> '{0:*> 6d}'.format(-123)
'**-123'
```

##### 2.1.c.5 - `<#>` belirteçi

- Modulo operatörde olduğu gibi, format tiplerini ön plana çıkarmak için kullanılır.
    - `b, o, x, X` tiplerinde, format bilgisini de yazar.
    - `f, e` float tiplerinde her durumda nokta kullanılmasını sağlar.

```python
>>> '{0:b}, {0:#b}'.format(16)
'10000, 0b10000'

>>> '{0:o}, {0:#o}'.format(16)
'20, 0o20'

>>> '{0:x}, {0:#x}'.format(16)
'10, 0x10'

>>> '{0:.0f}, {0:#.0f}'.format(123)
'123, 123.'

>>> '{0:.0e}, {0:#.0e}'.format(123)
'1e+02, 1.e+02'
```

##### 2.1.c.6 - `<0>` belirteçi

- `<width>` ile kullanıldığında, boşluk gelecek yerlere `0` gelmesini sağlar.
    - Numerik ve karakter ifadelerinde kullanılabilir.
    - `<fill>` ile birlikte kullılırsa dikkate alınmaz.

```python
>>> '{0:05d}'.format(123)
'00123'

>>> '{0:08.1f}'.format(12.3)
'000012.3'

>>> '{0:>06s}'.format('foo')
'000foo'

>>> '{0:*>05d}'.format(123)
'**123'
```

##### 2.1.c.7 - `<group>` belirteçi

- Sayıların binlik olarak ayrılmasını sağlar.
    - `,` veya `_` karakterlerinden biri gelebilir.

```python
>>> '{0:d}'.format(1234567)
'1234567'
>>> '{0:,d}'.format(1234567)
'1,234,567'
>>> '{0:_d}'.format(1234567)
'1_234_567'

>>> '{0:.2f}'.format(1234567.89)
'1234567.89'
>>> '{0:,.2f}'.format(1234567.89)
'1,234,567.89'
>>> '{0:_.2f}'.format(1234567.89)
'1_234_567.89'
```

- `_` ifadesi aynı zamanda `b, o, x` değerleriyle de kullanılabilir. 

```python
>>> '{0:_b}'.format(0b111010100001)
'1110_1010_0001'
>>> '{0:#_b}'.format(0b111010100001)
'0b1110_1010_0001'

>>> '{0:_x}'.format(0xae123fcc8ab2)
'ae12_3fcc_8ab2'
>>> '{0:#_x}'.format(0xae123fcc8ab2)
'0xae12_3fcc_8ab2'
```

##### 2.1.c.8 - `.<prec>` belirteçi

- Decimal ve float sayılarının ondalık kısımlarında kaç sayının geleceğini belirtir.

```python
>>> '{0:8.2f}'.format(1234.5678)
' 1234.57'
>>> '{0:8.4f}'.format(1.23)
'  1.2300'

>>> '{0:8.2e}'.format(1234.5678)
'1.23e+03'
>>> '{0:8.4e}'.format(1.23)
'1.2300e+00'
```

- String ifadelerde max genişliği ifade eder ve fazla karakterleri siler.

```python
>>> '{:.4s}'.format('foobar')
'foob'
```

### 2.2. Nested Replacement Fields

- Dönüşüm belirteç değerlerinin dışarıdan alınması işlemidir. Bu işlem, modulo operatörde olduğu gibi `*` işaretiyle yapılır.

```python
>>> '%*.*f' % (10, 2, 123.456)  # Width is 10, precision is 2
'    123.46'

>>> '{0:10.2f}'.format(123.456)
'    123.46'

>>> '{2:{0}.{1}f}'.format(10, 2, 123.456)
'    123.46'

>>> '{val:{wid}.{pr}f}'.format(wid=10, pr=2, val=123.456)
'    123.46'
```

- Modulo operatörde sadece `<width>` ve `<prec>` belirteçleri dışarıdan değer alabilirken,  `.format()` metodunda her değer dışarıdan alınabilir.

```python
>>> bin(10), oct(10), hex(10)
('0b1010', '0o12', '0xa')
>>> for t in ('b', 'o', 'x'):
...     print('{0:#{type}}'.format(10, type=t))
...
0b1010
0o12
0xa

>>> '{0:{grp}d}'.format(123456789, grp='_')
'123_456_789'
>>> '{0:{grp}d}'.format(123456789, grp=',')
'123,456,789'
```