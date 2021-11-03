# Everything is "First Class"

* Pythonda tanımlanan herşey öncelikle class'tır.
* `type()` ve `isinstance()` fonksiyonları

```python
>>> a = 10
>>> type(a)
<class 'int'>
>>> isinstance(a, int)
True

>>> s = "Hello World!"
>>> type(s)
<class 'str'>
>>> isinstance(s, str)
True

>>> L = [1, 2, 3]
>>> type(L)
<class 'list'>>>> def my_func(x)

>>> def my_func(x)
...    x = 89
>>> type(my_func)
<class 'function'>
```

# Mutable vs. Immutable Objects

- Python dilinde iki çeşit obje türü vardır:
- `Mutable`
    - list, dict, set, byte array, user-defined classes
    - Oluşturulduktan sonra içeriği değiştirilebilen objelerdir.
    - İçeriği değiştirildiğinde Object Identity değeri değişmez, referansladığı value değeri değişir.
- `Immutable`
    - int, float, long, complex, string tuple, bool
    - Oluşturulduktan sonra içeriği değiştirilemeyen objelerdir.
    - Immutable objelere genenllikle yeni bir atama yapılabilir fakat bu atama değişkenin Object Identity değerini değiştirir. Basit olarak eski değişken silinip tekrar oluşturulur.
    - Bu sebepten ötürü, immutable objelerde değişim işlemleri yapmak, mutable objelerde değişim işlemleri yapmaktan daha fazla kaynak harcar.
- `id()` fonksiyonu ve `is` - `is not` operatörleri değişkenlerin **Object Identity (Memory Address)** değerlerini karşılaştırmak için kullanılabilir.

```python
>>> a = 89
>>> id(a)
4434330504

>>> a = 89 + 1
>>> id(a)
4430689552  # this is different from before!

>>> L = [1, 2, 3]
>>> id(L)
4430688016

>>> L += [4]
>>> id(L)
4430688016    # this is the same as before! 
```

- Aynı mutable değere referans verilen iki değişkenden biri değiştirildiğinde diğeri de değişir. 
    - Bu işleme `aliasing` denir.
    - Immutable değerler için aynı durum söz konusu değildir.

```python
# immutable string
>>> s1 = "hello world"
>>> s2 = s1
>>> s1 += " test"
>>> s1
'hello world test'
>>> s2
'hello world'

# immutable integeer
>>> a = 10
>>> b = a
>>> a += 1
>>> a
11
>>> b
10

# mutable list
>>> a = [1,2,3]
>>> b = a 			# aliasing
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]

# mutable dict
>>> a = {1:1, 2:2}
>>> b = a			# aliasing
>>> a.update({3:3})
>>> a
{1: 1, 2: 2, 3: 3}
>>> b
{1: 1, 2: 2, 3: 3}
```

- Class'lardan türetilen nesneler (Singleton Patern uygulanmamışsa) her zaman birbirinden farklı olarak oluşturulur.

```python
>>> class Foo:
...     pass
...

>>> bar = Foo()
>>> baz = Foo()

>>> id(bar)
140730612513248
>>> id(baz)
140730612513320
```

# Python Referancing Background

- Python üzerinde tanımlanan her değişkenin bir veri tipi vardır. Fakat python, değişkene farklı veri tiplerinde değerler atanmasına izin verir ve atama yapıldığında arka plandaki veri veri yapısını değiştirir.
- Bir değişken tanımlandığında, öncelikli olarak o veri tipinden bir nesne oluşturulur ve değişken ismi o nesneye referans verilir.
- Object Identity : Değişkenin referans aldığı yer, `id(<degisken>)` fonksiyonu ile öğrenilebilir.

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

# Memory Optimization in Python Implementation

- Python her yeni değişken tanımlamasında yeni bir obje üretir.

```python
>>> a = "hello world!"
>>> b = "hello world!"
>>> a is b
False

>>> a = 499
>>> b = 499
>>> a is b
False

>>> a = [1,2,3]
>>> b = [1,2,3]
>>> a is b
False
```

- Bununla birlikte Python dili memory optimizasyonu için bazı durumarda istisna yapar:
    - Kısa ve karmaşık olmayan string değerler
    - [-5, 256] aralığındaki integer değerler
    - Boş immutable değerer (örn: tuples)

## Caching Small Integer Values

* Pythonda her tanımlanan değişlenin farklı bir id değeri vardır.

```python
>>> id(300)
1828300156880

>>> a = 300
>>> b = 300

>>> id(a)
1828300156688
>>> id(b)
1828291578352
```

- Bununla birlikte python, optimizasyon amacıyla ilk çalıştırıldığında `[-5, 256]` aralığını cache'ler ve atamaları bu cache değerlerine referans vererek yapar.

```python
>>> id(30)
1828197985488

>>> a = 30
>>> b = 30

>>> id(a)
1828197985488
>>> id(b)
1828197985488
```

## String Interning with `intern()` Function

- Normalde RAM'de farklı yerlerde tutulan string değişkenler, `intern()` fonksiyonu kullanılarak RAM'de aynı yerde tutulması sağlanabilir.
- Burdaki temel amaç, çok kullanılan program değişkenlerinin RAM'de kapladığı alanı azaltmaktır. 

```python
>>> from sys import intern

>>> s1 = 'foo!'
>>> s2 = 'foo!'
>>> s1 is s2
False

>>> s1 = intern('foo!')
>>> s2 = intern('foo!')
>>> s1 is s2
True
```

<center><img src="..\statics\01.png" style="zoom:50%;" /></center>

<center><img src="..\statics\02.png" style="zoom:50%;" /></center>

- Dil işleme gibi yüksek sayıda ama tekrarlayan öğeler içeren yapılarda kullanılması, RAM optimizasyonunu fazlasıyla düşürür.

```python
import guppy
import nltk

hp = guppy.hpy()
hp.setrelheap()

hamlet = nltk.corpus.shakespeare.words('hamlet.xml')
print hp.heap()

hamlet = [intern(wrd) for wrd in nltk.corpus.shakespeare.words('hamlet.xml')]
print hp.heap()

# As you can see, we drastically reduced the number of allocated string objects from 31,166 to 4,529 and divided by 6.5 the memory occupied by the strings!

Partition of a set of 31187 objects. Total size = 1725752 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  31166 100  1394864  81   1394864  81 str
...

Partition of a set of 4555 objects. Total size = 547840 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0      4   0   328224  60    328224  60 list
     1   4529  99   215776  39    544000  99 str
...
```

- `intern()` function pseudo Python code:

```python
interned = None

def intern(string):
    if string is None or not type(string) is str:
        raise TypeError

    if string.is_interned:
        return string

    if interned is None:
        global interned
        interned = {}

    t = interned.get(string)
    if t is not None:
        return t

    interned[string] = string
    string.is_intern
```

## Native String Interning

- Python'da tanımlanan string ifadeler basit ve kısaysa, memory üzerinde farklı yerlere kaydedilmez, değişkenler aynı değere referans verir.

```python
>>> s1 = 'hello'
>>> s2 = 'hello'

>>> id(s1), id(s2)
(4454725888, 4454725888)
>>> s1 == s2
True
>>> s1 is s2
True

>>> s3 = 'hello, world!'
>>> s4 = 'hello, world!'

>>> id(s3), id(s4)
(4454721608, 4454721664)
>>> s3 == s4
True
>>> s3 is s4
False
```

- String interning test

```python
>>> 'foo' is 'foo'
True
>>> 'foo!' is 'foo!'
False
>>> 'foo' + 'bar' is 'foobar'
True
>>> ''.join(['f']) is ''.join(['f'])
True
>>> ''.join(['f', 'o', 'o']) is ''.join(['f', 'o', 'o'])
False
>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
>>> 'foooooooooooooooooooooooooooooo' is 'foooooooooooooooooooooooooooooo'
True
```
