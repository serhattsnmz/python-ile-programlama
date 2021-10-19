# Diğer Veri Tipleri

## Boolean Veri Tipi

* `True` ve `False` olmak üzere iki değeri vardır.

```python
>>> type(False)
<class 'bool'>
>>> type(True)
<class 'bool'>
```

- Python dilinde boolean ifadeler sayısal olarak `1` ve `0`'a tekabül eder. Sayısal ifadelerle yapılan tüm işlemler boolean ifadeler için de geçerlidir.

```python
>>> True == 1
True
>>> False == 0
True
>>> True + (False / True)
1.0
```

- Boolean ifadelerin sayısal olarak kabul edilmesi bazı durumlarda işleri kolaylaştırabilir:

```python
>>> example = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra."
>>> contains_t = ["t" in item for item in example.split(" ")]
>>> contains_t
[False, False, False, True, True, True, False, True, False, True]
>>> sum(contains_t)
5
```

