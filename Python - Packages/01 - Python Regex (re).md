# Python Regular Expressions (Regex)

- Bir text içinde belirli bir string değerini `in`, `text.find()` veya `text.index()` fonksiyonlarıyla bulabiliriz. Fakat aradığımız bir string değeri değil de bir string deseni (patern) olursa bu metotlar işe yaramaz. 
- Regular Expressions (Regex); bir text içinde araştıracağımız desene verilen isimdir. Regex oluşturduktan sonra bu desene uyan yapıları text içinde arar ve kesip kullanırız.
- `Regex` veya `Pattern` : Özel ifadeler şekilde yazılmış ve bir text içinde arama yaparken uygulayacağımız kuralları içeren kural öbeğidir.
- Python dışında diğer dillerin çoğunda da regex işlemleri yapılır. Python dilinde bu işlemleri built-in bir paket olan `re` kütüphanesiyle yaparız.
- Kaynaklar
    - Online regex düzenlerine bakmak için kaynak : https://regex101.com/
    - Python regex doc : https://docs.python.org/3/library/re.html


## Creating Pattern

- Bir pattern oluşturmak için bazı özel karakterlerden yararlanırız.
- Bir pattern temel olarak şu temel yapıdan oluşur:
    1. **Selectors (Seçiciler) :** O alana gelmesini istediğimiz karakterlerden (sayı, haft, özel karakter vs.) bir küme oluşturulur. Tek bir karakter değilse `[]` arasında belirtilir.
    2. **Quantifiers (Niceleyiciler) :** Seçicilerden bir küme oluşturulduktan sonra bu küme içindeki elemanlardan kaç tane geleceğini sayısal olarak belirttiğimiz kısımdır. `{}` arasında belirtilir.
    3. **Başlangıç ve Bitiş :** Zorunlu olmasa da satır/kelime başını belirtmek için `^` işareti, satır/kelime bitişini ifade etmek için de `$` işareti kullanılır.

```
Selector    : [abc]
Quantifier  : {2}
REGEX 		: ^[abc]{2}$
Şunlar uyar   > ab, ac, bc, ba, aa vs. 
Şunlar uymaz  > ad, abc, a, dd vs.

Selector    : [a-z]
Quantifier  : {0,4}
REGEX 		: ^[a-z]{0,4}$
Şunlar uyar   > foo, bar, ba, bazr
Şunlar uymaz  > Foo, bAr, f1o

Selector    : [a-zA-Z0-9]
Quantifier  : {0,4}
REGEX 		: ^[a-zA-Z0-9]{0,4}$
Şunlar uyar   > foo, bar, ba, bazr, Foo, bAr, f1o
Şunlar uymaz  > f-4, s.s, tes?
```

#### Selectors

- Selectorlar niceleyici almadığında tek bir karakter gibi davranırlar:

    - `^foo$` > Sadece `foo` uyar.

- Selectorlar tek karakter veya küme olabilir. Küme olduğunda `[]` kullanılmalıdır.

    - Tek karakter olabilir:
        - `^foo-?bar$` > `foo-bar`, `foo-bar`

    - Küme olabilir:
        - `^foo[-_]?bar$` > `foo-bar`, `foobar`, `foo_bar`

| Character           | Meaning                                                   |
| ------------------- | --------------------------------------------------------- |
| `c`                 | Tek bir karakter                                          |
| `[ccc...]`          | Birden fazla karakterden oluşan bir küme                  |
| `[c-c]`             | Karakter aralığı belirtir                                 |
| `[^cc...]` `[^c-c]` | Bu karakterler dışındakileri seçer (`not` işlemi uygular) |
| `.`                 | Herhangi bir karakteri ifade eder.                        |

#### Quantifiers

| Character            | Meaning                                     |
| -------------------- | ------------------------------------------- |
| `{n}`                | Tam olarak n tane gelir                     |
| `{min,}`             | En az min kadar gelmeli                     |
| `{,max}`             | En fazla max kadar gelmeli                  |
| `{min, max}`         | En az min kadar, en fazla max kadar gelmeli |
| `*`                  | 0 veya daha fazla gelmeli                   |
| `?`                  | 0 veya 1 kere gelmeli                       |
| `+`                  | 1 veya daha fazla gelmeli                   |
| `*?` `+?` `??` `{}?` | Non-greedy version of `*`, `+`, `?`, `{}`   |

- **Non-greedy** : tek başlarına kullanıldığında `*`, `+`, `?` ifadeleri, olabilecek en uzun yolu seçerler. `?` ile birlikte kullanıldığında ise en kısa yolu seçerler.

```python
>>> re.findall(r'<.*>', '%<foo> <bar> <baz>%')
['<foo> <bar> <baz>']
>>> re.findall(r'<.*?>', '%<foo> <bar> <baz>%')
['<foo>', '<bar>', '<baz>']

>>> re.findall(r'<.+>', '%<foo> <bar> <baz>%')
['<foo> <bar> <baz>']
>>> re.findall(r'<.+?>', '%<foo> <bar> <baz>%')
['<foo>', '<bar>', '<baz>']

>>> re.findall(r'ba?', 'baaaa')
['ba']
>>> re.findall(r'ba??', 'baaaa')
['b']

>>> re.findall(r'[ba]{1,3}', 'baaaa')
['baa', 'aa']
>>> re.findall(r'[ba]{1,3}?', 'baaaa')
['b', 'a', 'a', 'a', 'a']
```

#### Special Identifiers

| Character | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| `^`       | Satır başını ifade eder                                      |
| `$`       | Satır sonunu ifade eder                                      |
| `\b`      | Kelime başını ve sonunu ifade eder                           |
| `\B`      | `\b` karakterinin tersi, bulunduğu yerin kelime başı veya sonu olmaması anlamına gelir. |
| `\A`      | Kelimenin başını ifade eder.                                 |
| `\Z`      | Kelimenin sonunu ifade eder.                                 |
| `\`       | Kaçış karakteri                                              |
| `|`       | `or` işlemi uygular, iki seçenekten birini seçemye yarar.    |
| `()`      | Grup oluşturur                                               |

#### Chracter Classes

| Chracter | Meaning                   |                |
| -------- | ------------------------- | -------------- |
| `\d`     | Digits                    | [0-9]          |
| `\D`     | Non-Digits                | [^0-9]         |
| `\w`     | Alphanumeric and `_`      | [A-Za-z0-9_]   |
| `\W`     | Non Alphanumeric nor `_`  | [^A-Za-z0-9_]  |
| `\s`     | Whitespace Chracters      | [ \t\r\n\v\f]  |
| `\S`     | Non Whitescpace Chracters | [^ \t\r\n\v\f] |

## Python `re` Package

- Python regex işlemleri yapılırken pattern tanımlamaları `raw string` olarak yapılmalıdır.
    - Örn: `r"pattern"` gibi
    - Ayrıntılı bilgi için bkz: https://stackoverflow.com/a/13836171/13177166

---

`re.findall(pattern, string, flags=0)`

- Text içindeki pattern aranır ve liste olarak sonuç döner.

```python
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']

>>> re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
[('width', '20'), ('height', '10')]
```

---

`re.split(pattern, string, maxsplit=0, flags=0)`

- Verilen text'i, verilen pattern'e göre böler ve liste olarak verir.
- `maxsplit` parametresi, text'in kaç kere bölüneceğini belirtir. Değer verilmezse tüm texti böler.

```python
>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']

>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']

>>> re.split(r'\W+', 'Words, words, words.', 1)
['Words', 'words, words.']

>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
```

---

`re.sub(pattern, repl, string, count=0, flags=0)`

- Verilen text içindeki uygun pattern kısmını verilen değer ile değiştirir.
- `count` parametresi ile değişimin kaç kere yapılacağını limitleyebiliriz.

```python
>>> text = "Date : 11.11.2021, Name : James"

>>> text = re.sub(r"\d{2}.\d{2}.\d{4}", "---", text)
>>> text
'Date : ---, Name : James'

>>> text = re.sub(r"Name : \w+\b","Name : xxx", text)
>>> text
'Date : ---, Name : xxx'
```

- `repl` parametresi olarak bir fonksiyon da verilebilir.

```python
>>> def f(match_obj):
...     s = match_obj.group(0)  # The matching string
...
...     # s.isdigit() returns True if all characters in s are digits
...     if s.isdigit():
...         return str(int(s) * 10)
...     else:
...         return s.upper()
...
>>> re.sub(r'\w+', f, 'foo.10.bar.20.baz.30')
'FOO.100.BAR.200.BAZ.300'
```

---

`re.subn(pattern, repl, string, count=0, flags=0)`

- `re.sub()` ile aynı işlemi yapar ama return olarak iki elemanlı tuple döner. İlk eleman yeni stringi, ikinci eleman kaç tane replace işlemi yapıldığının bilgisini döner.

```python
>>> re.subn(r"\b\w{3}\b", "xxx", "foo bar bazr hello world tes")
('xxx xxx bazr hello world xxx', 3) 
```

---

`re.search(pattern, string, flags=0)`

- Text içinde pattern'i araştırır, bulduğu ilk konum bilgisini döner. Ayrıca pattern içinde grup varsa gruplama yapabilir (ayrıntılar bi sonraki bölümde).
- Eğer herhangi bir eşleşme olmazsa `None` döner.

```python
>>> text = "Python is fun!"

>>> r = re.search(r"\bfun", text)
>>> r
<re.Match object; span=(10, 13), match='fun'>

>>> r.start()
10
>>> r.end()
13
```

---

`re.match(pattern, string, flags=0)`

- `re.search()` ile aynıdır. Tek farklı `.search()` tüm string içeriğinde arama yaparken, `.match()` sedece stringin başına bakar.

```python
>>> re.search(r'\d+', '123foobar')
<_sre.SRE_Match object; span=(0, 3), match='123'>
>>> re.search(r'\d+', 'foo123bar')
<_sre.SRE_Match object; span=(3, 6), match='123'>

>>> re.match(r'\d+', '123foobar')
<_sre.SRE_Match object; span=(0, 3), match='123'>
>>> print(re.match(r'\d+', 'foo123bar'))
None
```

---

`re.finditer(pattern, string, flags=0)`

- `.search()` gibi arama yapar ama generator döner.

```python
>>> it = re.finditer(r'\w+', '...foo,,,,bar:%$baz//|')

>>> next(it)
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> next(it)
<_sre.SRE_Match object; span=(10, 13), match='bar'>
>>> next(it)
<_sre.SRE_Match object; span=(16, 19), match='baz'>
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> for i in re.finditer(r'\w+', '...foo,,,,bar:%$baz//|'):
...     print(i)
...
<_sre.SRE_Match object; span=(3, 6), match='foo'>
<_sre.SRE_Match object; span=(10, 13), match='bar'>
<_sre.SRE_Match object; span=(16, 19), match='baz'>
```

---

`re.compile(<regex>, flags=0)`

- Regex objesi oluşturur. Aşağıdaki örnekte her üç kullanım da birbirinin aynısıdır.

```python
result = re.search(<regex>, <string>, <flags>)

re_obj = re.compile(<regex>, <flags>)
result = re.search(re_obj, <string>)

re_obj = re.compile(<regex>, <flags>)
result = re_obj.search(<string>)

---

>>> re.search(r'(\d+)', 'foo123bar')
<_sre.SRE_Match object; span=(3, 6), match='123'>

>>> re_obj = re.compile(r'(\d+)')

>>> re.search(re_obj, 'foo123bar')
<_sre.SRE_Match object; span=(3, 6), match='123'>

>>> re_obj.search('foo123bar')
<_sre.SRE_Match object; span=(3, 6), match='123'>
```

---

**MATCH OBJECT**

- `.search(), .finditer(), .match()` gibi fonksiyonlar, `match` objesi döndürür. Bu obje ile ulaşılabilecek fonksiyonlar ve attribute'ler şunlardır.

| Method                | Returns                                                      |
| --------------------- | ------------------------------------------------------------ |
| `match.group()`       | The specified captured group or groups from `match`          |
| `match.__getitem__()` | A captured group from `match`                                |
| `match.groups()`      | All the captured groups from `match`                         |
| `match.groupdict()`   | A dictionary of named captured groups from `match`           |
| `match.expand()`      | The result of performing backreference substitutions from `match` |
| `match.start()`       | The starting index of `match`                                |
| `match.end()`         | The ending index of `match`                                  |
| `match.span()`        | Both the starting and ending indices of `match` as a tuple   |

| Attribute                  | Meaning                                                      |
| -------------------------- | ------------------------------------------------------------ |
| `match.pos` `match.endpos` | The effective values of the `<pos>` and `<endpos>` arguments for the match |
| `match.lastindex`          | The index of the last captured group                         |
| `match.lastgroup`          | The name of the last captured group                          |
| `match.re`                 | The compiled regular expression object for the match         |
| `match.string`             | The search string for the match                              |

## Regex İfadesinde Gruplama

- `()` işaretleriyle gruplama yapılabilir ve sonrasında bu gruplar yakalanbilir.

```python
>>> re.search('(bar)+', 'foo bar baz')
<_sre.SRE_Match object; span=(4, 7), match='bar'>

>>> re.search('(bar)+', 'foo barbar baz')
<_sre.SRE_Match object; span=(4, 10), match='barbar'>

>>> re.search('(bar)+', 'foo barbarbarbar baz')
<_sre.SRE_Match object; span=(4, 16), match='barbarbarbar'>
```

| Regex    | Interpretation                                              | Matches                                             | Examples                         |
| -------- | ----------------------------------------------------------- | --------------------------------------------------- | -------------------------------- |
| `bar+`   | The `+` metacharacter applies only to the character `'r'`.  | `'ba'` followed by one or more occurrences of `'r'` | `'bar'` `'barr'` `'barrr'`       |
| `(bar)+` | The `+` metacharacter applies to the entire string `'bar'`. | One or more occurrences of `'bar'`                  | `'bar'` `'barbar'` `'barbarbar'` |

```python
>>> re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar')
<_sre.SRE_Match object; span=(0, 9), match='foofoobar'>

>>> re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123')
<_sre.SRE_Match object; span=(0, 12), match='foofoobar123'>

>>> re.search('(foo(bar)?)+(\d\d\d)?', 'foofoo123')
<_sre.SRE_Match object; span=(0, 9), match='foofoo123'>
```

| Regex          | Matches                                |
| -------------- | -------------------------------------- |
| `foo(bar)?`    | `'foo'` optionally followed by `'bar'` |
| `(foo(bar)?)+` | One or more occurrences of the above   |
| `\d\d\d`       | Three decimal digit characters         |
| `(\d\d\d)?`    | Zero or one occurrences of the above   |

- `re.search()` ile ifade aramalarında yakalan pattern, `.groups()` ile gruplama yapılarak yazdırılabilir.

```python
>>> m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')

>>> m
<_sre.SRE_Match object; span=(0, 12), match='foo:quux:baz'>

>>> m.groups()
('foo', 'quux', 'baz')

>>> m.group()
'foo,quux,baz'
>>> m.group(0)
'foo,quux,baz'
>>> m.group(1)
'foo'
>>> m.group(2)
'quux'
>>> m.group(3)
'baz'

>>> m.group(2, 3)
('quux', 'baz')
>>> m.group(3, 2, 1)
('baz', 'quux', 'foo')
```

- `(?P<name><pattern>)` : Gruplama yapılırken grup başına yazılarak gruplara isim verilebilir.

```python
>>> m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')

>>> m.groups()
('foo', 'quux', 'baz')
>>> m.group(1, 2, 3)
('foo', 'quux', 'baz')

>>> m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
>>> m.groups()
('foo', 'quux', 'baz')
>>> m.group('w1', 'w2', 'w3')
('foo', 'quux', 'baz')
>>> m.group(1, 2, 3)
('foo', 'quux', 'baz')
```

- `(?P=<name>)` : Başka bir gruba referans vererek o grupta bulunan karşılığın aynısının bulunmasını ister.

```python
>>> m = re.search(r'(\w+),\1', 'foo,foo')
>>> m
<_sre.SRE_Match object; span=(0, 7), match='foo,foo'>
>>> m.group(1)
'foo'

>>> m = re.search(r'(?P<word>\w+),(?P=word)', 'foo,foo')
>>> m
<_sre.SRE_Match object; span=(0, 7), match='foo,foo'>
>>> m.group('word')
'foo'

>>> m = re.search(r'(?P<word>\w+),(?P=word)', 'foo,bar')
>>> m
None
```

- `(?:<regex>)` : Grup başına yazıldığında o grup yakalanmaz.

```python
>>> m = re.search('(\w+),(?:\w+),(\w+)', 'foo,quux,baz')
>>> m
<re.Match object; span=(0, 12), match='foo,quux,baz'>

>>> m.groups()
('foo', 'baz')
>>> m.group()
'foo,quux,baz'
>>> m.group(1)
'foo'
>>> m.group(2)
'baz'
```

- `(?(<num_or_name>)<yes-regex>|<no-regex>)` : Bu ifadeyle bir grup için koşul yazılır. `(<num_or_name>)` kısmında ismi veya numarası belirtilen grup varsa `yes-regex` kısmı, yoksa `no-regex` kısmı aranır.

```python
>>> regex = r'^(###)?foo(?(1)bar|baz)'

# (?(1)bar|baz) > 1. numaralı grup varsa "bar" ara yoksa "baz" ara
# (###) > 1 numaralı grup
# (###)?foo > ön regex kısmı, "###foo" veya "foo" ile eşleşir.
# Son durumda aranan regex ifadeleri : "###foobar" or "foobaz"

>>> re.search(regex, '###foobar')
<_sre.SRE_Match object; span=(0, 9), match='###foobar'>

>>> print(re.search(regex, '###foobaz'))
None

>>> print(re.search(regex, 'foobar'))
None

>>> re.search(regex, 'foobaz')
<_sre.SRE_Match object; span=(0, 6), match='foobaz'>
```

#### Lookahead and Lookbehind Assertions

- `(?=<lookahead_regex>)` : Yazıldığı yere verilen regex kısmının gelmesini ister ama regex alınırken bu kısım alınmaz. Asıl pattern'den sonra kullanılır.

```python
>>> re.search('foo([a-z]{3})', 'foobar')
<re.Match object; span=(0, 6), match='foobar'>

>>> re.search('foo(?=[a-z]{3})', 'foobar')
<re.Match object; span=(0, 3), match='foo'>

>>> re.search('foo(?=[a-z]{3})', 'foo123')
None
```

- `(?!<lookahead_regex>)` : Yukarıdaki işlemin tersini uygular.

```python
>>> re.search('foo(?=[a-z])', 'foobar')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> print(re.search('foo(?![a-z])', 'foobar'))
None

>>> print(re.search('foo(?=[a-z])', 'foo123'))
None
>>> re.search('foo(?![a-z])', 'foo123')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
```

- `(?<=<lookbehind_regex>)` : Yazıldığı yere verilen regex kısmının gelmesini ister ama regex alınırken bu kısım alınmaz. Asıl pattern'den önce kullanılır.

```python
>>> re.search('(?<=foo)bar', 'foobar')
<_sre.SRE_Match object; span=(3, 6), match='bar'>

>>> print(re.search('(?<=qux)bar', 'foobar'))
None
```

```python
>>> text = "Date : 11.11.2021, Name : James"

>>> re.sub(r"Name : \w+", "Name : xxx", text)
'Date : 11.11.2021, Name : xxx'

>>> re.sub(r"(?<=Name : )\w+", "xxx", text)
'Date : 11.11.2021, Name : xxx'
```

- `(?<!<lookbehind_regex>)` : Yukarıdaki işlemin tersini uygular.

```python
>>> print(re.search('(?<!foo)bar', 'foobar'))
None

>>> re.search('(?<!qux)bar', 'foobar')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
```

#### Miscellaneous Metacharacters

- `(?#...)` : Regex içine yorum yazmaya yarar.

```python
>>> re.search('bar(?#This is a comment) *baz', 'foo bar baz qux')
<_sre.SRE_Match object; span=(4, 11), match='bar baz'>
```

- `|` : Pipe karakteri birden fazla regex grubu arasında `or` işlemi uygular.

```python
>>> re.search('foo|bar|baz', 'bar')
<_sre.SRE_Match object; span=(0, 3), match='bar'>

>>> re.search('foo|bar|baz', 'baz')
<_sre.SRE_Match object; span=(0, 3), match='baz'>

>>> print(re.search('foo|bar|baz', 'quux'))
None
```

```python
>>> re.search('(foo|bar|baz)+', 'foofoofoo')
<_sre.SRE_Match object; span=(0, 9), match='foofoofoo'>

>>> re.search('(foo|bar|baz)+', 'bazbazbazbaz')
<_sre.SRE_Match object; span=(0, 12), match='bazbazbazbaz'>

>>> re.search('(foo|bar|baz)+', 'barbazfoo')
<_sre.SRE_Match object; span=(0, 9), match='barbazfoo'>
```

```python
>>> re.search('([0-9]+|[a-f]+)', '456')
<_sre.SRE_Match object; span=(0, 3), match='456'>

>>> re.search('([0-9]+|[a-f]+)', 'ffda')
<_sre.SRE_Match object; span=(0, 4), match='ffda'>
```

## Regex Flags

| Short Name | Long Name       | Effect                                                       |
| ---------- | --------------- | ------------------------------------------------------------ |
| `re.I`     | `re.IGNORECASE` | Makes matching of alphabetic characters case-insensitive     |
| `re.M`     | `re.MULTILINE`  | Causes start-of-string and end-of-string anchors to match embedded newlines |
| `re.S`     | `re.DOTALL`     | Causes the dot metacharacter to match a newline              |
| `re.X`     | `re.VERBOSE`    | Allows inclusion of whitespace and comments within a regular expression |
| `----`     | `re.DEBUG`      | Causes the regex parser to display debugging information to the console |
| `re.A`     | `re.ASCII`      | Specifies ASCII encoding for character classification        |
| `re.U`     | `re.UNICODE`    | Specifies Unicode encoding for character classification      |
| `re.L`     | `re.LOCALE`     | Specifies encoding for character classification based on the current locale (outdated!) |

```python
# re.IGNORECASE
>>> re.search('a+', 'aaaAAA')
<_sre.SRE_Match object; span=(0, 3), match='aaa'>
>>> re.search('a+', 'aaaAAA', re.I)
<_sre.SRE_Match object; span=(0, 6), match='aaaAAA'>

# re.MULTILINE
>>> s = 'foo\nbar\nbaz'

>>> re.search('^foo', s)
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> print(re.search('^bar', s))
None
>>> print(re.search('foo$', s))
None
>>> re.search('baz$', s)
<_sre.SRE_Match object; span=(8, 11), match='baz'>

>>> re.search('foo$', s, re.M)
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.search('bar$', s, re.M)
<_sre.SRE_Match object; span=(4, 7), match='bar'>
>>> re.search('baz$', s, re.M)
<_sre.SRE_Match object; span=(8, 11), match='baz'>

# re.DOTALL
>>> print(re.search('foo.bar', 'foo\nbar'))
None
>>> re.search('foo.bar', 'foo\nbar', re.S)
<_sre.SRE_Match object; span=(0, 7), match='foo\nbar'>

# re.VERBOSE : Regex tanımında boşluk karakterleri ve yorum satırı kullanmaya izin verir.
>>> regex = r'''^               # Start of string
...             (\(\d{3}\))?    # Optional area code
...             \s*             # Optional whitespace
...             \d{3}           # Three-digit prefix
...             [-.]            # Separator character
...             \d{4}           # Four-digit line number
...             $               # Anchor at end of string
...             '''

>>> re.search(regex, '414.9229', re.VERBOSE)
<_sre.SRE_Match object; span=(0, 8), match='414.9229'>
>>> re.search(regex, '414-9229', re.VERBOSE)
<_sre.SRE_Match object; span=(0, 8), match='414-9229'>

# re.DEBUG
>>> re.search('foo.bar', 'fooxbar', re.DEBUG)
LITERAL 102
LITERAL 111
LITERAL 111
ANY None
LITERAL 98
LITERAL 97
LITERAL 114
<_sre.SRE_Match object; span=(0, 7), match='fooxbar'>

# re.ASCII & re.UNICODE & re.LOCALE
# Several of the regex metacharacter sequences (\w, \W, \b, \B, \d, \D, \s, and \S) require you to assign characters to certain classes like word, digit, or whitespace. The flags in this group determine the encoding scheme used to assign characters to these classes. The possible encodings are ASCII, Unicode, or according to the current locale.
>>> s = '\u0967\u096a\u096c'
>>> s
'१४६'
>>> re.findall("\d", s)
['१', '४', '६']
>>> re.findall("\d", s, re.ASCII)
[]
>>> re.findall("\d", s, re.UNICODE)
['१', '४', '६']
```

- Birden fazla flag, `|` ile birleştirilip kullanılabilir.

```python
>>> re.search('^bar', 'FOO\nBAR\nBAZ', re.I|re.M)
<_sre.SRE_Match object; span=(4, 7), match='BAR'>
```

- Flag işaretleri regex başında `(?<flags>)` ifadesiyle kullanılabilir.

```python
>>> re.search('^bar', 'FOO\nBAR\nBAZ\n', re.I|re.M)
<_sre.SRE_Match object; span=(4, 7), match='BAR'>

>>> re.search('(?im)^bar', 'FOO\nBAR\nBAZ\n')
<_sre.SRE_Match object; span=(4, 7), match='BAR'>
```

- Flag işaretleri grup başında `(?<set_flags>-<remove_flags>:<regex>)` sadece o gruba özel olarak kullanılabilir veya sadece o grup için kullanılması engellenebilir.

```python
>>> re.search('(?i:foo)bar', 'FOObar')
<re.Match object; span=(0, 6), match='FOObar'>

>>> print(re.search('(?i:foo)bar', 'FOOBAR'))
None

>>> print(re.search('(?-i:foo)bar', 'FOOBAR', re.IGNORECASE))
None
```
