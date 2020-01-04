# Koleksiyon Veri Tipleri - Liste

- Listeler sıralıdır.
    - Ordered Collection olarak tanımlanır.
    - Elemanlar aynı olsa bile, sıralamanın değişmesi veriyi farklı kılar.

```python
>>> [1, 2, 3, 4] == [4, 1, 3, 2]
False
```

- Bir liste her türlü objeyi tutabilir.
    - Python listeleri fonksiyonları, sınıfları, modülleri de tutabilir.
    - Özellikle fonksiyonları tutması, işlemleri hızlandırması açısından çok önemli bir özelliktir.

```python
>>> a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
```

```python
>>> int
<class 'int'>

>>> len
<built-in function len>
>>> def foo():
...     pass
...

>>> foo
<function foo at 0x035B9030>

>>> import math
>>> math
<module 'math' (built-in)>

>>> a = [int, len, foo, math]
>>> a
[<class 'int'>, <built-in function len>, <function foo at 0x02CA2618>,
<module 'math' (built-in)>]
```

- Pythonda listelerin belli bir sınırı yoktur. Memory izin verdiği kadar obje tutabilir.
- Liste elemanları unique olmak zorunda değillerdir.
- Indexler üzerinden bir elamana ulaşılabilir.

<p align="center"><img src="https://files.realpython.com/media/t.c11ea56e8ca2.png" width="50%" /></p>

- Index işlemleri string işlemlerindekiyle aynıdır.
    - Tek fark, içerikleri birebir aynı olsa bile, üretilen yeni bir listedir ve eskisiyle aynı değildir.
    - Ayrıca string işlemlerinde tek bir öğe değiştirilemezken, listelerde değiştirilebilir.

```python
>>> s = 'foobar'
>>> s[:]
'foobar'
>>> s[:] is s
True

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a[2] = 10
>>> a[-1] = 20
>>> a
['foo', 'bar', 10, 'qux', 'quux', 20]
```

```python
>>> s = 'foobarbaz'
>>> s[2] = 'x'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> del a[3]
>>> a
['foo', 'bar', 'baz', 'quux', 'corge']
```

- Listeler istenildiği kadar iç içe yazılabilir.

```python
>>> x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
>>> x[1][1][1]
'ddd'
```

- Listeler mutable'dır.
    - Immutable : Oluşturulduktan sonra İÇERİĞİ değiştirilemeyen yapılardır. String, int, float vs örnek verilebilir.
    - Mutable : Oluşturulduktan sonra İÇERİĞİ değiştirilebilir, ekleme yapılabilir, silme yapılabilir, taşınabilir.

```python
# Immutable
>>> exp = "serhat"
>>> id(exp)
97196128

>>> exp += " sönmez"
>>> id(exp)
26071968

# Mutable
>>> l = [1,2]
>>> id(l)
86088280

>>> l.append(3)
>>> id(l)
86088280
```

- Listeler dinamiktir.
    - Listelere istenildiği kadar eleman eklenip çıkarılabilir.
    - Ekleme ve çıkarma işlemleri listenin idsini değiştirmez.

## List Operatörleri

- (+)       List birleştirme 
- (*)       List çoğaltma
- (in)      List içinde belli bir kelimenin olup olmadığına bakma
- (not in)  in yapısının tersi

## List Fonksiyonları

- len()     Listenin eleman sayısını verir
- max()     Listenin en büyük elemanını verir. String değerler varsa unicode değerlerinin toplamına göre işlem yapar.
- min()     Listenin en küçük elemanını verir. String değerler varsa unicode değerlerinin toplamına göre işlem yapar.

## Liste İşlemleri

- Listenin tek bir elemanını değiştirme
- Listenin birden fazla elamanını değiştirme
    - Değiştirilecek eleman sayısı ile yeni eleman sayısı aynı olmak zorunda değildir.

```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
>>> a
['foo', 1.1, 2.2, 3.3, 4.4, 5.5, 'quux', 'corge']

>>> a[1:6] = ['Bark!']
>>> a
['foo', 'Bark!', 'quux', 'corge']

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a[1:5] = []
>>> a
['foo', 'corge']

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> del a[1:5]
>>> a
['foo', 'corge']
```

- Eğer bir eleman birden fazla eleman ile değiştirilecekse, yine aralık vermeyi unutmamak gerekir.

```python
>>> a = [1, 2, 3]
>>> a[1] = [2.1, 2.2, 2.3]
>>> a
[1, [2.1, 2.2, 2.3], 3]

>>> a = [1, 2, 7, 8]
>>> a[2:2] = [3, 4, 5, 6]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
```

- Listenin bir elemanını silme

```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> del a[3]
>>> a
['foo', 'bar', 'baz', 'quux', 'corge']
```

- Listenin başına veya sonrasına yeni bir liste ekleme

```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a += ['grault', 'garply']
>>> a
['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a = [10, 20] + a
>>> a
[10, 20, 'foo', 'bar', 'baz', 'qux', 'quux', 'corge']
```

- `a.append(<obj>)`         : Listeye eleman ekler.
- `a.extend(<iterable>)`    : Listeye yeni bir liste ekler. += gibi davranır.
- `a.insert(<index>, <obj>)`: Listenin belli bir alanına eleman ekler.

```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a.insert(3, 3.14159)
>>> a
['foo', 'bar', 'baz', 3.14159, 'qux', 'quux', 'corge']
```

- `a.remove(<obj>)`         : Listenin içinden verilen elemanı kaldırır. 
    - Eğer eleman birden fazla ise sadece ilk bulduğunu kaldırır. 
    - Eleman bulamaz ise ValueError hatası verir.
- `a.pop(index=-1)`         : Listenin içinden verilen index numarasındaki elemanı kaldırır. 
    - İndex verilmezse son öğreyi kaldırır.
    - Eğer boş listeden eleman kaldırılmak istenirse veya olmayan index verilirse, IndexError hatası verir.