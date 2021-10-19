# Python Örnekleri

- String metotlarından chr() ve ord() fonksiyonları kullanarak basit bir decode ve encode fonksiyonları yapma

```python
def encode(deger):
    son = ""
    for k in deger:
        son += chr(ord(k) + 3)
    return son

def decode(deger):
    son = ""
    for k in deger:
        son += chr(ord(k) - 3)
    return son
```