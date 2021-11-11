# Object-Oriented Programming in Python

## OOP'ye Genel Bakış

- OOP; yazılan programın, birbirinden bağımsız objelerle yapılandırılmasına olanak sağlar.
- OOP'nin sağladığı faydalar:
    - OOP sayesinde, gerçek hayattaki nesneleri program dillerinde sınıflaştırıp kullanabiliriz (araba, insan, email, kontrat vs).
        - Sınıfların özelliklerini birbirinden ayırarak soyutlama sağlar.
        - Sınıflarda bir kere oluşturulan özellikler tekrar tekrar yazılmak durumda kalınmaz.
        - Bir sınıfı değiştirerek tüm nesneleri değiştirebileceğimiz için program yönetimini kolaylaştırır.
    - Ayrıca OOP sayesinde programlar modüler (birbirinden bağımsız) parçalar halinde yazılabilir.
        - OOP kod tekrarını da önler.
        - Fonksiyonel programlamayı sağlar.
        - Modüller başka programlarda kullanılmak üzere tanışabilir.
- Nesne yönelimli programlamanın 4 temel özelliği bulunur:
    - Soyutlama (Abstraction) : Sınıfın sadece gerekli özelliklerinin dışarı açılmasını, sınıf içinde işlem yapılan özelliklerin sınıf içinde gizli kalması olayıdır. Daha derli toplu bir ifadeyle objelerin ayrıntılarıyla uğraşmak yerine yalnızca girdi ve çıktılarına odaklanarak tasarımı daha iyi oluşturmayı ve anlamayı sağlamaktır.
    - Kapsülleme (Encapsulation) : Sınıfın özelliklerinin (fields) fonksiyonlar ile dışarı açılmasıdır. Sınıfın özelliklerine direk olarak atanma yapılmaması ve bunun yerine `get_x()`, `set_x()` vb. metotlarda yönetilmesi durumunu ifade eder. Sınıfı veya nesneyi kullanan programcı, sınıf içi `imlementation codes/deails` ile uğraşmaz, sadece ilgili metodu istenen parametrelerle kullanır.
    - Miras Alma (Inheritance) : Sınıfın özelliklerini başka bir sınıftan alabilmesi veya özelliklerini başka bir sınıfa verebilmesi özelliğidir.
    - Çok Biçimlilik (Polymorphism) : Başka bir sınıftan kalıtım alınan özelliklerin sınıf içinde ezilip (`overriding`) tekrar oluşturulmasıdır. Bu özellik sayesinde birbirinden kalıtım alan sınıflar farklı davranışlar gösterebilir.

##### Class ve Elemanları

- **Class (Sınıf)** : Nesne oluşturmak için kullanılan soyut taslaklardır. İçinde herhangi bir data bulunmaz.
- **Instance / Object (Nesne / Obje)** : Class'lardan türetilen somut objelerdir. İçinde data bulundurur. Bir class'tan farklı datalar buunduran farklı nesneler oluşturulabilir.
- Class elemanları: 
    - **Fields** : Class içinde bulunan ve class'ın özelliklerinin belirlendiği değişkenlerdir. Birçok programlama dilinde private olarak tanımlanırlar ve properties fonksiyonları ile yönetilirler (Encapsulation).
    - **Properties** : Class içindeki private field'ları yönetmek için kullanılan fonksiyonlardır. `get` ve `set` olarak iki metodun birleşiminden oluşur.
    - **Methods** : Class içinde, class ile ilgili çeşitli işlemler yapan fonksiyonlardır.

## Python'da Class ve Instance Tanımlama ve Özellikleri

```python
# Create Class
class Dog:
    pass
```

- Class isimlendirmesinde (zorunlu olmamakla birlikte) PEP8 kurallarına göre `PascalCase` kullanılır.

```python
# Create instance of class
>>> a = Dog()
>>> b = Dog()
>>> a is b, a == b
(False, False)
```

## `self` Keyword

- Class içinde türetilen nesne işlem yapmaya, class içindeki method ve özelliklere ulaşmaya yarar.

## Constructor Method `__init_`

- Class'tan nesne oluştururken çalışan methottur.
- Zorunlu parametre tanımlama

## Attributes

- Pythonda iki çeşit attribute bulunur:
    - `Class Attribute`
    - `Instance Attribute`

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attribute
        self.name = name
        self.age = age
```

- `instance attribute`
    - **"Nesne"**lere özel değişkenlerdir.
    - Nesneler üzerinden ulaşılabilir.
    - Her nesne için farklı değerler alabilir ve alınan değerler sadece o nesne ile kullanılabilir.
    - `Construction` metot olan `__init__(self)` metodu içinde tanımlanır.
- `class attribute`
    - **"Class"**lara özel değişkenlerdir.
    - Class üzerinden veya nesne üzerinden ulaşılabilir.
    - Her nesne için başlangıçta aynı değere sahiptir ve bu sahiplik classtan gelir. 
        - Eğer class üzerinden değişken değeri değişirse, tüm nesnelerde de bu değer değişir. 
        - Eğer nesne üzerinden değişken değeri değişirse, değişkenin sahipliği bu nesneye aktarılır. Yeni değere sadece bu nesne üzerinden erişilir ve class değerinde veya diğer nesnelerde herhangi bir değişiklik olmaz.

```python
>>> class Dog:
...     # Class attribute
...     species = "Canis familiaris"
...
...     def __init__(self, name, age):
...         # Instance attribute
...         self.name = name
...         self.age = age

>>> a = Dog("foo", 4)
>>> b = Dog("baz", 5)

>>> a.name, a.age
('foo', 4)
>>> b.name, b.age
('baz', 5)
>>> a.species, b.species, Dog.species
('Canis familiaris', 'Canis familiaris', 'Canis familiaris')

>>> Dog.species = "Beagle"
>>> a.species, b.species, Dog.species
('Beagle', 'Beagle', 'Beagle')

>>> a.species = "Golden"
>>> a.species, b.species, Dog.species
('Golden', 'Beagle', 'Beagle')

>>> Dog.species = "Dakhund"
>>> a.species, b.species, Dog.species
('Golden', 'Dakhund', 'Dakhund')
```

## Methods

- Python'da üç çeşit method bulunur.
    - `Instance Method`
    - `Class Method`
    - `Static Method`

#### 1. Instance Methods

- Class içinde tanımlanan ve nesneler üzerinden ulaşılan fonksiyonlardır.
- `self` keyword'ü ile tanımlanır.

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
>>> miles = Dog("Miles", 4)

>>> miles.description()
'Miles is 4 years old'

>>> miles.speak("Woof Woof")
'Miles says Woof Woof'

>>> miles.speak("Bow Wow")
'Miles says Bow Wow'
```

#### 2. Class Methods

#### 3. Static Methods

## Inherit From Other Classes

