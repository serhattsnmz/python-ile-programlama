# Python Bitwise Operatörleri

Python bit (bitwise) operatörler ile değişkenleri karşılaştırarak AND , OR , XOR , NOT , Sağa Kaydırma ve Sola Kaydırma işlemlerini gerçekleştirebilirsiniz. Örnek kullanımları aşağıdan inceleyebilirsiniz.

- `&` operatörü ile elinizdeki bir sayıyı başka bir sayı ile bit düzeyinde AND  işlemine tabi tutabilirsiniz

```python
a = 3
# bit değeri: 0011

b = 5
# bit değeri: 0101

a &= b
#         0011
#(AND)    0101
#-------------
#         0001

print(a)    
# 1
```

- `|` operatörü ile elinizdeki bir sayıyı başka bir sayı ile bit düzeyinde OR  işlemine tabi tutabilirsiniz.

```python
a = 3
# bit değeri: 0011

b = 5
# bit değeri: 0101

a |= b

#         0011
#(OR)     0101
#-------------
#         0111


print(a)    # 7
```

- `^` operatörü ile elinizdeki bir sayıyı başka bir sayı ile bit düzeyinde XOR  işlemine tabi tutabilirsiniz. 

```python
a = 3
# bit değeri: 0011

b = 5
# bit değeri: 0101

a ^= b

#          0011
#(XOR)     0101
#--------------
#          0110


print(a)    # 6
```

- `~` operatörü ile elinizdeki bir sayıyı `~x = -(x+1)`  işlemine tabi tutabilirsiniz. 

```python
a = 3
# bit değeri: 0011

a = ~a

#-(x+1)    0011
#--------------
#         -0100


print(a)    # -4
```

- `>>` operatörü ile elinizdeki bir sayının bit değeri üzerinden sağa kaydırma işlemi yapabilirsiniz. Soldan gelen yeni bitle ise 0 değerini alır.

```python
a = 5
# bit değeri: 0101

a >>= 2
# yeni bit değeri: 0001

print(a)    #1
```

- `<<` operatörü ile elinizdeki bir sayının bit değeri üzerinden sola kaydırma işlemi yapabilirsiniz. Sağdan gelen yeni bitle ise 0 değerini alır.

```python
a = 13
# bit değeri: 1101

a <<= 5
# yeni bit değeri: 110100000

print(a)    #416
```

