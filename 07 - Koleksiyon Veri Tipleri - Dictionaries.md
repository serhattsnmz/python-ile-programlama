# Koleksiyon Veri Tipleri - Dictionaries (Sözlükler)

- Listelere benzer olarak:
    - Mutable yapıdadırlar
    - Dinamik yapıdadırlar. İstenildiği kadar veri eklenip çıkarılablir.
    - İstenildiği kadar iç içe yazılabilir. Ayrıca dictionary içine liste, liste içine dictionary yazılabilir.

- Listelerden farklı olarak :
    - Liste elemanlarına index yoluyla ulaşılabilir. 
    - Dictionary elemanlarına anahtar vasıtasıyla ulaşılabilir.
    - Dict yapısına index veya olmayan bir key ile ulaşılmaya çalışılırsa, KeyError hatası alınır.

```python
>>> some_dict[1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    some_dict[1]
KeyError: 1

>>> some_dict['Toronto']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    some_dict['Toronto']
KeyError: 'Toronto'
```

- Dict tanımlama iki farklı yöntemle yapılabilir: 

```python
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}

d = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])

d = dict()
```

- Key yapıları için herhangi bir immutable tiple veri kullanılabilir. Int buna dahildir.

```python
>>> d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
>>> d[0]
'a'
>>> d[2]
'c'
```

- Aksi gibi görünse de, dict içindeki objelerin sırası korunaklıdır. Yeni eklenen veriler her zaman sona eklenir. Bu durum python 3.7 ve sonrasında geçerlidir. Aslında 3.6da da bu durum vardır ama 3.6 tanımlamasında bu durum yer almamaktadır.

- Dict yapısı içinde hem keyler hem de valueler farklı obje türlerinden olabilir.

```ptyhon
>>> foo = {42: 'aaa', 2.78: 'bbb', True: 123}

>>> foo[42]
'aaa'
>>> foo[2.78]
'bbb'
>>> foo[True]
123
```

## Dict içine yeni veri ekleme, değiştirme, silme

```python
>>> d = {}

>>> d["exp"] = "deneme"
>>> d
{'exp': 'deneme'}

>>> d.update({"key":"value"})
>>> d
{'exp': 'deneme', 'key': 'value'}

>>> d["key"] = "new value"
>>> d
{'exp': 'deneme', 'key': 'new value'}

>>> del d["exp"]
>>> d
{'key': 'new value'}
```

## İki dict verisini birleştirme

```python
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}

>>> z = {**x, **y}

>>> z
{'c': 4, 'a': 1, 'b': 3}
```

## Key yapısının özellikleri

- Keyler her obje yapısında olabilirler, hatta build-in obj yapısında bile olabilirler

```python
>>> d = {int: 1, float: 2, bool: 3}
>>> d
{<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}
>>> d[float]
2

>>> d = {bin: 1, hex: 2, oct: 3}
>>> d[oct]
3
```

- Dict yapısında keyler yalnız bir kere kullanılabilir. Aynı key ile farklı bir değer eklenmeye çalışıldığında, varolan value değişir.

```python
>>> d = {'key': 'value'}
>>> d.update({"key":"new value"})
>>> d
{'key':'new value'}
```

- Eğer dict yapısı oluşturulurken aynı keyden birden fazla verilirse, son key değeri alınır. 

```python
>>> MLB_team = {
...     'Colorado' : 'Rockies',
...     'Boston'   : 'Red Sox',
...     'Minnesota': 'Timberwolves',
...     'Milwaukee': 'Brewers',
...     'Seattle'  : 'Mariners',
...     'Minnesota': 'Twins'
... }
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
```

- Key yapıları immutable olmak zorundadır.

```python
>>> d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
>>> d[(1,1)]
'a'
>>> d[(2,1)]
'c'

>>> d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
TypeError: unhashable type: 'list'
```

- Buradaki error açıklamasından da anlaşılacağı üzere, aslında key yapısına vermemiz gereken değer immutable olmasından ziyade hashable olmasıdır. Bir verinin hashlenebilmesi için o verinin belirli bir uzunluğa sahip olması gerekmektedir. Mutable veri tiplerinin belirli uzunlukları olmadığından hashlenemezler.

```python
>>> hash('foo')
11132615637596761

>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

## Dict Operatörleri

- (in)      Dict içinde belli bir kelimenin olup olmadığına bakma
- (not in)  in yapısının tersi

NOT : Özellikle KeyError hatalarından kaçınmak için, bir key değerinin öncelikle dict içinde olup olmadığı kontrol edilmelidir.

```python
>>> MLB_team['Toronto']
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    MLB_team['Toronto']
KeyError: 'Toronto'

>>> 'Toronto' in MLB_team and MLB_team['Toronto']
False
```

## Dict Fonksiyonları

- len()     Dict eleman sayısını verir
- max()     Dict en büyük key elemanını verir. String değerler varsa unicode değerlerinin toplamına göre işlem yapar.
- min()     Dict en küçük key elemanını verir. String değerler varsa unicode değerlerinin toplamına göre işlem yapar.

## Build-in Dict Metotları 

- `d.clear()`                   : Dict içeriğini tamamen siler
- `d.get(<key>[, <default>])`   : Verilen key değerine göre value getirir. 
    - Eğer key değeri yoksa, default değer veya None döner.
- `d.items()`                   : Dict elemanlarını tuple listesi olarak döner. 
- `d.keys()`                    : Keyleri liste olarak döner
- `d.values()`                  : Valueleri liste olarak döner
- `d.pop(<key>[, <default>])`   : Verilen key değerini dict içeriğinden çıkarır.
    - Eğer key değeri yoksa, default değeri veya KeyError hatasını verir.
- `d.popitem()`                 : Dict yapısından son elemanı çıkarır. Eğer dict boş ise KeyError döner.
- `d.update(<obj>)`             : Dict yapısına başka bir dict veya key-value pair (tuple listesi) eklemek için kullanılır.
    - Aynı elemanlar varsa güncellenir. 

```python
>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d2 = {'b': 200, 'd': 400}

>>> d1.update(d2)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}

>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update([('b', 200), ('d', 400)])
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}

>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update(b=200, d=400)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
```

## Dict key ve value elemanlarını liste olarak alma

```python
>>> d = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}

>>> d.keys()
dict_keys([0, 1, 2, 3])

>>> d.items()
dict_items([(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')])

>>> d.values()
dict_values(['a', 'a', 'a', 'a'])

>>> [*d.keys()] or list(d.keys())
[0, 1, 2, 3]

>>> [*d.items()] or list(d.items())
[(0, 'a'), (1, 'a'), (2, 'a'), (3, 'a')]

>>> [*d.values()] or list(d.values())
['a', 'a', 'a', 'a']
```