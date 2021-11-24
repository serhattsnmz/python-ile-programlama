# Diğer Veri Tipleri

## Boolean Veri Tipi

* `True` ve `False` olmak üzere iki değeri vardır.

```python
>>> type(False)
<class 'bool'>
>>> type(True)
<class 'bool'>
```

- Python dilinde boolean ifadeler sayısal olarak `1` ve `0`'a tekabül eder. Sayısal ifadelerle yapılan tüm işlemler boolean ifadeler için de geçerlidir.

```python
>>> True == 1
True
>>> False == 0
True
>>> True + (False / True)
1.0
```

- Boolean ifadelerin sayısal olarak kabul edilmesi bazı durumlarda işleri kolaylaştırabilir:

```python
>>> example = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra."
>>> contains_t = ["t" in item for item in example.split(" ")]
>>> contains_t
[False, False, False, True, True, True, False, True, False, True]
>>> sum(contains_t)
5
```

## Truthy ve Falsy İfadeleri

- Bu ifadeler dışında python bazı durumları `False` olarak algılar. Bu durumlar:
    - False
    - Tüm sayısal 0 ifadeleri (0, 0.0, 0.0+0.0j)
    - Boş string ifadesi
    - Data objelerinin boş halleri ({}, [], ())
    - None ifadesi

- Bunlar dışında kalan tüm ifadeler python tarafından `True` olarak algılanır.

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
## Kıyaslama Operatörleri

- (<) Küçüktür anlamına gelir
- (>) Büyüktür anlamına gelir
- (<=) Küçük eşittir anlamına gelir (ya küçük olacak ya da eşit)
- (>=) Büyük eşittir anlamına gelir (ya büyük olacak ya da eşit)
- (==) Eşittir anlamına gelir
- (!=) Eşit değildir anlamına gelir
- (is) Değer ve ID eşitliği manasına gelir
- (in) Mevcut anlamına gelir.

## Mantıksal Operatörler

- (and) Türkçedeki ve bağlacıdır
- (or) Türkçedeki veya bağlacıdır
- (not) Koda olumsuzluk katar

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

## Zincirleme Karşılaştırmalar

- Zincirleme karşılaştırmalarda, ortadaki ifade bir kere çalışır. And veya Or gibi ifadelerle ayrılan karşılaştırmalarda ise, ortadaki değer iki kez çalıştırılır. Ortadaki fonksiyonun data işlemi yaptığı durumlarda bu durum göz önünde bulundurulmalıdır.

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