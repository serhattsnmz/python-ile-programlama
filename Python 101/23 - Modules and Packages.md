# Modules and Packages

- **Modüler Programlama** : Büyük kapsamlı ve birçok iş yapan bir programın, küçük ve kendi içinde anlamlı parçalara bölünerek oluşturulmasını sağlayan programlama yaklaşımıdır.
- Modüler programlamanın avantajları:
    - **Simplicity (Basitlik)**: Her modül programın küçük bir parçasını oluşturuğu için yönetilmesi basittir. Çıkan hatalar daha kolay handle edilebilir. Her modülün kendi içinde anlam bütünlüğü olduğundan anlaşılması daha kolaydır.
    - **Maintainability (Bakım)**: Modüller birbirinden mantıksal olarak bağımsız inşa edildiklerinden, bir modülün değişimi, yeniden kurgulanması veya hata ayıklaması daha kolaydır.
    - **Reusability (Yeniden kullanılabilirlik)**: Bir modül bağımsız ama kendi içinde tutarlı olduğundan, birçok projede kullanılabilir.
    - **Scoping (Ayrık Kapsam)**: Her modülün kendine ait bir namespace'i (scope) olduğundan, modüller arasındaki çakışma daha azdır.

## Modül Oluşturma ve Kullanma

- Pythonda modüller, basit olarak `.py` dosyaları ile oluşturulur. Özel bir tanımlama şekli yoktur.

```python
# mod.py file 

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass
```

#### The `import` Statement

- Herhangi bir modül dosyası kullanılmak istendiğinde `import` keyword'ü kullanılarak projeye eklenir.
    - Birden fazla modül, tek bir `import` kullanılarak projeye eklenebilir.


```python
import <module_name>
import <module_name>[, <module_name> ...]
```

- `import` ile projeye eklenen modülün içeriği direk olarak projeye eklenmez. Proje namespace(`symbol table`)'ine sadece `<modul_name>` ismi eklenir ve modül içeriğine bu isim üzerinden ulaşılır.

```python
>>> import mod

>>> mod
<module 'mod' from 'C:\\Users\\john\\Documents\\Python\\doc\\mod.py'>

>>> s
NameError: name 's' is not defined
    
>>> foo('quux')
NameError: name 'foo' is not defined

>>> mod.s
If Comrade Napoleon says it, it must be right.

>>> mod.a
[100, 200, 300]

>>> mod.foo(['quux', 'corge', 'grault'])
arg = ['quux', 'corge', 'grault']

>>> x = mod.Foo()
>>> x
<mod.Foo object at 0x03C181F0>
```

#### The `from` Statement

- Modül içeriğinin bir kısmını veya hepsini projenin namespace(`symbol table`)'ine eklemek için kullanılır.

```python
from <module_name> import <name(s)>
from <module_name> import <name(s)>[, <name(s)> ...]
from <module_name> import *
```

- Projeye direk eklendiğinden `<module_name>` öneki kullanılmadan direk olarak çalıştırılırlar.

```python
>>> from mod import s, foo, Foo

>>> s
'If Comrade Napoleon says it, it must be right.'

>>> foo('quux')
arg = quux

>>> x = Foo()
>>> x
<mod.Foo object at 0x02E3AD50>
```

- Projeye `*` wildcard'ı ile tüm içerik eklenebilir. Yalnız `_` ile başlayan değişken veya fonksiyonlar projeye eklenmez. (bkz: InDeph - The Meaning of Underscores in Python notu)
    - Wildcard kullanımı şu durumlardan ötürü tavsiye edilmez:
        - Çok fazla içerik bulunduran modüllerin eklenmesi, ana projenin namespace'inde gereksiz yer işgal edecektir ve karışıklığa neden olacaktır. 
        - Projede kullanılan fonsiyon veya değişkenlerin referanslarına gidilmek istendiğinde hangi modül içinde olduğu zorlukla bulunacaktır.

```python
>>> from mod import *
>>> s
'If Comrade Napoleon says it, it must be right.'
>>> a
[100, 200, 300]
>>> foo
<function foo at 0x03B449C0>
>>> Foo
<class 'mod.Foo'>
```

#### The `from ... import ... as ...` and `import ... as ...` Statement

```python
from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]
import <module_name> as <alt_name>
```

- `as` keyword'ü, projeye eklenen modüle veya modül içeriğine farklı alias'lar ile ulaşmayı sağlar.
    - `from ... import ...` kullanılırken, eklenen objeler ana namespace içinde daha önceden varsa bunlar override edilir. Bunun önüne geçmek için bu yöntem kullanılabilir.

```python
>>> s = 'foo'
>>> a = ['foo', 'bar', 'baz']

>>> from mod import s as string, a as alist
>>> s
'foo'
>>> string
'If Comrade Napoleon says it, it must be right.'
>>> a
['foo', 'bar', 'baz']
>>> alist
[100, 200, 300]
```

```python
>>> import mod as my_module
>>> my_module.a
[100, 200, 300]
>>> my_module.foo('qux')
arg = qux
```

## The Module Search Path

- Bir modül import edildiğinde, Python bu modülü belli yollarda arar. Bunlar sırasıyla şunlardır:
    1. Python dosyasının çalıştırıldığı kök dosya yolu. Eğer interpreter çalıştırılmışsa, çalıştırıldığı andaki dosya yolu. 
    2. `PYTHONPATH` evironment variable (ortam değişkeni) işletim sisteminde tanımlanmışsa, burdaki dosya yolları. 
    3. Python kurulurken default olarak kurulan local ve global script dosya yolları
- Module search yolları, `sys.path` ile yazdırılabilir.

```python
import os
>>> print(sys.path)
[
    # Mevcut çalıştırılma dizini
    '',
    # Local default script yolları
    'C:\\Users\\serhat\\AppData\\Roaming\\Python\\Python39\\site-packages',
    'C:\\Users\\serhat\\AppData\\Roaming\\Python\\Python39\\site-packages\\win32',
    'C:\\Users\\serhat\\AppData\\Roaming\\Python\\Python39\\site-packages\\win32\\lib',
    'C:\\Users\\serhat\\AppData\\Roaming\\Python\\Python39\\site-packages\\Pythonwin',
    # Global default script yolları
    'C:\\Program Files\\Python39\\Scripts\\ptpython.exe',
    'C:\\Program Files\\Python39\\python39.zip',
    'C:\\Program Files\\Python39\\DLLs',
    'C:\\Program Files\\Python39\\lib',
    'C:\\Program Files\\Python39',
    'C:\\Program Files\\Python39\\lib\\site-packages'
]
```

- `pip` ile kurulum yaparken indirilen modüller aşağıdaki yollardan birine kurulur:
    - `C:\\Program Files\\Python39\\lib\\site-packages`
    - `C:\\Users\\serhat\\AppData\\Roaming\\Python\\Python39\\site-packages`
    - Eğer kurulum admin ile yapılmışsa global, `--user` ile yapılmışsa local path'e kurulum yapılır.
- Bir modüle ulaşılmak istendiğinde modülün path içindeki yollardan birinde olması gerekir.
    - Eğer modül farklı bir yerden import edilecekse, bu yol `PYTHONPATH` içine eklenebilir.
    - Ya da runtime'da `sys.path` listesine eklenip ordan çekmesi sağlanabilir. 

```python
# "mod.py" is in "C:\Users\john"
>>> sys.path.append(r'C:\Users\john')
>>> sys.path
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages', 'C:\\Users\\john']
>>> import mod
```

## The `dir()` Function

- Built-in `dir()` fonksiyonu, verilen obje veya modülün `local symbol table` içeriğini döndürür. Başka bir deyişle o namespace içinde tanımlanmış değişkenlerin isimlerini liste olarak verir. 
    - Herhangi bir parametre verilmediğinde o an bulunan modülün içeriğini döndürür. `globals()` ile aynı değerleri verir.

```python
print(list(globals().keys()))
['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__']

print(dir())
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
```

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> qux = [1, 2, 3, 4, 5]
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'qux']

>>> class Bar():
...     pass
...
>>> x = Bar()
>>> dir()
['Bar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'qux', 'x']
```

- Import durumlarının mevcut namespace içine nasıl eklendiğine `dir()` ile bakabiliriz. 

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> import mod
>>> dir()
[..., 'mod']

>>> from mod import a, Foo
>>> dir()
[..., 'mod', 'Foo', 'a']

>>> from mod import s as string
>>> dir()
[..., 'mod', 'Foo', 'a', 'string']
```

- `dir(<module_name>)` fonksiyonuna parametre olarak modül ismi verirsek, modülün kendi global scope'undaki obje isimlerini döndürür. 

```python
>> import mod
>>> dir(mod)
['Foo', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'a', 'foo', 's']
```

- `dir()` fonksiyonunu bir çok obje için, propery ve fonksiyonlarını görmek için kullanabiliriz.

```python
>>> a = "foo bar"
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> a = [1,2,3]
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> a = {1:2}
>>> dir(a)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

>>> a = {1,2,3}
>>> dir(a)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
```

## Using `__name__` in Script File

- Bir modül import edildiğinde içindeki class ve function objelerinin programın namespace'ine eklendiğinden bahsetmiştik. Bununla birlikte modül içinde çalışacak kodlar varsa, bu kodlar da import edilirken çalıştırılır.

```python
# module.py

class Test:
    def __init__(self):
        self.foo = "bar"
        
def f():
    print("Hellow!")
    
t = Test()
print(t.foo)
f()
```

```python
>>> import module
bar
Hellow!
```

- Script dosyasını çalıştırdığımızda da aynı kodlar çalışır.

```
λ python module.py
bar
Hellow!
```

- Bazı durumlarda script dosyasını çalıştırdığımızda bazı kodların çalışmasını (unit test gibi) isteriz, fakat modül olarak import edildiğinde bu kodların çalışmasını istemeyiz. Bu durumda bu kodları bir koşul altına yazmak gerekir. 
- `__name__` özel ifadesi, modül olarak eklenen dosyanın ismini verir. Ana dosya içinde ise `"__main__"` ifadesine karşılık gelir.

```python
>>> import module
bar
Hellow!

>>> module.__name__
'module'

>>> __name__
'__main__'
```

- Python dosyasında, sadece dosya çalıştırıldığında çalışacak fakat import edildğinde çalışmamasını istediğimiz kodları, `__name__ == "__main__"` koşuluyla sağlayabiliriz. `module.py` dosyasını aşağıdaki gibi düzenleyebiliriz:

```python
# module.py

class Test:
    def __init__(self):
        self.foo = "bar"
        
def f():
    print("Hellow!")

if __name__ == "__main__": 		# All "script spesific" codes are in this condition
    t = Test()
    print(t.foo)
    f()
```

- Düzenlememiz sonucunda `module.py` dosyasını direk olarak çalıştırdığımızda kodlarımız çalışacak, import ettiğimizde ise kodlar çalışmayacaktır. 

```
λ python module.py
bar
Hellow!
```

```python
>>> import module
>>> 
```

## Reloading Module

- Modüller import edildiğinde bir kere çalışır ve daha sonra tekrar import edilseler dahi yüklenmezler.

```python
# mod.py

a = [100, 200, 300]
print('a =', a)
```

```python
>>> import mod
a = [100, 200, 300]
>>> import mod
>>> import mod
>>> mod.a
[100, 200, 300]
```

- Belli bir interpreter session'ı içinde bir modül değiştirilirse yeniden yüklemek için;
    - Interpretter kapatılıp açılabilir, bu şekilde session sıfırlanmış olur. 
    - `importlib.reload()` fonksiyonu kullanılabilir.

```python
>>> import mod
a = [100, 200, 300]

>>> import mod

>>> import importlib
>>> importlib.reload(mod)
a = [100, 200, 300]
<module 'mod' from 'C:\\Users\\john\\Documents\\Python\\doc\\mod.py'>
```

## Python Packages

- Modüllerin bir namespace altında toplanmasına yarar. Bir veya birden fazla modül bulunduran kütüphaneler olarak tanımlayabiliriz.
- Paketler oluşturulurken, modüller bir dizin altında toplanır ve import edilirken dizin ismini namespace olarak alırlar.

```
.
├── main.py
└── pkg				# Package
    ├── mod1.py		# Module 1
    └── mod2.py		# Module 2
```

```python
	# import method 1
import pkg.mod1
import pkg.mod2
pkg.mod1.foo()
pkg.mod2.bar()

	# import method 2
from pkg import mod1
from pkg import mod2
mod1.foo()
mod2.bar()

	# import method 3
from pkg.mod1 import foo
from pkg.mod2 import bar
foo()
bar()

	# import method 4
import pkg.mod1 as m1
import pkg.mod2 as m2
m1.foo()
m2.bar()
```

- Paketin direk olarak import edilmesi bir hataya neden olmaz ama herhangi bir işe de yaramaz. Import edilen paket üzerinden herhangi bir modüle ulaşılamaz. 

```python
>>> import pkg
>>> pkg
<module 'pkg' (namespace)>

>>> pkg.mod1
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    pkg.mod1
AttributeError: module 'pkg' has no attribute 'mod1'
    
>>> pkg.mod1.foo()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    pkg.mod1.foo()
AttributeError: module 'pkg' has no attribute 'mod1'
```

- Pip ile indirilen kütüphaneler package şeklindedir. "The Module Search Path" başlığı altındaki default pip kurulum yollarına bakılırsa package düzenleri görülebilir.

## Package Initialization

- Paketler içinde oluşturulan ve özel bir dosya olan `__init__.py` dosyası, paket import edildiğinde veya paket içindeki herhangi bir modül import edildiğinde çalışacak kodları bulunduran `initialization` dosyasıdır. (Class'lardaki mantığa benzer, sadece burda class düzeyinde değil, package düzeyinde çalışır.)

```
.
├── main.py
└── pkg
    ├── __init__.py
    ├── mod1.py
    └── mod2.py
```

```python
# __init__.py

print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']
```

```python
>>> import pkg
Invoking __init__.py for pkg

>>> pkg.A
['quux', 'corge', 'grault']
```

- Paket içindeki modüller, `__init__.py` içindeki global değişkenlere, paketi import ederek ulaşabilirler.

```python
# mod1.py

def foo():
    from pkg import A
    print('[mod1] foo() / A = ', A)

class Foo:
    pass
```

```python
>>> from pkg import mod1
Invoking __init__.py for pkg

>>> mod1.foo()
[mod1] foo() / A =  ['quux', 'corge', 'grault']
```

- `__init__.py` dosyası, paket çağırıldığında import edilmesi istenilen modülleri de import edebilir. Böylece sadece paket import edilerek altındaki modüller kullanılabilir.

```python
# __init__.py
print(f'Invoking __init__.py for {__name__}')
import pkg.mod1, pkg.mod2
```

```python
>>> import pkg
Invoking __init__.py for pkg

>>> pkg.mod1.foo()
[mod1] foo()

>>> pkg.mod2.bar()
[mod2] bar()
```

- **Bilgi** : Python2 ve Python 3.3 öncesi sürümlerde, python package oluşturmak için `__init__.py` dosyası oluşturmak zorunluydu. Python 3.3 ile beraber bu dosyanın oluşturulması opsiyonel hale getirildi.

## Using `__all__` Variable

- `__all__` değişkeni, bir paket veya modül wildcard ile import edildiğinde, hangi objelerin import edileceğinin belirlendiği özel liste değişkenidir.
    - Default olarak modüller import edildiğinde, alt çizgi ile başlayan objeler (`_var`) dışında tüm objeler import edilir.
    - Default olarak bir paket import edildiğinde herhangi bir modül import edilmez.

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> from pkg import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> mod1.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mod1' is not defined

name 'mod1' is not defined
```

- Package içindeki modülleri wildcard ile yüklemek için `__init__.py` dosyası içinde `__all__` özel değişkeninin tanımlanması gerekir.

```python
# __init__.py
__all__ = [
    'mod1',
    'mod2'
]
```

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> from pkg import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'mod1', 'mod2']

>>> mod1.foo()
[mod1] foo()

>>> mod2.bar()
[mod2] bar()
```

- Modül içinde de `__all__` değişkeni, import edilecek objeleri sınırlandırmak için kullanılır.

```python
# pkg/mod1.py

__all__ = ['foo']

def foo():
    print('[mod1] foo()')

class Foo:
    pass
```

```python
>>> from pkg.mod1 import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'foo']

>>> foo()
[mod1] foo()

>>> Foo
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Foo
NameError: name 'Foo' is not defined
```

## Subpackages

- Bir paket içinde birden fazla alt paket oluşturulabilir. Import edilme yapıları normal paket importu ile aynıdır.

```
.
├── main.py
└── pkg
    ├── sub_pkg1
    │   └── mod1.py
    └── sub_pkg2
        └── mod2.py
```

```python
>>> import pkg.sub_pkg1.mod1
>>> pkg.sub_pkg1.mod1.foo()
[mod1] foo()

>>> from pkg.sub_pkg2 import mod2
>>> mod2.bar()
[mod2] bar()
```

- Alt paketler içinde diğer alt paketler import edilmek isteniyorsa, iki yöntemle yapılır.

1. Absulute path verilerek import edilebilir. Burdaki absulute path, ana script dosyasının çalıştığı yerden başlar.

```python
# pkg/sub_pkg2/mod2.py
def baz():
    print('[mod3] baz()')

class Baz:
    pass

from pkg.sub_pkg1.mod1 import foo
foo()
```

2. Relative path verilerek import edilebilir. `..` ile path dışına çıkılır ve diğer paketler import edilir. Burda başlangıç konumu, modülün bulunduğu dosya yoludur. 

```python
# pkg/sub_pkg2/mod2.py
def baz():
    print('[mod3] baz()')

class Baz:
    pass

from .. import sub_pkg1
print(sub_pkg1)

from ..sub_pkg1.mod1 import foo
foo()
```

## Using Pip

- **Pip** : Python Package Manager. Çalışma ortamına yeni python paketleri yüklemeyi sağlar. 
    - Yüklenebilecek paketlerin listesi şurdan bakılabilir: https://pypi.org/
    - Pip yüklemesi ile ilgili ayrıntılı bilgi: https://pip.pypa.io/en/stable/
- Bir bilgisayarda birden fazla pip sürümü olabilir. Genellikle Python2 ve Python3 için farklı, ve her versiyonu için farklı pip olabilir.

```bash
└─[$]> ls -la /usr/bin/ | grep -i pip
-rwxr-xr-x  1 root root           941 Jul  1 23:44 pip
-rwxr-xr-x  1 root root           943 Jul  1 23:44 pip3
```

- Pip versiyonu ve pip'in hangi python versiyonuna bağlı olduğunu `-v` ile öğrenebiliriz:

```
λ pip --version
pip 21.3.1 from C:\Program Files\Python39\lib\site-packages\pip (python 3.9)

λ python -m pip -V
pip 21.3.1 from C:\Program Files\Python39\lib\site-packages\pip (python 3.9)
```

- Pip işlemleri

```bash
# Install packages with pip	
λ pip install <package_name>

# Install package to user install directory
λ pip install <package_name> --user

# Uninstall packages with pip
λ pip unistall <package_name>

# List downloaded packages
λ pip list

# Upgrade package
λ pip install --upgrade <package_name>

# Upgrade pip
λ python -m pip install --upgrade pip

# Show package metadata and details
λ pip show <package_name>
```

- **NOT:** pip ile indirilen dosyalar aşağıdaki iki yoldan birine kaydedilir.
    - Admin/root yetkisi ile indirilmişse;
        - ` C:\Program Files\Python39\lib\site-packages`
        - `/usr/lib/python3/dist-packages`
    - `--user` parametresi ile indirilmişse;
        - `C:\Users\serhat\AppData\Roaming\Python\Python39\site-packages`
        - ` /home/serhat/.local/lib/python3.9/site-packages`
    - `pip show <package_name>` ile indirilen paketin konumuna bakılabilir.
    - Aşağıdaki python kodları ile de indirme konumlarına bakılabilir:

```python
>>> import site
>>> site.getsitepackages()
['C:\\Program Files\\Python39', 'C:\\Program Files\\Python39\\lib\\site-packages']
>>> site.getusersitepackages()
'C:\\Users\\serhat\\AppData\\Roaming\\Python\\Python39\\site-packages'
```

#### Requirements.txt File

- pip ile indirilen paketler, projeyi çalıştıran bilgisayarın ilgili kayıt yerlerinde saklanır. Bir proje başka bir ortamda çalıştırılırsa aynı paketlerin o bilgisayara da indirilmesi gerekir.
- Bunu kolaylaştırmak için projelere `requirements.txt` adlı bir dosya eklenir. (Dosya adı değişebilir ama genellikle herkes aynı ismi tercih eder.)
- Dosya içine, her satıra bir paket ismi gelecek şekilde, projede kullanılacak kütüphaneler yazılır.

```
$ cat requirements.txt
certifi
chardet>=3.0
idna==2.8
requests==2.21.0
urllib3==1.24.1
```

- Paket isimlerinin yanına versiyon numaraları verilebilir ve istenilirse `==, >, <, >=, <=` ifadelerinden biri de kullanılabilir.
- Bir dosya içindeki paketler pip ile `-r` parametresi kullanılarak kolayca indirilebilir ve topluca kaldırılabilir.

```
$ pip install -r requirements.txt
$ pip uninstall -r requirements.txt -y
```

- Tavsiye edilmese de, bir çalışma ortamında pip ile indirilen tüm paketlerin isimleri ve versiyonları `pip freeze` komutu kullanılarak bir dosyaya yazılabilir.

```
$ pip freeze > requirements.txt
$ cat requirements.txt

certifi==2018.11.29
chardet==3.0.4
idna==2.8
requests==2.21.0
urllib3==1.24.1
```

- Ayrıntılı bilgi için bkz: https://pip.pypa.io/en/stable/reference/requirements-file-format/

## Python Virtual Environments

- Python virtual environment, default çalıştırma konumlarından izole bir python ortamı oluşturmamızdır.
- PVE oluştururken, hem python programının kendisi için hem de pip için izole edilmiş farklı bir kopya oluşturulur ve pip ile indirilen paketler sadece bu ortam için indirilir.
- PVE'a neden ihtiyaç duyarız;
    - Bir proje için bağımsız bir ortam oluşturup projeye ait pip paketlerini ana bilgisayar ve başka projenin ortamlarından ayrı olarak oluşturabiliriz. Bu şekilde birden fazla proje aynı paketin farklı versiyonlarında çalışabilir.
    - Bir proje için oluşturulan ortamda proje dışı pip paketleri olmayacağından `pip freeze` ile kolaylıkla `requirements.txt` dosyası oluşturulabilir.
    - Farklı python sürümleri için farklı ortamlar oluşturup testler gerçekleştirebiliriz. Fakat bu python sürümlerinin ana bilgisayarda yüklü olması gerekir, çünkü ana python dosyaları ortam içine kopyalanır, ana bilgisayarda yoksa kopyalanma yapılamaz.
- PVE oluşturmak için pip ile kurabildiğimiz `virtualenv` paketinden yararlanırız:

```
# Install (Linux)
$ sudo pip3 install virtualenv

# Install (Windows)
λ pip install virtualenv

# Create PVE (Windows & linux)
λ virtualenv <env_path>
```

- PVE oluşturduktan sonra;
    - `<env_name>/bin/activate`(linux) veya `<env_name>\Scripts\activate.bat` (windows) çalıştırılarak ortam aktifleştirilir.
    - `deactivate`(linux) veya `deactivate.bat`(windows) komutu çalıştırılarak ortamdan çıkılır.

```bash
## Linux

[$]> virtualenv env-linux
created virtual environment CPython3.9.7.final.0-64 in 145ms
...

[$]> source env-linux/bin/activate

[$](env-linux)> python -V
Python 3.9.7

[$](env-linux)> which python
/home/serhat/Desktop/env-linux/bin/python

[$](env-linux)> pip -V
pip 21.3.1 from /home/serhat/Desktop/env-linux/lib/python3.9/site-packages/pip (python 3.9)

[$](env-linux)> deactivate

[$]> which python
/usr/bin/python

[$]> pip -V
pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)
```

```
## Windows

λ virtualenv env-win
created virtual environment CPython3.9.7.final.0-64 in 534ms
...

λ .\env-win\Scripts\activate.bat

(env-win) λ python -V
Python 3.9.7

(env-win) λ which python
/c/Users/serhat/Desktop/python-test/env-win/Scripts/python

(env-win) λ pip -V
pip 21.2.4 from C:\Users\serhat\Desktop\python-test\env-win\lib\site-packages\pip (python 3.9)

(env-win) λ deactivate.bat

λ which python
/c/Program Files/Python39/python

λ pip -V
pip 21.3.1 from C:\Program Files\Python39\lib\site-packages\pip (python 3.9)
```

- PVE kurulduktan sonra pip ile yapılan tüm işlemler (indirme, kaldırma veya listeleme gibi) bu ortamda çalışır. Python ile çalıştırılan tüm dosyalar da **_sadece_** bu ortamdaki paketleri kullanır.

- PVE ortamı aktifleştirildiğinde temel olarak iki işlem yapılır:
    - `python` ve `pip` programları kopyalanır.
    - Sistemin `PATH` değişkeni geçici olarak değiştirilir ve yeni ortam olarak ayarlanır.

- PVE oluştururken farklı python versiyonları seçilebilir. Default olarak `python3` alias'ıyla temsil edilen python versiyonu seçilir.
    - Python versiyonlarının ana sistemde yüklü olması gerekir.

```
λ virtualenv -p python3.5 env-win
...
λ virtualenv -p python3.9 env-win
...
```

