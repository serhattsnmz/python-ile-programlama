# Koşul İfadeleri

## Kıyaslama Operatörleri

- (<) Küçüktür anlamına gelir
- (>) Büyüktür anlamına gelir
- (<=) Küçük eşittir anlamına gelir (ya küçük olacak ya da eşit)
- (>=) Büyük eşittir anlamına gelir (ya büyük olacak ya da eşit)
- (==) Eşittir anlamına gelir
- (!=) Eşit değildir anlamına gelir
- (is) Değer ve ID eşitliği manasına gelir
- (in) Mevcut anlamına gelir ( kümenin içinde olup olmadığını test ederken kullanmıştık)


NOT : Pythonda -5'ten 256'ya kadar olan sayısal değerler array olarak hafızada tanımlı tutulur. Bu sayılarla değişken tanımlandığında aynı değerlere referans verir. Doğal olarak int ifadelerde `is` kullanılması tavsiye edilmez.

Bkz: https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong

Ayrıca uzunluğu 20'den küçük olan string değerlerde birden fazla tanımlandığında aynı yere referans verilir.

```python
>>> a = 10
>>> id(a)
1521998144

>>> b = 10
>>> id(b)
1521998144

>>> c = 9 + 1
>>> id(c)
1521998144

>>> d = 8
>>> d += 2
>>> id(d)
1521998144

>>> k = 345
>>> id(k)
82334704

>>> y = 345
>>> id(y)
82333920

>>> 30 is 20 + 10
True
>>> 300 is 200 + 100
False
```

## Mantıksal Operatörler

- (and) Türkçedeki ve bağlacıdır
- (or) Türkçedeki veya bağlacıdır
- (not) Koda olumsuzluk katar

Bu ifadeler dışında python bazı durumları False olarak algılar. Bu durumlar:

- False
- Tüm sayısal 0 ifadeleri (0, 0.0, 0.0+0.0j)
- Boş string ifadesi
- Data objelerinin boş halleri ({}, [], ())
- None ifadesi

Bunlar dışında kalan tüm ifadeler python tarafından True olarak algılanır.

```python
>>> bool(None)
False
>>> bool("example")
True
>>> bool({})
False
>>> bool([])
False
>>> bool([1])
True
>>> bool(())
False
```

### Short-Circuit Evaluation (Kısa-Devre Değerlendirmesi)

- Mantıksal ifadeler, soldan sağa doğru ilerler. Eğer "en az" diye tabir edilen ifadelerden biriyle karşılaşırsa, sorasını okumaz, sonucu döndürür.
- Birkaç durumda bu yapı tasarımsal bir desen olarak kullanılır. 

**Hataların Engellenmesi**

```python
>>> a = 0
>>> b = 1
>>> (b / a) > 0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    (b / a) > 0
ZeroDivisionError: division by zero

>>> a = 0
>>> b = 2
>>> a != 0 and (b / a) > 0
False

>>> k = a and (b / a)
>>> k
False

>>> a = 1
>>> k = a and (b / a)
>>> k
2.0

>>> k = a and b / a and a / b
>>> k
0.5
```

**Default Value Atanması**

```python
>>> string = 'foo bar'
>>> s = string or '<default_value>'
>>> s
'foo bar'

>>> string = ''
>>> s = string or '<default_value>'
>>> s
'<default_value>'
```

**Zincirleme Karşılaştırmalar**

Zincirleme karşılaştırmalarda, ortadaki ifade bir kere çalışır. And veya Or gibi ifadelerle ayrılan karşılaştırmalarda ise, ortadaki değer iki kez çalıştırılır. Ortadaki fonksiyonun data işlemi yaptığı durumlarda bu durum göz önünde bulundurulmalıdır.

```python
>>> 1 < 2 < 4
True

>>> 1 < 4 < 4
False

>>> def f(deger):
...     print(deger)
...     return deger

>>> 1 < f(2) < 5
2
True

>>> 1 < f(2) and f(2) < 5
2
2
True
```

## Bitwise Operatörler (Sadece bool değerler)

- (<<) Sola bit kaydırır
- (>>) Sağa bit kaydırır
- (&) Türkçedeki ve bağlacıdır (and)
- (|) Türkçedeki veya bağlacıdır (or)
- (^) xor komutudur özel anlamına gelir
- (~) Koda olumsuzluk anlamı (değil anlamı) katar (not)

```python
>>> '0b{:04b}'.format(0b1100 & 0b1010)
'0b1000'
>>> '0b{:04b}'.format(0b1100 | 0b1010)
'0b1110'
>>> '0b{:04b}'.format(0b1100 ^ 0b1010)
'0b0110'
>>> '0b{:04b}'.format(0b1100 >> 2)
'0b0011'
>>> '0b{:04b}'.format(0b0011 << 2)
'0b1100'
```

## If - Elif - Else Yapısı

- Girintili ifadeler ve kod bloğu
- `pass` keyword ifadesi