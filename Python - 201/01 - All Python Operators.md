# Arithmetic Operators

| Operator     | Example  | Meaning                                               | Result                                                       |
| ------------ | -------- | ----------------------------------------------------- | :----------------------------------------------------------- |
| `+` (unary)  | `+a`     | **Unary Positive**                                    | `a` In other words, it doesn’t really do anything. It mostly exists for the sake of completeness, to complement **Unary Negation**. |
| `+` (binary) | `a + b`  | **Addition**                                          | Sum of `a` and `b`                                           |
| `-` (unary)  | `-a`     | **Unary Negation**                                    | Value equal to `a` but opposite in sign                      |
| `-` (binary) | `a - b`  | **Subtraction**                                       | `b` subtracted from `a`                                      |
| `*`          | `a * b`  | **Multiplication**                                    | Product of `a` and `b`                                       |
| `/`          | `a / b`  | **Division**                                          | Quotient when `a` is divided by `b`. The result always has type `float`. |
| `%`          | `a % b`  | **Modulo**                                            | Remainder when `a` is divided by `b`                         |
| `//`         | `a // b` | **Floor Division** (also called **Integer Division**) | Quotient when `a` is divided by `b`, rounded to the next smallest whole number |
| `**`         | `a ** b` | **Exponentiation**                                    | `a` raised to the power of `b`                               |

# Comparison Operators

| Operator | Example  | Meaning                      | Result                                                       |
| -------- | -------- | ---------------------------- | ------------------------------------------------------------ |
| `==`     | `a == b` | **Equal to**                 | `True` if the value of `a` is equal to the value of `b` `False` otherwise |
| `!=`     | `a != b` | **Not equal to**             | `True` if `a` is not equal to `b` `False` otherwise          |
| `<`      | `a < b`  | **Less than**                | `True` if `a` is less than `b` `False` otherwise             |
| `<=`     | `a <= b` | **Less than or equal to**    | `True` if `a` is less than or equal to `b` `False` otherwise |
| `>`      | `a > b`  | **Greater than**             | `True` if `a` is greater than `b` `False` otherwise          |
| `>=`     | `a >= b` | **Greater than or equal to** | `True` if `a` is greater than or equal to `b` `False` otherwise |

# Logical Operators

| Operator | Example   | Meaning                                                      |
| -------- | --------- | ------------------------------------------------------------ |
| `not`    | `not x`   | `True` if `x` is `False` `False` if `x` is `True` (Logically reverses the sense of `x`) |
| `or`     | `x or y`  | `True` if either `x` or `y` is `True` `False` otherwise      |
| `and`    | `x and y` | `True` if both `x` and `y` are `True` `False` otherwise      |

# Bitwise Operators

| Operator | Example  | Meaning                        | Result                                                       |
| -------- | -------- | ------------------------------ | ------------------------------------------------------------ |
| `&`      | `a & b`  | bitwise **AND**                | Each bit position in the result is the logical **AND** of the bits in the corresponding position of the operands. (`1` if both are `1`, otherwise `0`.) |
| `|`      | `a | b`  | bitwise **OR**                 | Each bit position in the result is the logical **OR** of the bits in the corresponding position of the operands. (`1` if either is `1`, otherwise `0`.) |
| `~`      | `~a`     | bitwise **negation**           | Each bit position in the result is the logical negation of the bit in the corresponding position of the operand. (`1` if `0`, `0` if `1`.) |
| `^`      | `a ^ b`  | bitwise **XOR (exclusive OR)** | Each bit position in the result is the logical **XOR** of the bits in the corresponding position of the operands. (`1` if the bits in the operands are different, `0` if they are the same.) |
| `>>`     | `a >> n` | **Shift right** `n` **places** | Each bit is shifted right `n` places.                        |
| `<<`     | `a << n` | **Shift left** `n` **places**  | Each bit is shifted left `n` places.                         |

```python
>>> '0b{:04b}'.format(0b1100 & 0b1010)
'0b1000'
>>> '0b{:04b}'.format(0b1100 | 0b1010)
'0b1110'
>>> '0b{:04b}'.format(0b1100 ^ 0b1010)
'0b0110'
>>> '0b{:04b}'.format(0b1100 >> 2)
'0b0011'
>>> '0b{:04b}'.format(0b0011 << 2)
'0b1100'
```

# Identity Operators

| Operator | Example      | Meaning                    |
| -------- | ------------ | -------------------------- |
| `is`     | `a is b`     | `True` if `id(a) == id(b)` |
| `is not` | `a is not b` | `True` if `id(a) != id(b)` |

```python
>>> x = 1001
>>> y = 1000 + 1
>>> print(x, y)
1001 1001

>>> x == y
True
>>> x is y
False

>>> a = 'I am a string'
>>> b = a
>>> id(a)
55993992
>>> id(b)
55993992

>>> a is b
True
>>> a == b
True
```

# Shorthand Augmented Assignment

| Arithmetic                    | Bitwise               |
| ----------------------------- | --------------------- |
| `+` `-` `*` `/` `%` `//` `**` | `&` `|` `^` `>>` `<<` |

```python
x <op>= y
x = x <op> y
```

```python
>>> a = 10
>>> a = a + 5
>>> a += 5

>>> b = "serhat"
>>> b = b + " sönmez"
>>> b *= " sönmez"
```

# Chaining Comparison Operators

- Birden fazla `and` ile yapılan karşılaştırma adımının tek bir adımda yazılmasıdır.
- Her iki karşılaştırma sırayla kendi arasında karşılaştırılarak sonuca gidilir.

```python
>>> 1 < 2 and 2 < 3
True
>>> 1 < 2 < 3
True

>>> 1 < 2 < 1
False
>>> 1 == 1.0 < 0.5
False
>>> 1 == 1.0 == True
True
>>> 1 < 3 > 2
True
>>> 1 < 2 < 3 < 4 < 5
True
>>> "b" in "aba" in "cabad" < "cabae"
True
```

- `Short-Circuit Chain Evaluation` kuralları burda da geçerlidir.

```python
>>> 2 < "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
    
>>> 3 < 2 < "2"
False

>>> 3 < 2 < (1//0)
False
```

# Operator Precedence

|                        | Operator                                         | Description                                                  |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| **lowest precedence**  | `or`                                             | Boolean OR                                                   |
|                        | `and`                                            | Boolean AND                                                  |
|                        | `not`                                            | Boolean NOT                                                  |
|                        | `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not` | comparisons, identity                                        |
|                        | `|`                                              | bitwise OR                                                   |
|                        | `^`                                              | bitwise XOR                                                  |
|                        | `&`                                              | bitwise AND                                                  |
|                        | `<<`, `>>`                                       | bit shifts                                                   |
|                        | `+`, `-`                                         | addition, subtraction                                        |
|                        | `*`, `/`, `//`, `%`                              | multiplication, division, floor division, [modulo](https://realpython.com/python-modulo-operator/) |
|                        | `+x`, `-x`, `~x`                                 | unary positive, unary negation, bitwise negation             |
| **highest precedence** | `**`                                             | exponentiation                                               |
