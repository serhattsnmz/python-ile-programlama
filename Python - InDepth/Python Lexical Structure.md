# Python Lexical Structure (Python Sözcüksel Yapısı)

## Python Statements (Python İfadeleri)

- İfadeler (Statements) basit olarak, python yorumlayıcısının aldığı ve işlediği talimatlardır.
- Python her bir talimatı tek tek alır, işler ve sonraki talimata geçer.
- Python'da, genellikle her bir satır bir talimata karşılık gelir. Başka bir ifadeyle satır sonu karakteri (`\n`) ifadenin bittiği anlamına gelir.
    - C# gibi dillerde böyle bir durum yoktur, `;` görülene kadar birden fazla satıra tek bir ifade yazılabilir.

```python
>>> print('Hello, World!') 	# 1st statement
Hello, World!

>>> x = [1, 2, 3]			# 2nd statement
>>> print(x[1:2])			# 3rd statement
[2]
```

- REPL kullanırken, işlenen ifadelerin çıktıları konsolda gösterilirken, script dosyalarında böyle bir durum söz konusu değildir.

## Line Continuation (Satır Sürdürme)

- Bazı durumlarda tek bir ifadenin uzunluğu çok büyük olabilir. Böyle bir durumda bu ifadeleri birden fazla satıra bölmek okunuş olarak daha mantıklıdır.

```python
>>> person1_age = 42
>>> person2_age = 16
>>> person3_age = 71

>>> someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)

>>> a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
```

- PEP8 kurallarına göre maximum satır uzunluğunun 72 karakter olaması tavsiye edilmiştir.
    - https://www.python.org/dev/peps/pep-0008/#maximum-line-length
- Normalde python her bir satırı bir ifade olarak kabul eder, fakat bazı durumlarda satır sonu karakterini ifade bitişi olarak algılamaz ve takip eden satırı okumaya devam eder.

### a. Implicit Line Continuation (Kapalı Satır Sürdürme)

- `()`, `[]`, `{}` işaretleri kullanıldığında, bu işaretler kapatılana kadar python, ifade birden fazla satırda yazılmışsa dahi ifadeyi hata vermeden okumaya devam eder. 
- Özellikle iç içe tanımlamalarda bu özellikten yararlanmak okunabilirlik açısından önemlidir.

```python
>>> a = [
...     [1, 2, 3, 4, 5],
...     [6, 7, 8, 9, 10],
...     [11, 12, 13, 14, 15],
...     [16, 17, 18, 19, 20],
...     [21, 22, 23, 24, 25]
... ]

>>> a
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
```

- Birden fazla deyim içeren ifadeler, gruplama parantezi kullanılarak birden fazla satırda yazılabilir.

```python
>>> someone_is_of_working_age = (
...     (person1_age >= 18 and person1_age <= 65)
...     or (person2_age >= 18 and person2_age <= 65)
...     or (person3_age >= 18 and person3_age <= 65)
... )

>>> someone_is_of_working_age
True
```

### b. Explicit Line Continuation (Açık Satır Sürdürme)

- Normalde Python satır sonu karakterini (`\n`) ifade bitişi olarak görür ve ifade tamamlanmamışsa `SyntaxError` hatası döner.

```python
>>> s =
  File "<stdin>", line 1
    s =
      ^
SyntaxError: invalid syntax

>>> x = 1 + 2 +
  File "<stdin>", line 1
    x = 1 + 2 +
              ^
SyntaxError: invalid syntax
```

- Açık satır sürdürme, satır sonu karakterini kaçış karakteri (`\`) kullanarak etkisiz hale getirmeyle oluşturulur.

```python
>>> s = \
... 'Hello, World!'
>>> s
'Hello, World!'

>>> x = 1 + 2 \
...     + 3 + 4 \
...     + 5 + 6
>>> x
21
```

- Burada unutulmaması gereken durum, kaçış karakterinden sonra satır sonu karakterinden başka herhangi bir karakter getirilmemesidir. Aksi durumda kaçış karakteri hemen sonrasında yazılan ifade için kaçış belirtir ve satır sonu karakteri etkili kalmaya devam eder.

```python
>>> # there is empty space after \
>>> s = \ 
  File "<stdin>", line 1
    s = \
         ^
SyntaxError: unexpected character after line continuation character
```

## Multiple Statements Per Line

- Bir satıra birden fazla ifade yazma işlemidir.
- Her ifade noktalı virgül (`;`) işaretiyle ayrılır. 

```python
>>> x = 1; y = 2; z = 3
>>> print(x); print(y); print(z)
1
2
3
```

- PEP8 kurallarına göre tavsiye edilmez. Sadece gerçekten okumayı kolaylaştıracak noktalarda kullanılması gerekir.
- Çoğu durumda birden fazla ifadeyi tek satırda yazmanın daha Pythonic yöntemleri vardır.

```python
>>> x, y, z = 1, 2, 3
>>> print(x, y, z, sep='\n')
1
2
3
```

> If you find your code has multiple statements on a line, there is probably a more Pythonic way to write it. But again, if you think it’s appropriate or enhances readability, you should feel free to do it.

## Comment

- Pythonda diyez (`#`) işaretiyle yorumlar yazılabilir. Python yorumlayıcısı diyez işaretini gördüğünde, işaretten sonra satır sonuna kadar olan kısmı okumaz ve işlem yapmaz.

```python
>>> a = ['foo', 'bar', 'baz']  # I am a comment.
>>> a
['foo', 'bar', 'baz']
```

- String ifadenin içindeki diyez işareti yorum anlamı taşımaz.

```python
>>> a = 'foobar # I am *not* a comment.'
>>> a
'foobar # I am *not* a comment.'
```

- Yorumlar, satır sürdürme ifadeleri içinde de yazılabilir.

```python
>>> x = (1 + 2           # I am a comment.
...      + 3 + 4         # Me too.
...      + 5 + 6)

>>> a = [
...     'foo', 'bar',    # Me three.
...     'baz', 'qux'
... ]
```

- Kaçış karakteri ile yapılan satır sürdürmelerinde, son ifadenin kaçış karakteri olması gerektiğinden yorum satırları hata verir.

```python
>>> x = 1 + 2 + \   # I wish to be comment, but I'm not.
SyntaxError: unexpected character after line continuation character
```

- Diğer dillerin aksine, Python'da birden fazla satır için özelleşmiş yorum düzenleyicisi yoktur. Böyle durumlarda her satırın başına diyez işareti getirilmelidir.

```python
>>> # Initialize value for radius of circle.
>>> #
>>> # Then calculate the area of the circle
>>> # and display the result to the console.
```

- Python'da birden fazla satır için yorum satırı bulunmamasına karşılık, özellikle üç tırnak (`"""`) ile yazılan string ifadeler yorum olarak kullanılabilir. 
    - Özellikle "docstring" (bkz: Pythonda Döküman Yazma Kuralları notu) yazarken bu ifade kullanılır.
    - PEP8 kurallarına göre docstring yazımı ve bunun için üç tırnak kullanımı tavsiye edilir.

```python
"""Initialize value for radius of circle.

Then calculate the area of the circle
and display the result to the console.
"""

pi = 3.1415926536
r = 12.35

area = pi * (r ** 2)

print('The area of a circle with radius', r, 'is', area)
```

