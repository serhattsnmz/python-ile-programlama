# Koşul İfadeleri

- Girintili yapıyla kod bloğu oluşturulması
    - Girintili ifadede tab veya boşluk kullanılması
    - Girinti boşluk değerinin default 4 alınması veya değiştirilmesi
    - "Off-side rule" languages : https://en.wikipedia.org/wiki/Off-side_rule#Off-side_rule_languages

- Koşul ifadesi söz dizimi:
    - `<expr>` : Boolean değerdedir. Koşulu belirtir. (True, False, Truly, Falsy olabilir.)
    - `<statement>` : Koşul ifadesi gerçekleşirse çalışacak kod bloğunu ifade eder.

```python
if <expr>:
    <statement>
```

```python
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
else:
    <statement(s)>
```

- `pass` keyword ifadesi

```python
>>> if True:
>>> print('foo')

  File "foo.py", line 3
    print('foo')
        ^
IndentationError: expected an indented block
```

```python
>>> if True:
>>>     pass

>>> print('foo')
foo
```

- Expression olarak `True`, `False`, `Truly`, `Falsy` ifadelerin kullanılması

## Short-Circuit Evaluation

- Koşul zincirlerinde okuma sırayla yapılır. Herhangi bir koşul sağlanırsa, o koşulun kod bloğu işlenir ve diğer koşul ifadelerine bakılmaz.

```python
>>> var  # Not defined
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    var
NameError: name 'var' is not defined

>>> if 'a' in 'bar':
...     print('foo')
... elif 1/0:
...     print("This won't happen")
... elif var:
...     print("This won't either")
...
foo
```

## Error Handling Best Practice

```python
person = {
    "name" 		: "Joe",
    "age" 		: 30,
    "children" 	: ["Ralph", "Betty", "Joey"],

    "addressess": [
        {
            "address" : "928 Illinois Avenue",
            "zipCode" : 67674
        }
    ]
}

# Method 1
if "addressess" in person:
    if len(person["addressess"]) > 0:
        if "zipCode" in person["addressess"][0]:
            return person["addressess"][0]["zipCode"]
        else:
            return False, "Address of person doesn't have zipcode!"
    else:
        return False, "Person doesn't have enough address!"
else:
    return False, "Addresses not found!"
    
# Method 2
if not "addressess" in person: 
    return False, "Addresses not found!"

if len(person["addressess"]) == 0: 
    return False, "Person doesn't have enough address!"

if not "zipCode" in person["addressess"][0]:
    return False, "Address of person doesn't have zipcode!"

return True, person["addressess"][0]["zipCode"]
    
# Method 3
if not person.get("addressess"): # Falsy usage
    return False, "Addresses not found!"

if len(person["addressess"]) == 0: 
    return False, "Person doesn't have enough address!"

if not person["addressess"][0].get("zipCode"): # Falsy usage
    return False, "Address of person doesn't have zipcode!"

return True, person["addressess"][0]["zipCode"]
```

## One-Line if Statements

```python
if <expr>:
    <statement>

if <expr>: <statement>

if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
```

```python
>>> x = 3
>>> if x == 1: print('foo'); print('bar'); print('baz')
... elif x == 2: print('qux'); print('quux')
... else: print('corge'); print('grault')
...
corge
grault
```

## Conditional Expressions (Python’s Ternary Operator)

```python
<expr1> if <conditional_expr> else <expr2>
```

```python
>>> if a > b:
...     m = a
... else:
...     m = b

>>> m = a if a > b else b
```

- Tek sıra if ifadeleri kullanılırken, işlem önceliğine dikkat edilmelidir.
- Uzun ifadelerin içinde tek sıra if ifadeleri kullanılacaksa, parantez ile kullanmak okunurluk açısından daha iyidir.

```python
>>> x = y = 40

>>> z = 1 + x if x > y else y + 2
>>> z
42

>>> z = (1 + x) if x > y else (y + 2)
>>> z
42

>>> z = 1 + (x if x > y else y) + 2
>>> z
43
```

- Tek sıra ifadeleri, ard arda kullanılarak if/elif/else yapısı kurulabilir. 

```python
>>> s = ('foo' if (x == 1) else
...      'bar' if (x == 2) else
...      'baz' if (x == 3) else
...      'qux' if (x == 4) else
...      'quux')
>>> s
'baz'
```

- Normal if yapısında olduğu gibi, tek sıra if yapısında da eğer durum değeri True değilse ifade çalıştırılmaz.

```python
>>> 'foo' if True else 1/0
'foo'
>>> 1/0 if False else 'bar'
'bar'
```

- Ayrıca ifadeler tek tek çalıştırılır.

```python
>>> 1 if True else 2 if 1/0 else 3
1

>>> 1 if False else 2 if 1/0 else 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

division by zero
```