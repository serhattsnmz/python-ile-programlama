# Python Veri Yapıları

## Değişkenler ve Değişken Tanımlama

- Değişken nedir?
- Değişken tanımlama ve atama operatörü

## Değişken tanımlama tiplerine göre diller : 

- Static-Typed Diller : Compile edildiğinde tipi belirlenen dillerde kullanılır. 
    - Java, C, C++, C#, FORTRAN, Pascal, Scala
- Dynamic-Typed Diller : Runtime durumunda tipi kontrol edilir ve belirlenir.
    - JavaScript, Objective-C, PHP, Python, Ruby
- Strong-Typed Diller : Belirlenen tip üzerinden işlem yapılmasını zorunlu kılar. 
    - Örneğin string olarak tanımlanmış bir değişkenle, int bir veriyi toplayamazsınız.
    - Java, Python, C# vs.
- Weakly-Typed Diller : Değişkenin tipi bellidir, fakat farklı tiplerle işlem yapıldığında hata vermek yerine çevirme işlemi yapılır.
    - Örneğin string bir değer ile int değer toplandığında, int değer string olarak çevrilip birleştirme yapılır. 
    - PHP, Perl

## Değişken isimlendirme kuralları

- Değişken isimlendirme kuralları : snake_case, PascalCase, camelCase, _private_tanim, GLOBAL_TANIM
    - Değişken ismi sayı ile başlayamaz
    - Değişken arasında boşluk olamaz
    - Özel karakterler kullanılamaz. (Sadece `_` kullanılabilir.)
    - Değişkenler, büyük-küçük harf duyarlıdır.
    - Python tarafından reserve edilen özel anahtar kelimeler değişken ismi olarak kullanılamaz. (while, not vs. )
        - Tüm listeye erişmek için : `help("keywords")`
    - Python kütüphanelerinden gelen değerler override edilebilir (ayrıntılar aşağıda).
- PEPs kuralları:
    - Python Enhancement Proposals
    - Python Geliştirme Önerileri
    - Index of PEPs : https://www.python.org/dev/peps/
    - PEP-8 kuralları : https://pep8.org/
- PEP 8 kurallarına göre : 
    - Fonksiyonlarda ve değişken isimlendirmelerinde : Snake Case
    - Class isimlendirmelerinde : Pascal Case kullanılmalıdır.
- `type()` fonksiyonu
- `del` ile değişken silme

> **NOT :** Python dilinde, diğer dillerin aksine built-in değişken-fonksion-class isimlerine herhangi bir değer atanmasında hata alınmaz. Değişken atamalarında built-in isimlendirmelerin kullanılmamasına yazılımcının dikkat etmesi gerekir.
>
> ```python
> >>> str
> <class 'str'>
> >>> str = "serhat"
> >>> str
> 'serhat'
> >>> del str
> >>> str
> <class 'str'>
> 
> >>> print
> <built-in function print>
> >>> print = 10
> >>> print
> 10
> >>> del print
> >>> print
> <built-in function print>
> ```
>
> Bununla birliıkte "keyword"lere herhangi bir atama yapılamaz.
>
> ```python
> >>> True = "serhat"
>   File "<stdin>", line 1
>     True = "serhat"
>     ^
> SyntaxError: cannot assign to True
> 
> >>> continue = "serhat"
>   File "<stdin>", line 1
>     continue = "serhat"
>              ^
> SyntaxError: invalid syntax
> ```
>
> 

## Python Veri Tipleri

- `type()` fonksiyonu

| Text Type:      | `str`                              |
| --------------- | ---------------------------------- |
| Numeric Types:  | `int`, `float`, `complex`          |
| Sequence Types: | `list`, `tuple`, `range`           |
| Mapping Type:   | `dict`                             |
| Set Types:      | `set`, `frozenset`                 |
| Boolean Type:   | `bool`                             |
| Binary Types:   | `bytes`, `bytearray`, `memoryview` |

```python
>>> 2+3j
(2+3j)
>>> type(2+3j)
<class 'complex'>
```

## Chained Assignment

```python
>>> a = b = c = 300
>>> print(a, b, c)
300 300 300
```

## Print() Fonksiyonu

```
print(*objects, sep = 'separator')

objects     - object to the printed. * indicates that there may be more than one object
sep         - objects are separated by sep. Default value: ' '
end         - end is printed at last
file        - must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
```

```python
sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()
```

- Print fonksiyonunda * kullanarak, verilen listenin dönmesi sağlanabilir.

```python
>>> print(*'Python', sep = ".")
P.y.t.h.o.n

>>> a = [1,2,3,4]
>>> print(*a, sep=".")
1.2.3.4
```