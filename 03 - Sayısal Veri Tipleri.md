# Sayısal Veri Tipleri

- Tamsayılar (Integer)
    - Int değerler için max bir limit yoktur. Çalıştırılan bilgisayarın memory değeri max limittir.
- Ondalıklı Sayılar (Float)
    - Max sınırı : 1.8 x 10 ^ 308

```python
>>> a = 4.7
>>> type(a)
<class 'float'>

>>> a = .77
>>> a
0.77

>>> a = 11e5
>>> a
1100000.0

>>> 1.79e308
1.79e+308
>>> 1.8e308
inf
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