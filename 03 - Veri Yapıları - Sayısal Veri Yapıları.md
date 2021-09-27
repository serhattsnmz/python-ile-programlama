# Sayısal Veri Tipleri

- Tamsayılar (Integer)
    - Int değerler için max bir limit yoktur. Çalıştırılan bilgisayarın memory değeri max limittir.
    - Onluk taban dışında tam sayı tanımlamaları için aşağıdaki önekler kullanılır:

| Prefix                                                       | **Interpretation** | **Base** |
| ------------------------------------------------------------ | ------------------ | -------- |
| `0b` (zero + lowercase letter `'b'`) <br />`0B` (zero + uppercase letter `'B'`) | Binary             | 2        |
| `0o` (zero + lowercase letter `'o'`) <br />`0O` (zero + uppercase letter `'O'`) | Octal              | 8        |
| `0x` (zero + lowercase letter `'x'`)<br />`0X` (zero + uppercase letter `'X'`) | Hexadecimal        | 16       |

```python
>>> print(0o10)
8

>>> print(0x10)
16

>>> print(0b10)
2
```

- Ondalıklı Sayılar (Float)
    - Max sınırı : 1.8 x 10 ^ 308
    
    - > Almost all platforms represent Python `float` values as 64-bit “double-precision” values, according to the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754_revision) standard. In that case, the maximum value a floating-point number can have is approximately 1.8 ⨉ 10308. Python will indicate a number greater than that by the string `inf`
    
    - Min sınırı : 5.0 ⨉ 10 ^ -324

```python
>>> a = 4.7
>>> type(a)
<class 'float'>

>>> .77
0.77

>>> 11e5
1100000.0

>>> 4.2e-4
0.00042

""" Max value """
>>> 1.79e308
1.79e+308

>>> 1.8e308
inf

""" Min value"""
>>> 5e-324
5e-324

>>> 1e-325
0.0
```

### Aritmetik Operatörler

- (+) Toplama işlemini gerçekleştirir
- (–) Çıkarma işlemini gerçekleştirir
- (*) Çarpma işlemini gerçekleştirir
- (/) Bölme işlemini gerçekleştirir
- (//) Tam sayı bölme işlemini gerçekleştirir. Cevabın tam kısmını çıktı olarak verir.
- (**) Üs alma işlemini gerçekleştirir. Diğer bir söylemle kuvvet alır.
- (%) Bölme işleminin kalanını hesaplar.

### Atama Operatörleri 

- (+=) Artırarak atama yapar
- (-=) Eksilterek atama yapar
- (*=) Çarparak atama yapar
- (/=) Bölerek atama yapar
- (**=) Üs alarak atama yapar
- (//=) Tamsayı bölmesi yaparak atama yapar
- (%=) Bölme işleminin kalanını hesaplayarak atama yapar
- (<<=) Sola kaydırarak atama yapar
- (>>=) Sağa kaydırarak atama yapar
- (&=) ve (and) bağlacını uygulayarak atama yapar
- (|=) veya (or) bağlacını uygulayarak atama yapar
- (^=) xor uygulayarak atama yapar

## Veri Tipi Dönüşümleri

- `int()`
- `float()`
- `str()`
- Dönüşümlerde hata alınırsa : `ValueError`