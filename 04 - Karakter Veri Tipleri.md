# String İşlemleri

- Tek tırnak veya çift tırnak ile tanımlanabilir.
- Birden fazla satırda tanımlama yapılacaksa üç tırnakla tanımlama yapılabilir.
- Kaçış karakteri (\\)
- White Space : Boşluk karakterleri : " ", "\n", "\t"

## String Operatörleri

- (+) String birleştirme 
- (*) String çoğaltma
- (in) String içinde belli bir kelimenin olup olmadığına bakma
- (not in) in yapısının tersi

## Gömülü String Fonksiyonları - 1

- `chr()` - string to int (ascii and unicode)
- `ord()` - int ot string (ascii and unicode)
- `len()` - Karakter boyutunu verir.
- `str()` - Objeyi string değere çevirir.

## Index İşlemleri

- String yapıları karakter dizileri olduklarından, diziler gibi index işlemleri yapılabilir.

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

- `s.capitalize()`    : Verilen stringin baş harfini büyültür, diğerlerini küçültür.
- `s.lower()`         : Tüm harfleri küçültür.
- `s.upper()`         : Tüm harfleri büyültür.
- `s.swapcase()`      : Küçüklük ve büyüklük durumunu tersine çevirir. 
- `s.title()`         : Her kelimenin baş harfini büyük harfe, diğerlerini küçük harfe çevirir.

## String İçinde Arama Yapma Fonksiyonları

- `s.count(<sub>[, <start>[, <end>]])`        : Verilen değeri kelime içinde sayar
- `s.endswith(<suffix>[, <start>[, <end>]])`  : True veya False döner
- `s.startswith(<prefix>[, <start>[, <end>]])`: True veya False döner
- `s.find(<sub>[, <start>[, <end>]])`         : Değeri string içinde arar. Bulursa, ilk bulduğu değerin index numarasını verir. Bulamazsa -1 döner.
- `s.index(<sub>[, <start>[, <end>]])`        : Find metoduyla aynı işleve sahiptir. Ama değer bulunamazsa -1 yerine ValueError döner.
- `s.rfind(<sub>[, <start>[, <end>]])`        : Find metodunun tersten aramasını yapar. 
- `s.rindex(<sub>[, <start>[, <end>]])`       : Index metodunun tersten aramasını yapar.

## String Sınıflandırma Fonksiyonları

- `s.isalnum()`       : True veya False döner
- `s.isalpha()`       : True veya False döner
- `s.isdigit()`       : True veya False döner
- `s.isidentifier()`  : Değişken ismine uygun olup olmadığını gösterir. True veya False döner
- `s.islower()`       : True veya False döner
- `s.istitle()`       : True veya False döner
- `s.isupper()`       : True veya False döner
- `s.isprintable()`   : Tüm karakterlerin yazılabilir olup olmadığını gösterir.

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

## String Formatlama Fonksiyonları

- `s.replace(<old>, <new>[, <count>])`  : Verilen değerleri yenisiyle değiştirir. Sayı verilirse sadece o sayı kadarını değiştirir. Aksi halde hepsini değiştirir.
- `s.center(<width>[, <fill>])`         : Verilen sayı kadar alana yaslama yapar
- `s.rjust(<width>[, <fill>])`          : Verilen sayı kadar alana yaslama yapar
- `s.ljust(<width>[, <fill>])`          : Verilen sayı kadar alana yaslama yapar
- `s.strip([<chars>])`                  : Boşluk, \n, \t gibi karakterleri kaldırır.
- `s.lstrip([<chars>])`                 : Boşluk, \n, \t gibi karakterleri kaldırır.
- `s.rstrip([<chars>])`                 : Boşluk, \n, \t gibi karakterleri kaldırır.

## String ve List Arasında Dönüşüm Yapma

- `s.join(<iterable>)`
- `list(<string>)`

```python
>>> ', '.join(['foo', 'bar', 'baz', 'qux'])
'foo, bar, baz, qux'

>>> list('corge')
['c', 'o', 'r', 'g', 'e']

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

- `s.partition(<sep>)`      : Verilen string değerine göre string yapıyı 3 e böler.
- `s.rpartition(<sep>)`     : Partition ile aynı fakat bölmeye sondan başlar. 

```python
>>> 'foo@@bar@@baz'.partition('@@')
('foo', '@@', 'bar@@baz')

>>> 'foo@@bar@@baz'.rpartition('@@')
('foo@@bar', '@@', 'baz')
```

- `s.split(sep=None, maxsplit=-1)`  : Verilen karaktere göre yapıyı böler ve listeye çevirir.
- `s.rsplit(sep=None, maxsplit=-1)` : Verilen karaktere göre yapıyı TERSTEN böler ve listeye çevirir.
- Bu yapılara sep. değeri verilmezse boşluk karakterlerine göre böler
- `s.splitlines([<keepends>])`      : Satır karakterlerine göre bölme işlemi yapar.

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

## Bytes Veri Yapısı

- String ve Bytes arasındaki farklar:
    - String, temelde karakter içerir, Bytes ise byte dizisi içerir.
    - String, insanların okuyabileceği yapıdadır, bytes ise makinenin okuyabileceği yapıdadır.
    - Bytes tipi direk disk üzerinde saklanabilirken, string tipi öncelikli olarak encode edilir, sonra saklanır.
- String >> Bytes : Encode
- Bytes >> String : Decode


- `bytes(<s>, <encoding>)`      : Stringi verilen encoding yapısına göre bytes tipine çevirir. 
- `bytes.fromhex(<s>)`          : Hex yapısından bytes yapısı oluşturur.
- `b.hex()`                     : Bytes tipinin hex karşılığını gösterir.
- `b.decode(<encoding>)`        : Bytes to string (default encoding : utf8)
- `s.encode(<encoding>)`        : String to Bytes (default encoding : utf8)