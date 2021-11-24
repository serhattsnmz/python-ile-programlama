# Karakter Veri Yapısı

- Tek tırnak veya çift tırnak ile tanımlanabilir.
- Birden fazla satırda tanımlama yapılacaksa üç tırnakla tanımlama yapılabilir.
- Max sınırı yoktur. Çalıştırılan makinenin memory değeriyle sınırlıdır.
- Eğer string içinde tek veya çift tırnak kullanılacaksa;
  - Tek tırnak barındıran string çift tırnak içinde yazılabilir.
  - Çift tırnak barındıran string tek tırnak içinde yazılabilir.
  - Üç tırnak kullanılabilir.
  - Kaçış karakteri kullanılabilir.
- "None" ve "Empty" arasındaki farklar

## Kaçış Karakterleri

| Escape Sequence | Usual Interpretation of Character(s) After Backslash  | “Escaped” Interpretation                                     |
| --------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| `\'`            | Terminates string with single quote opening delimiter | Literal single quote (`'`) character                         |
| `\"`            | Terminates string with double quote opening delimiter | Literal double quote (`"`) character                         |
| `\<newline>`    | Terminates input line                                 | [Newline is ignored](https://stackoverflow.com/questions/48693600/what-does-the-newline-escape-sequence-mean-in-python) |
| `\\`            | Introduces escape sequence                            | Literal backslash (`\`) character                            |

```python
>>> print('a\
... b\
... c')
abc
```

| Escape Sequence | “Escaped” Interpretation                            |
| --------------- | --------------------------------------------------- |
| `\a`            | ASCII Bell (`BEL`) character                        |
| `\b`            | ASCII Backspace (`BS`) character                    |
| `\f`            | ASCII Formfeed (`FF`) character                     |
| `\n`            | ASCII Linefeed (`LF`) character                     |
| `\N{<name>}`    | Character from Unicode database with given `<name>` |
| `\r`            | ASCII Carriage Return (`CR`) character              |
| `\t`            | ASCII Horizontal Tab (`TAB`) character              |
| `\uxxxx`        | Unicode character with 16-bit hex value `xxxx`      |
| `\Uxxxxxxxx`    | Unicode character with 32-bit hex value `xxxxxxxx`  |
| `\v`            | ASCII Vertical Tab (`VT`) character                 |
| `\ooo`          | Character with octal value `ooo`                    |
| `\xhh`          | Character with hex value `hh`                       |

```python
>>> print("a\tb")
a    b
>>> print("a\141\x61")
aaa
>>> print("a\nb")
a
b
>>> print('\u2192 \N{rightwards arrow}')
→ →
```

## Raw String

* `r` veya `R` öneki ile belirtilir.
* Önüne geldiği string ifadenin içindeki kaçış karakterlerini direk olarak yazdırmaya yarar.

```python
>>> print('foo\nbar')
foo
bar
>>> print(r'foo\nbar')
foo\nbar

>>> print('foo\\bar')
foo\bar
>>> print(R'foo\\bar')
foo\\bar
```

## String Operatörleri

- (+) String birleştirme 
- (*) String çoğaltma
- (in) String içinde belli bir kelimenin olup olmadığına bakma
- (not in) in yapısının tersi

## Gömülü (Built-in) String Fonksiyonları

| Function | Description                                                  |
| -------- | ------------------------------------------------------------ |
| `chr()`  | Converts an integer to a character - (py2:ASCII value, py3:Unicode value) |
| `ord()`  | Converts a character to an integer - (py2:ASCII value, py3:Unicode value) |
| `len()`  | Returns the length of a string                               |
| `str()`  | Returns a string representation of an object                 |

## Index ve Slicing İşlemleri

- String yapıları **_karakter dizileri_** olduklarından, diziler gibi index ve slicing işlemleri yapılabilir.

```python
deger = "serhat"

print(deger[1])     # "s"
print(deger[2:5])   # "rha"
print(deger[:5])    # "serha"
print(deger[0:5])   # "serha"
print(deger[2:])    # "rhat"
```

- İndex işlemlerinde sayı, len uzunluğuna eşit veya fazla olursa OutOfRange hatası alınır. 
- Slice işlemlerinde OutOfRange hatası alınmaz.

```
-6 -5 -4 -3 -2 -1 >> Tersten index numarası
 s  e  r  h  a  t
 0  1  2  3  4  5 >> İndex numarası
```

- Slice işlemlerinde 3. değer yazılarak atlama işlemleri yapılabilir.

```python
deger = "serhat"

print(deger[::2])       # "sra"
print(deger[-1:-6:-2])  # "the"
```

- Basit olarak string ters çevirme işlemleri şu şekilde yapılabilir:

```python
deger = "serhat"

print(deger[::-1])		# tahres
```

> **NOT : ** Herhangi bir string değerinin slice edildikten sonraki hali orjinal ile aynıysa yeni bir değişken referansı oluşmaz, slice referansı orjinal değerle aynıdır.
>
> ```python
> >>> s = 'foobar'
> >>> t = s[:]
> 
> >>> id(s)
> 59598496
> >>> id(t)
> 59598496
> 
> >>> s is t
> True
> ```

## String Formatlama

- print() fonksiyonunda, araya virgül koyularak formatlama yapılabilir.

```python
>>> n = 20
>>> m = 25
>>> prod = n * m
>>> print('The product of', n, 'and', m, 'is', prod)
The product of 20 and 25 is 500
```

- `%-formatting`

```python
>>> name = "Eric"
>>> "Hello, %s." % name
'Hello, Eric.'
```

- `s.format()` fonksiyonu kullanılabilir.

```python
>>> "{} {}".format("Python", "Programlama")
'Python Programlama'

>>> "{} {}".format("Python", "Programlama", "deneme")
'Python Programlama'

>>> "{} {}".format("Python")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range

tuple index out of range

>>> "Hello, {1}. You are {0}.".format(age, name)
'Hello, Eric. You are 74.'
```

- `f""` yapısı kullanılarak formatlama yapılabilir. 
- Bu yapı sadece python 3.6 ve sonrasında kullanılabilir.

```python
>>> n = 20
>>> m = 25
>>> prod = n * m
>>> print(f'The product of {n} and {m} is {prod}')
The product of 20 and 25 is 500
```

- Formatlama ile ilgili bakınız : https://pyformat.info/

## String Dönüştürme Fonksiyonları

- `s.capitalize()` : Verilen stringin baş harfini büyültür, diğerlerini küçültür.

```python
>>> 'foO BaR BAZ quX'.capitalize()
'Foo bar baz qux'
```

- `s.lower()` : Tüm harfleri küçültür.

```python
>>> 'FOO Bar 123 baz qUX'.lower()
'foo bar 123 baz qux'
```

- `s.upper()` : Tüm harfleri büyültür.

```python
>>> 'FOO Bar 123 baz qUX'.upper()
'FOO BAR 123 BAZ QUX'
```

- `s.swapcase()` : Küçüklük ve büyüklük durumunu tersine çevirir. 

```python
>>> 'FOO Bar 123 baz qUX'.swapcase()
'foo bAR 123 BAZ Qux'
```

- `s.title()` : Her kelimenin baş harfini büyük harfe, diğerlerini küçük harfe çevirir.

```python
>>> 'the sun also rises'.title()
'The Sun Also Rises'
```

## String İçinde Arama Yapma Fonksiyonları

- `s.count(<sub>[, <start>[, <end>]])` : Verilen değeri kelime içinde sayar

```python
>>> 'foo goo moo'.count('oo')
3
```

- `s.endswith(<suffix>[, <start>[, <end>]])` : True veya False döner

```python
>>> 'foobar'.endswith('bar')
True
>>> 'foobar'.endswith('baz')
False
```

- `s.startswith(<prefix>[, <start>[, <end>]])`: True veya False döner

```python
>>> 'foobar'.startswith('foo')
True
>>> 'foobar'.startswith('bar')
False
```

- `s.find(<sub>[, <start>[, <end>]])` : Değeri string içinde arar. Bulursa, ilk bulduğu değerin index numarasını verir. Bulamazsa -1 döner.

```python
>>> 'foo bar foo baz foo qux'.find('foo')
0
>>> 'foo bar foo baz foo qux'.find('grault')
-1
>>> 'foo bar foo baz foo qux'.find('foo', 4)
8
>>> 'foo bar foo baz foo qux'.find('foo', 4, 7)
-1
```

- `s.index(<sub>[, <start>[, <end>]])` : Find metoduyla aynı işleve sahiptir. Ama değer bulunamazsa -1 yerine ValueError döner.

```python
>>> 'foo bar foo baz foo qux'.index('grault')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    'foo bar foo baz foo qux'.index('grault')
ValueError: substring not found
```

- `s.rfind(<sub>[, <start>[, <end>]])` : Find metodunun tersten aramasını yapar. (Bulunan en yüksek index numarasını verir.)

```python
>>> 'foo bar foo baz foo qux'.rfind('foo')
16
>>> 'foo bar foo baz foo qux'.rfind('grault')
-1
```

- `s.rindex(<sub>[, <start>[, <end>]])`: Index metodunun tersten aramasını yapar. (Bulunan en yüksek index numarasını verir.)

```python
>>> 'foo bar foo baz foo qux'.rindex('grault')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    'foo bar foo baz foo qux'.rindex('grault')
ValueError: substring not found
```

## String Sınıflandırma Fonksiyonları

- `s.isalnum()` : Tüm karakterler alfanumerik ise True döner. True veya False döner.

```python
>>> 'abc123'.isalnum()
True
>>> 'abc$123'.isalnum()
False
>>> ''.isalnum()
False
```

- `s.isalpha()` : Tüm karakterler alfabetik ise True döner. True veya False döner.

```python
>>> 'ABCabc'.isalpha()
True
>>> 'abc123'.isalpha()
False
```

- `s.isdigit()` : Tüm karakterler numerik ise True döner. True veya False döner.

```python
>>> '123'.isdigit()
True
>>> '123abc'.isdigit()
False
```

- `s.isidentifier()` : Değişken ismine uygun olup olmadığını gösterir. True veya False döner.

```python
>>> 'foo32'.isidentifier()
True
>>> '32foo'.isidentifier()
False
>>> 'foo$32'.isidentifier()
False
```

> **NOT :** `s.isidentifier()` fonksiyonu, keyword değerleri için de True döner. String değerinin keyword olup olmadığı başka bir kütüphane ile belirlenebilir:
>
> ```python
> >>> 'and'.isidentifier()
> True
> 
> >>> from keyword import iskeyword
> >>> iskeyword('and')
> True
> 
> >>> test = "or"
> >>> test.isidentifier() and not iskeyword(test)
> False
> 
> >>> test = "number"
> >>> test.isidentifier() and not iskeyword(test)
> True
> ```
>
> 

- `s.islower()` : True veya False döner.

```python
>>> 'abc'.islower()
True
>>> 'abc1$d'.islower()
True
>>> 'Abc1$D'.islower()
False
```

- `s.istitle()` : True veya False döner.

```python
>>> 'This Is A Title'.istitle()
True
>>> 'This is a title'.istitle()
False
>>> 'Give Me The #$#@ Ball!'.istitle()
True
```

- `s.isupper()` : True veya False döner.

```python
>>> 'ABC'.isupper()
True
>>> 'ABC1$D'.isupper()
True
>>> 'Abc1$D'.isupper()
False
```

- `s.isprintable()` : Tüm karakterlerin yazılabilir olup olmadığını gösterir.

```python
>>> 'a\tb'.isprintable()
False
>>> 'a b'.isprintable()
True
>>> ''.isprintable()
True
>>> 'a\nb'.isprintable()
False
```

- `s.isspace()` : Değer boş değilse ve tüm karakterler "Whitespace" karakterlerden oluşuyorsa True döner.

```python
>>> ' \t \n '.isspace()
True
>>> '   a   '.isspace()
False
```

## String Formatlama Fonksiyonları

- `s.replace(<old>, <new>[, <count>])`  : Verilen değerleri yenisiyle değiştirir. Sayı verilirse sadece o sayı kadarını değiştirir. Aksi halde hepsini değiştirir.

```python
>>> 'foo bar foo baz foo qux'.replace('foo', 'grault')
'grault bar grault baz grault qux'
>>> 'foo bar foo baz foo qux'.replace('foo', 'grault', 2)
'grault bar grault baz foo qux'
```

- `s.center(<width>[, <fill>])` : Verilen sayı kadar alana yaslama yapar.

```python
>>> 'foo'.center(10)
'   foo    '
>>> 'bar'.center(10, '-')
'---bar----'
>>> 'foo'.center(2)
'foo'
```

- `s.expandtabs(tabsize=8)` : Tab karakterlerini boşluk ile değiştirir.

```python
>>> 'a\tb\tc'.expandtabs()
'a       b       c'
>>> 'aaa\tbbb\tc'.expandtabs()
'aaa     bbb     c'
>>> 'a\tb\tc'.expandtabs(4)
'a   b   c'
>>> 'aaa\tbbb\tc'.expandtabs(tabsize=4)
'aaa bbb c'
```

- `s.rjust(<width>[, <fill>])` : Verilen sayı kadar alana yaslama yapar.

```python
>>> 'foo'.rjust(10)
'       foo'
>>> 'foo'.rjust(10, '-')
'-------foo'
```

- `s.ljust(<width>[, <fill>])` : Verilen sayı kadar alana yaslama yapar.

```python
>>> 'foo'.ljust(10)
'foo       '
>>> 'foo'.ljust(10, '-')
'foo-------'
```

- `s.strip([<chars>])` : Boşluk, \n, \t gibi karakterleri kaldırır. Opsiyonel olarak parametre verilirse, parametre stringi içindeki her bir karakteri ayrı ayrı kaldırır.

```python
>>> '   foo bar baz\t\t\t'.strip()
'foo bar baz'
>>> 'www.realpython.com'.strip('w.moc')
'realpython'
```

- `s.lstrip([<chars>])` : Boşluk, \n, \t gibi karakterleri kaldırır. Opsiyonel olarak parametre verilirse, parametre stringi içindeki her bir karakteri ayrı ayrı kaldırır.

```python
>>> '   foo bar baz   '.lstrip()
'foo bar baz   '
>>> '\t\nfoo\t\nbar\t\nbaz'.lstrip()
'foo\t\nbar\t\nbaz'
>>> 'http://www.realpython.com'.lstrip('/:pth')
'www.realpython.com'
```

- `s.rstrip([<chars>])` : Boşluk, \n, \t gibi karakterleri kaldırır. Opsiyonel olarak parametre verilirse, parametre stringi içindeki her bir karakteri ayrı ayrı kaldırır.

```python
>>> '   foo bar baz   '.rstrip()
'   foo bar baz'
>>> 'foo\t\nbar\t\nbaz\t\n'.rstrip()
'foo\t\nbar\t\nbaz'
>>> 'foo.$$$;'.rstrip(';$.')
'foo'
```

- `s.zfill(<width>)` : `rjust` gibi davranır, string değerinin başına "0" karakterini ekler. Eğer negatif veya pozitif belirleyici varsa, bu değerlerin baştaki yerini korur. Sayısal ifadeleri belli bir karakter sayısına ulaştırmak için kullanılır ama normal string ifadelerde kullanılabilir.

```python
>>> '42'.zfill(5)
'00042'

>>> '+42'.zfill(8)
'+0000042'
>>> '-42'.zfill(8)
'-0000042'

>>> '-42'.zfill(3)
'-42'

>>> 'foo'.zfill(6)
'000foo'
```

## String ve List Arasında Dönüşüm Yapma

- `s.join(<iterable>)`

```python
>>> ', '.join(['foo', 'bar', 'baz', 'qux'])
'foo, bar, baz, qux'

>>> ':'.join('corge')
'c:o:r:g:e'
```

- Join() kullanılırken, verilen elemanların hepsinin string olması gerekmektedir.

```python
>>> '---'.join(['foo', 23, 'bar'])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    '---'.join(['foo', 23, 'bar'])
TypeError: sequence item 1: expected str instance, int found
```

- `list(<string>)`

```python
>>> list('corge')
['c', 'o', 'r', 'g', 'e']
```

- `s.partition(<sep>)` : Verilen string değerine göre ana string ifadeyi ikiye böler. Çıktı olarak 1. ilk bölünmüş kısım 2. seperator 3. kalan kısmı verir.

```python
>>> 'foo.bar'.partition('.')
('foo', '.', 'bar')
>>> 'foo@@bar@@baz'.partition('@@')
('foo', '@@', 'bar@@baz')
>>> 'foo.bar'.partition('@@')
('foo.bar', '', '')
```

- `s.rpartition(<sep>)` : Partition ile aynı fakat bölmeye sondan başlar. 

```python
>>> 'foo@@bar@@baz'.rpartition('@@')
('foo@@bar', '@@', 'baz')
```

- `s.split(sep=None, maxsplit=-1)` : Verilen karaktere göre yapıyı böler ve listeye çevirir. Default olarak whitespace karakterlerin tümünü sep olarak dikkate alır.

```python
>>> 'foo bar baz qux'.split()
['foo', 'bar', 'baz', 'qux']
>>> 'foo\n\tbar   baz\r\fqux'.split()
['foo', 'bar', 'baz', 'qux']

>>> 'foo.bar.baz.qux'.split(sep='.')
['foo', 'bar', 'baz', 'qux']

>>> 'www.realpython.com'.split('.', maxsplit=1)
['www', 'realpython.com']
```

- `s.rsplit(sep=None, maxsplit=-1)` : Verilen karaktere göre yapıyı TERSTEN böler ve listeye çevirir.

```python
>>> 'foo bar baz qux'.rsplit()
['foo', 'bar', 'baz', 'qux']
>>> 'foo\n\tbar   baz\r\fqux'.rsplit()
['foo', 'bar', 'baz', 'qux']

>>> 'foo.bar.baz.qux'.rsplit(sep='.')
['foo', 'bar', 'baz', 'qux']

>>> 'www.realpython.com'.rsplit('.', maxsplit=1)
['www.realpython', 'com']
```

- `s.splitlines([<keepends>])` : Satır karakterlerine göre bölme işlemi yapar.

```python
>>> 'foo\nbar\r\nbaz\fqux\u2028quux'.splitlines()
['foo', 'bar', 'baz', 'qux', 'quux']

>>> 'foo\f\f\fbar'.splitlines()
['foo', '', '', 'bar']

>>> 'foo\nbar\nbaz\nqux'.splitlines(True)
['foo\n', 'bar\n', 'baz\n', 'qux']
```

| Escape Sequence  | Character                     | 
| ---------------- | ----------------------------- | 
| \n	           | Newline                       |
| \r	           | Carriage Return               |
| \r\n	           | Carriage Return + Line Feed   |
| \v or \x0b	   | Line Tabulation               |
| \f or \x0c       | Form Feed                     |
| \x1c	           | File Separator                |
| \x1d	           | Group Separator               |
| \x1e	           | Record Separator              |
| \x85	           | Next Line (C1 Control Code)   |
| \u2028	       | Unicode Line Separator        |
| \u2029	       | Unicode Paragraph Separator   |

# Bytes Veri Yapısı

- Bytes veri yapısı byte değerlerinden oluşan binary dataları tanımlamak için kullanılır.
- Bytes objesinin her bir elemanı small integeer değeridir ve 0-255 arasındadır.
- `b` öneki ile gösterilir.

```python
>>> b = b'foo bar baz'
>>> b
b'foo bar baz'
>>> type(b)
<class 'bytes'>
```

- Yalnızca ASCII karakterler desteklenir. Değeri 127'den fazla olan (ASCII olmayan) karakterler, kaçış karakterleri kullanılarak gösterilir.

```python
>>> b = b'foo\xddbar'
>>> b
b'foo\xddbar'
>>> b[3]
221
>>> int(0xdd)
221
>>> chr(221)
'Ý'
```

- String ve Bytes arasındaki farklar:
    - String, temelde karakter içerir, Bytes ise byte dizisi içerir.
    - String, insanların okuyabileceği yapıdadır, bytes ise makinenin okuyabileceği yapıdadır.
    - Bytes tipi direk disk üzerinde saklanabilirken, string tipi öncelikli olarak encode edilir, sonra saklanır.
- Çevirme işlemlerinin adlandırılması
    - String >> Bytes : Encoding
    - Bytes >> String : Decoding


- `bytes(<s>, <encoding>)` : Stringi verilen encoding yapısına göre bytes tipine çevirir. 

```python
>>> b = bytes('foo.bar', 'utf8')
>>> b
b'foo.bar'
>>> type(b)
<class 'bytes'>
```


- `bytes(<size>)` : Verilen karakter sayısı kadar null byte üretir.

```python
>>> b = bytes(8)
>>> b
b'\x00\x00\x00\x00\x00\x00\x00\x00'
>>> type(b)
<class 'bytes'>
```


- `bytes(<iterable>)` : Integeer dizisinden bytes üretir.

```python
>>> b = bytes([100, 102, 104, 106, 108])
>>> b
b'dfhjl'
>>> type(b)
<class 'bytes'>
>>> b[2]
104
```


- `bytes.fromhex(<s>)` : Hex yapısından bytes yapısı oluşturur.

```python
>>> b = bytes.fromhex(' aa 68 4682cc ')
>>> b
b'\xaahF\x82\xcc'
>>> list(b)
[170, 104, 70, 130, 204]
```


- `b.hex()` : Bytes tipinin hex karşılığını gösterir.

```python
>>> b = bytes.fromhex(' aa 68 4682cc ')
>>> b
b'\xaahF\x82\xcc'

>>> b.hex()
'aa684682cc'
>>> type(b.hex())
<class 'str'>
```


- `b.decode(<encoding>)` : Bytes to string (default encoding : utf8)
- `s.encode(<encoding>)` : String to Bytes (default encoding : utf8)

# Bytearray Veri Yapısı

- `bytearray` veri yapısı, `bytes` gibi binary dataları tanımlar ve `bytes` veri yapısıyla aşağıdaki özellikler dışında benzerdir.
- `bytearray` veri yapısını tanımlamak içn özel bir önek bulunmamaktadır. Sadece `bytearray()` built-in fonksiyonuyla tanımlama yapılır.

```python
>>> ba = bytearray('foo.bar.baz', 'UTF-8')
>>> ba
bytearray(b'foo.bar.baz')

>>> bytearray(6)
bytearray(b'\x00\x00\x00\x00\x00\x00')

>>> bytearray([100, 102, 104, 106, 108])
bytearray(b'dfhjl')

>>> ba = bytearray(b'foo')
>>> ba
bytearray(b'foo')
```

- `bytearray` veri tipi "mutable", `bytes` veri tipi "immutable" tiptedir. Bunun anlamı `bytearray` verisi içindeki değerler değiştirilebilirken, `bytes` yapısı içindeki değerler değiştirilemez.

```python
>>> ba = bytearray('foo.bar.baz', 'UTF-8')
>>> ba
bytearray(b'foo.bar.baz')

>>> ba[5] = 0xee
>>> ba
bytearray(b'foo.b\xeer.baz')

>>> ba[8:11] = b'qux'
>>> ba
bytearray(b'foo.b\xeer.qux')

>>> b = b'foo.bar.baz'
>>> b
b'foo.bar.baz'

>>> b[5] = 0xee
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment

'bytes' object does not support item assignment
```

