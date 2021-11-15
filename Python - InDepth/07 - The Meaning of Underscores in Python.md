# The Meaning of Underscores in Python

- Python'da tekil `_` ve double (`dunder`) `__` alt çizgi faklı anlamlarda kullanılır.
    - Single Leading Underscore: `_var`
    - Single Trailing Underscore: `var_`
    - Double Leading Underscore: `__var`
    - Double Leading and Trailing Underscore: `__var__`
    - Single Underscore: `_`
- Source : https://pep8.org/#descriptive-naming-styles

## 1. Single Leading Underscore: `_var`

- Tek alt çizgi öneki ile tanımlanan değişken, programcıya bu değişkenin sadece internal amaçla kullanıldığı söyler. Başka bir deyişle, diğer dillerdeki `private` kullanıma karşılık gelir fakat dışarıdan da erişilebilir. Burdaki amaç sadece program yazarken değikenlerin `internal/external` durumunu belirtmektir, teknik olarak diğer değişkenlerden bir farkı yoktur. 
- Bildiğimiz üzere, pythonda public, private veya internal belirteçleri yoktur, class içinde tanımlanan tüm değişken ve fonksiyonlar public'tir.

```python
class Test:
    def __init__(self):
        self.foo = 11         # External property
        self._bar = 23        # Internal property
        
    def external_func(self):  # External function
        return 23

    def _internal_func(self): # Internal function
        return 42
    
    
t = Test()
print(t.foo)
print(t._bar)
print(t.external_func())
print(t._internal_func())

# 11
# 23
# 23
# 42
```

- **NOT**: Bir modül wildcard (`*`) ile import edilirken, içindeki internal değişken ve fonksiyonlar import edilmez. Fakat bir class import edilirse, içindekiler import edilir. Internal değişkenler wildcard kullanmadan import edilebilir. 

```python
## module.py 

def external_func():  # External function
    return 23

def _internal_func(): # Internal function
    return 42

class Test:
    def __init__(self):
        self.foo = 11         # External property
        self._bar = 23        # Internal property
        
    def external_func(self):  # External function
        return 23

    def _internal_func(self): # Internal function
        return 42
```

```python
## main.py

from module import *
from module import Test

t = Test()
print(t.foo)
print(t._bar)
print(t.external_func())
print(t._internal_func())

print(external_func())
print(_internal_func())

# 11
# 23
# 23
# 42
# 23
# Traceback (most recent call last):
#   File "C:\Users\serhat\Desktop\python-test\test.py", line 11, in <module>
#     print(_internal_func())
# NameError: name '_internal_func' is not defined
```

## 2. Single Trailing Underscore: `var_`

- Python keyword'leri değişken ismi olarak kullanılamaz, kullanılırsa hata verir. Bu keyword'lere benzer değişkenler tanımlanmak isteniyorsa sonuna `_` eklenir.

```python
>>> def make_object(name, class):
SyntaxError: "invalid syntax"

>>> def make_object(name, class_):
...     pass
```

## 3. Double Leading Underscore: `__var`

- `Dunders` : Python programcıları arasında çift alt çizgiyi tanımlamak amacıyla kullanılan bir kısaltmadır. Böyle bir kısaltmaya ihtiyaç duyulmasının nedeni, python dilinde çift alt çizginin çok fazla kullanılıyor olmasıdır.
    - https://nedbatchelder.com/blog/200605/dunder.html
- Başa ve sona eklenen tekil `_` karakterleri teknik olarak normal değişken tanımlamaktan farklı bir anlam içermezler. Fakat önek olarak gelen çift `__` karakteri için durum farklıdır.
- `Name Mangling (İsim Bozma)` : Class içinde dunders ile başlayan değişkenler, değişken isminin başına class ismini alıp hafızaya kaydedilir. Class veya nesne üzerinden değişkene erişilmeye çalışıldığında, tanımlanan isim yerine başına class ismi getirilerek çağırılırlar.(`_<class_name>__<variable_name>`)
    - Class içinde değişken kullanılırken bu durum geçerli değildir. Normal tanımlandığı şekilde kullanılabilir.
    - Ayrıca class dışında tanımlanan değişkenlerde de herhangi bir isim değişikliği yapılmaz.

```python
>>> __test = "serhat"

>>> __test
'serhat'

>>> class test:
...     __test = "serhat"

>>> test._test__test
'serhat'

>>> class test:
...     def __init__(self):
...         self.__test = "serhat"

>>> t = test()
>>> t._test__test
'serhat'

>>> class test:
...     def __init__(self):
...         self.__test = "serhat"
...     def print(self):
...         print(self.__test)

>>> t = test()
>>> t.print()
serhat
```

- Name mangling'in kullanılma nedeni, class genişletmelerinde (kalıtım verme) çakışmaları önlemektir. Dunder ile tanımlanan değişkenler, kalıtım verilen sınıfta override edilemezler, bunun yerine yeni bir değişken oluşur.

```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23
        
class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
  
t1 = Test()
print(dir(t1))
print(t1.foo)
print(t1._bar)
print(t1._Test__baz)
        
t2 = ExtendedTest()
print(dir(t2))
print(t2.foo)
print(t2._bar)
print(t2._ExtendedTest__baz)

# ['_Test__baz', ..., '_bar', 'foo']
# 11
# 23
# 23

# ['_ExtendedTest__baz', '_Test__baz', ..., '_bar', 'foo']
# overridden
# overridden
# overridden
```

- Değişkenler gibi fonksiyonlar da  aynı özelliğe sahiptir. 

```python
>>> class Test:
...     def __test(self):
...         return "serhat"
...     def print(self):
...         print(self.__test())

>>> t = Test()
>>> t._Test__test()
'serhat'
>>> t.print()
serhat
```

- Name mangling özelliği kullanılarak class değişkenleri dışarıdan atanabilir.

```python
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled

>>> MangledGlobal().test()
23
```

## 4. Double Leading and Trailing Underscore: `__var__`

- Python dilinde genellikle özel durumlarda kullanılan ve çoğunlukla built-in tanımlanan fonksiyonlar için kullanılır.
    - `__init__`, `__str_`, `__call__` gibi...
    - Bu metotlara `dunder methods` veya `magic methods` adı verilir.
- Dunders ile başlamasına rağmen, name mangling değişimine uğramazlar. Python, sondaki dunders ile bu durumu ayırt eder.

```python
class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

>>> PrefixPostfixTest().__bam__
42
```

## 5. Single Underscore: `_`

- Geçici veya önemsiz değişkenleri isimlendirmek için kullanılır.

```python
>>> for _ in range(32):
...     print('Hello, World.')
```

- Bir çok interpeter, `_` yazıldığında son tanımlanan değeri referans verir. Fakat bu özelliği kullanmak pek tavsiye edilmez, çünkü her interpreterda bu çalışmaz ve run-time'da işe yaramaz (.py dosyaları içinde).

```python
>>> 20 + 3
23
>>> _
23
>>> print(_)
23

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]
```

## Özet

| Pattern                                    | Example   | Meaning                                                      |
| ------------------------------------------ | --------- | ------------------------------------------------------------ |
| **Single Leading Underscore**              | `_var`    | Naming convention indicating a name is meant for internal use. Generally not enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only. |
| **Single Trailing Underscore**             | `var_`    | Used by convention to avoid naming conflicts with Python keywords. |
| **Double Leading Underscore**              | `__var`   | Triggers name mangling when used in a class context. Enforced by the Python interpreter. |
| **Double Leading and Trailing Underscore** | `__var__` | Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes. |
| **Single Underscore**                      | `_`       | Sometimes used as a name for temporary or insignificant variables (“don’t care”). Also: The result of the last expression in a Python REPL. |
