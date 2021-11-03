# Koleksiyon Veri Tipleri - Tuples

- Listelere benzer olarak :
    - Sıralı yapıdadırlar.
    - Herhangi bir objeyi alabilirler.
    - İndexlenebilir ve slice edilebilirler.
    - İç içe yapıda yazılabilirler.

- Listelerden farklı olarak :
    - Tuplelar, parantezler içinde tanımlanır. (Parentez kullanımı zorunlu değildir.)
    - Immutable yapıdadırlar.
    - Ekleme, çıkarma veya değiştirme işlemleri yapılamaz.

```python
>>> t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
>>> t[2] = 'Bark!'
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t[2] = 'Bark!'
TypeError: 'tuple' object does not support item assignment
```

- Listeler gibi slice işlemleri yapılabilir.

```python
>>> t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

>>> t[0]
'foo'
>>> t[-1]
'corge'
>>> t[1::2]
('bar', 'qux', 'corge')
>>> t[::-1]
('corge', 'quux', 'qux', 'baz', 'bar', 'foo')
```

## Listeler yerine neden tuple kullanılır?

- İçerdiği veri sayısı büyüdüğünde, tuple manipülasyon işlemleri listeden daha hızlıdır.
- Bazı durumlarda datanın modifiye edilmemesini isteriz. Bu gibi durumlarda tuplelar listeler yerine kullanılır.
- Dictionary yapılarında, en azından bir tane immutable tanımlayıcı gerektiğinden, listeler yerine tuple kullanılır.
- Fonksiyonlar içinde return işlemlerinde, birden fazla sonuç çıkarılacaksa, yazım kolaylığı ve değiştirilememesi açısından, daha çok tuple kullanılır. 

```python
>>> a = 'foo'
>>> b = 42
>>> a, 3.14159, b
('foo', 3.14159, 42)

def example(variable):
    result = variable == True
    return result, variable
```

## Tuple Kullanım Özellikleri

- NOT: Tek elemanlı tuple tanımlanırken, yanında virgül kullanılmalıdır. Aksi halde tuple olarak algılanmaz!

```python
>>> t = ()
>>> type(t)
<class 'tuple'>

>>> t = (1, 2)
>>> type(t)
<class 'tuple'>

>>> t = (2)
>>> type(t)
<class 'int'>

>>> t = (2,)
>>> type(t)
<class 'tuple'>
```

- Tuple elemanları aynı anda birden fazla değişkene atanabilir. (Unpacking)
    - Atanacak değişken sayısının tuple eleman sayısına eşit olması gerekir, aksi halde `ValueError` hatası döner.

```python
# This is -PACKING-
>>> t = 1, 'deneme', True
>>> t
(1, 'deneme', True)

# This is -UNPACKING-
>>> a, s, d = t
>>> a
1
>>> s
'deneme'
>>> d
True

# Define variables with Packing & Unpacking 
>>> x1, x2, x3 = 4, 5, 6
>>> x1, x2, x3
(4, 5, 6)
```

```python
>>> t = ('foo', 'bar', 'baz', 'qux')

>>> (s1, s2, s3) = t
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    (s1, s2, s3) = t
ValueError: too many values to unpack (expected 3)

>>> (s1, s2, s3, s4, s5) = t
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    (s1, s2, s3, s4, s5) = t
ValueError: not enough values to unpack (expected 5, got 4)
```

- Tuple kullanarak veri değişim işlemleri kolaylıkla yapılabilir.

```python
# Normal veri değişimi (diğer dillerde)
>>> a = 'foo'
>>> b = 'bar'
>>> a, b
('foo', 'bar')

>>> temp = a
>>> a = b
>>> b = temp

>>> a, b
('bar', 'foo')
```

```python
# Pythonda veri değişimi
>>> a = 'foo'
>>> b = 'bar'
>>> a, b
('foo', 'bar')

>>> a, b = b, a

>>> a, b
('bar', 'foo')
```

## Tuple Operatörleri

- `+` : Tuple birleştirme 
- `*` : Tuple çoğaltma

```python
>>> a = (1,2,3)
>>> id(a)
1828289445824

>>> a += (3,4,5)
>>> a
(1, 2, 3, 3, 4, 5)
>>> id(a)
1828300410688

>>> a *= 2
>>> a
(1, 2, 3, 3, 4, 5, 1, 2, 3, 3, 4, 5)
>>> id(a)
1828284063952
```

> NOT : Tuple veri tipip immutable olduğundan, birleştirme ve çoğaltma işlemleri yapıldığında oluşan değer, orjinal değerden farklı bir id değerine sahip olur. Basit olarak eski değişken silinmiş, yenisi oluşturulmuştur. List veri tipi için böyle bir durum geçerli değildir, çünkü list veri tipi mutable yapısındadır.
>
> ```python
> >>> a = [1,2,3]
> >>> id(a)
> 1828307318144
> >>> a += [3,4,5]
> >>> id(a)
> 1828307318144
> >>> a *= 2
> >>> id(a)
> 1828307318144
> ```

- `in` : Tuple içinde belli bir elamanın olup olmadığına bakma
- `not in` :  in yapısının tersi

```python
>>> a = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

>>> 'qux' in a
True
>>> 'thud' not in a
True
```

## Tuple Foksiyonları

- `t.index(<obj>)`  : Verilen ifadenin ilk yerinin index numarasını döndürür. Bulamazsa ValueError döner.

```python
>>> t = (1,2,3,3,4,4,4)

>>> t.index(4)
4

>>> t.index(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple

tuple.index(x): x not in tuple
```

- `t.count(<obj>)`  : Verilen objeden kaç tane bulunduğunu söyler. Bulamazsa 0 döner. Boş kullanılmaz.

```python
>>> t = (1,2,3,3,4,4,4)
>>> t.count(4)
3

>>> t.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: count() takes exactly one argument (0 given)

count() takes exactly one argument (0 given)
```