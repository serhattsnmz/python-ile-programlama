# Python Veri Yapıları

## Değişkenler ve Değişken Tanımlama

- Değişken nedir?
- Değişkenler nasıl tanımlanır?
- Değişken tipleri : 
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
- Değişken isimlendirme kuralları : snake_case, PascalCase, camelCase, _private_tanim, GLOBAL_TANIM
    - Değişken ismi sayı ile başlayamaz
    - Değişken arasında boşluk olamaz
    - Özel karakterler kullanılamaz.
    - Değişkenler, büyük-küçük harf duyarlıdır.
    - Python tarafından reserve edilen özel anahtar kelimeler değişken ismi olarak kullanılamaz. (while, not vs. )
        - Tüm listeye erişmek için : `help("keywords")`
    - Python kütüphanelerinden gelen değerler override edilebilir, bu konuya dikkat edilmesi gerekir, çünkü override edilen değerler eski haline geri getirilemeyecektir. (print, time vs.)
- PEP 8 kurallarına göre : 
    - Fonksiyonlarda ve değişken isimlendirmelerinde : Snake Case
    - Class isimlendirmelerinde : Pascal Case kullanılmalıdır.
- type() fonksiyonu

## Pythonda referanslama arka plan yapısı:

- Python üzerinde tanımlanan her değişkenin bir veri tipi vardır. Fakat python, değişkene farklı veri tiplerinde değerler atanmasına izin verir ve atama yapıldığında arka plandaki veri veri yapısını değiştirir.
- Pythonda her tanımlı şey birer classtır.
- Bir değişken tanımlandığında, öncelikli olarak o veri tipinden bir nesne oluşturulur ve değişken ismi o nesneye referans verilir.
- Değişkenin referans aldığı yer, `id(<degisken>)` fonksiyonu ile öğrenilebilir.

```python
>>> type(300)
<class 'int'>
```

```python
>>> n = 300
>>> id(n)
1743378752
```

<p align="center"><img src="https://files.realpython.com/media/t.2d7bcb9afaaf.png" width="50%" /></p>

```python
>>> m = n
>>> id(m)
1743378752
>>> id(n)
1743378752
```

<p align="center"><img src="https://files.realpython.com/media/t.d368386b8423.png" width="50%" /></p>

```python
>>> m = 400
>>> id(m)
1743378912
>>> id(n)
1743378752
```

<p align="center"><img src="https://files.realpython.com/media/t.d476d91592cd.png" width="50%" /></p>

```python
>>> n = "foo"
>>> id(n)
100584432
```

<p align="center"><img src="https://files.realpython.com/media/t.344ab0b3aa8c.png" width="50%" /></p>

- Değişkenin yaşam döngüsü, değişken bir değere referans olarak atandığında başlar, değerin referansı kalmadığında ise son bulur.
- Bir değişkeni manuel olarak kaldırmak için `del <degisken_adi>` kullanılabilir.

## Python Veri Tipleri

- Integeer (int)
- Float (float)
- Strings (str)
- Boolean (bool)
- Complex Numbers (complex)

```python
>>> 2+3j
(2+3j)
>>> type(2+3j)
<class 'complex'>
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