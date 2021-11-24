# List Comprehension

## Liste oluşturma Yöntemleri

#### 1. Create List with For Loop

```python
>>> squares = []
>>> for i in range(10):
...     squares.append(i * i)
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### 2. Create List With `map()` Function

- `map()` fonksiyonu, bir fonksiyonu bir iterable objenin tüm elemanlarına uygular ve bundan bir generator listesi oluşturur.

```python
>>> numbers = [1,2,3,4,5]

>>> def square(n):
...     return n * n

>>> s = map(square, numbers)
>>> next(s)
1
>>> next(s)
4
>>> list(map(square, numbers))
[1, 4, 9, 16, 25]

>>> list(map(lambda x: x*x, numbers))
[1, 4, 9, 16, 25]
```

#### 3. Using List Comprehension

```python
>>> squares = [i * i for i in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
new_list = [expression for member in iterable]
```

- List comprehension kullanımı 3 elemandan oluşur:
    - `expression` : Elemanlara yapılacak işlemlerin tanımlandığı yerdir.
    - `member` : Iterable değerin teker teker alınan elemanlarını ifade eder.
    - `iterable` : List, set, dict, generator veya benzer tüm itetable objeler olabilir.
- Dictionary yapıları da iterable olarak kullanılabilir.


```python
>>> a = {1:"a", 2:"b", 3:"c"}

>>> [k for k in a]
[1, 2, 3]

>>> [k for k in a.values()]
['a', 'b', 'c']

>>> [k for k in a.items()]
[(1, 'a'), (2, 'b'), (3, 'c')]

>>> [key for key,value in a.items()]
[1, 2, 3]
>>> [value for key,value in a.items()]
['a', 'b', 'c']
```
## Using Conditional Logic

- List comprehension ifadesi içinde kısıtlama yapacak `if` yapısı kullanmayı ifade eder.
- `iterable` ifadesinden hemen sonra kullanılan `if` kısmı filtreleme yapar. `filter()` fonksiyonuna karşılık gelir. Burada `else`  kullanılmaz.

```python
new_list = [expression for member in iterable (if conditional)]
```

```python
>>> sentence = 'the rocket came back from mars'
>>> vowels = [i for i in sentence if i in 'aeiou']
>>> vowels
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
```

- `if/else` yapısı `expression` ifadesinden hemen sonra da kullanılabilir. Bu kullanımda filtreleme yapılmaz, çıktı değerinde değişiklik yapılır. `else` kullanımı zorunludur.

```python
new_list = [expression (if conditional) for member in iterable]
```

```python
>>> numbers = [1,2,3,4,5]

>>> [k for k in numbers]
[1, 2, 3, 4, 5]

>>> [k for k in numbers if k % 2 == 0]
[2, 4]

>>> [k if k % 2 == 0 else "-" for k in numbers]
['-', 2, '-', 4, '-']
```

- Her iki ifade istenilirse birlikte kullanılabilir.

```python
>>> numbers = [1,2,3,4,5]

>>> [k if k % 2 == 0 else "-" for k in numbers if k > 2]
['-', 4, '-']
```

## Set and Dictionary Comprehensions

- Set comprehension, list yapısına benzer. Tek farkı, küme yapısında olduğu için çıktılarda tekrarlayan eleman bulunmaz. 

```python
>>> quote = "life, uh, finds a way"
>>> unique_vowels = {i for i in quote if i in 'aeiou'}
>>> unique_vowels
{'a', 'e', 'u', 'i'}
```

- Dictionary Comprehension da benzer şekilde oluşturulur. Faklı olarak burda key de tanımlamak gerekir.

```python
>>> squares = {i: i * i for i in range(10)}
>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

## Walrus Operator (Assigment Expression) `:=`

- Python 3.8 ve sonrasında kullanılır.
- İfadeler (expression) içinde değişken tanımlamaya yarar. 
- Aynı ifade içinde hem değişkenin tanımlanmasını hem de değer olarak döndürülmesini sağlar.

```
name := expr
```

```python
>>> print(num = 15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'num' is an invalid keyword argument for print()

'num' is an invalid keyword argument for print()

>>> print(num := 15)
15
```

```python
# without walrus op.
val = input("Enter sth: ")
while val != "":
    print("Nice!")
    val = input("Enter sth: ")

# with walrus op.
while val := input("Enter sth: ") != "":
    print("Nice!")
```

```python
>>> import random
>>> def get_weather_data():
...     return random.randrange(90, 110)

>>> hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]

>>> hot_temps
[107, 102, 109, 104, 107, 109, 108, 101, 104]
```

```python
>>> [(i,temp) for i in range(5) if (temp := i * i) > 0]
[(1, 1), (2, 4), (3, 9), (4, 16)]
```

## Nested Comprehensions

```python
>>> cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
>>> temps = {city: [0 for _ in range(7)] for city in cities}
>>> temps
{
    'Austin': [0, 0, 0, 0, 0, 0, 0],
    'Tacoma': [0, 0, 0, 0, 0, 0, 0],
    'Topeka': [0, 0, 0, 0, 0, 0, 0],
    'Sacramento': [0, 0, 0, 0, 0, 0, 0],
    'Charlotte': [0, 0, 0, 0, 0, 0, 0]
}
```

```python
>>> matrix = [[i for i in range(5)] for _ in range(6)]
>>> matrix
[
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]
```

```python
>>> matrix = [
...     [0, 0, 0],
...     [1, 1, 1],
...     [2, 2, 2],
... ]
>>> flat = [num for row in matrix for num in row]
>>> flat
[0, 0, 0, 1, 1, 1, 2, 2, 2]

>>> matrix = [
...     [0, 0, 0],
...     [1, 1, 1],
...     [2, 2, 2],
... ]
>>> flat = []
>>> for row in matrix:
...     for num in row:
...         flat.append(num)
...
>>> flat
[0, 0, 0, 1, 1, 1, 2, 2, 2]
```

## Choose Generators for Large Datasets

- List comprehension kullanılırken, list içinde oluşturulan tüm datalar RAM'de tanımlanır. Küçük data işlemlerinde bu durum pek sıkıntı yaratmazken, büyük datalarda çok fazla RAM harcayacağından performans kaybı yaratır.

```python
>>> sum([i * i for i in range(1000 * 1000 * 100)])
333333328333333350000000
```

- Yukarıdaki örnekte;
    - Öncelikle belirtilen aralıkta bir liste oluşturulur,
    - Sonrasında listenin elemanları tek tek toplanır.
    - Liste oluşturulurken ortalama 4GB RAMde alan kullanılır. (Görev yöneticisi ile bakılabilir.)

```python
>>> sum((i * i for i in range(1000 * 1000 * 100)))
333333328333333350000000
```

- Yukarıdaki örnekte ise;
    - Sayıları çeviren bir generator oluşturulur.
    - `sum()` fonksiyonu teker teker generator üzerinden eleman çekip ekleme işlemi yapar.
    - Çekilen ifadeler sonrasında silindiğinden hafızada yer kaplamaz, sadece toplam hafızada tutulur.
    - RAM kullanımı KB seviyesindedir.

```python
>>> sum(map(lambda i: i*i, range(1000 * 1000 * 100)))
333333328333333350000000
```

- `map()` fonksiyonu da generator ürettiğinden, bir önceki örnek ile aynı yolu izler ve hafızayı daha verimli kullanır.

## Performance Difference

- Listeler RAM'de fazla yer kaplar ama daha hızlı erişimlidir. 
- Generator'lar RAM'de çok az yer kaplar ama daha yavaş erişimlidir. 
- Aşağıdaki örnekte aynı işi yapan list, generator ve map fonksiyonlarının çalışma zamanları gösterilmiştir:

```python
from timeit import timeit
>>> def test1():
...     return sum([i * i for i in range(1000 * 1000 * 100)])
>>> timeit(test1, number = 1)
8.5563449

>>> def test2():
...     return sum((i * i for i in range(1000 * 1000 * 100)))
>>> timeit(test2, number = 1)
9.712445300000013

>>> def test3():
...     return sum(map(lambda i: i*i, range(1000 * 1000 * 100)))
>>> timeit(test3, number = 1)
11.1126698999999
```

