# Koleksiyon Veri Tipleri - Tuples

- Listelere benzer olarak :
    - Sıralı yapıdadırlar.
    - Herhangi bir objeyi alabilirler.
    - İndexlenebilir ve slice edilebilirler.
    - İç içe yapıda yazılabilirler.

- Listelerden farklı olarak :
    - Tuplelar, parantezler içinde tanımlanır.
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