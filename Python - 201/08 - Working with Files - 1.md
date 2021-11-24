# Working with Files in Python - 1

- Dosyalar, 
    - Bilgisayarın kalıcı hafızasında bilgi saklamaya yarayan ve içeriği byte'laradan oluşan veri kümeleridir.
    - İçinde raw text olabileceği gibi, ancak belirli programlar aracılığıyla yorumlanan karışık byte kümelerinden oluşabilir.
        - **Raw text dosyaları** direk olarak herhangi bir editör ile açılabilir. Dosya içeriğinde sadece text bulunduğundan okunduğunda direk parse edilebilir. `.txt, .csv, .py` dosyaları örnek gösterilebilir.
        - **Binary dosyaları** ise direk olarak okunmazlar, başka programlarla yorumlanmaya ihtiyaçları vardır. `.doc, .jpg, .png, .xls, .pdf` örnek olarak gösterilebilir.
    - Binary dosyaları içerik olarak 2 kısımdan oluşurlar:
        - Header: Dosyanın metadatasını bulundurur. Hangi türde bir dosya olduğu gibi.
        - Data: Dosyanın yorumlanacak içeriğinin bulunduğu kısımdır.
    - Dosya isimlendirmesinde kullanılan uzantılar, sadece işletim sisteminin dosyayı açarken hangi programa yönlendirmesi gerektiği ile ilgilidir. Bunun dışında bir önemi yoktur ve dosyanın türüne etki etmez. 
    - Dosyalar belli programlarla açıldığında, programlar dosyanın header kısmından (File Signature or Magic Number) yorumlamaya uygun olup olmadığına karar verirler, örneğin `.txt` uzantısına sahip bir resim dosyası, resim gösterici ile uzantısına bakılmaksızın açılabilir.
        - File signature (Magic Number) için bkz: https://en.wikipedia.org/wiki/List_of_file_signatures

> _**Extra Bilgi**_
>
> Linux'ta `oc` komutuyla dosyaların byte içerikleri yazdırılabilir.
>
> ```bash
> └─[$]> od -N 100 -t c pic.jpg
> 0000000 377 330 377 340  \0 020   J   F   I   F  \0 001 001 001  \0   d
> 0000020  \0   d  \0  \0 377 376  \0   N   F   i   l   e       s   o   u
> 0000040   r   c   e   :       h   t   t   p   :   /   /   w   w   w   .
> 0000060   i   t   .   i   i   t   b   .   a   c   .   i   n   /   a   r
> 0000100   n   d   g   /   d   o   k   u   w   i   k   i   /   i   n   d
> 0000120   e   x   .   p   h   p   /   F   i   l   e   :   U   s   e   r
> 0000140   .   j   p   g
> 
> └─[$]> od -N 100 -t c -t x1 pic.jpg
> 0000000 377 330 377 340  \0 020   J   F   I   F  \0 001 001 001  \0   d
>          ff  d8  ff  e0  00  10  4a  46  49  46  00  01  01  01  00  64
> 0000020  \0   d  \0  \0 377 376  \0   N   F   i   l   e       s   o   u
>          00  64  00  00  ff  fe  00  4e  46  69  6c  65  20  73  6f  75
> 0000040   r   c   e   :       h   t   t   p   :   /   /   w   w   w   .
>          72  63  65  3a  20  68  74  74  70  3a  2f  2f  77  77  77  2e
> 0000060   i   t   .   i   i   t   b   .   a   c   .   i   n   /   a   r
>          69  74  2e  69  69  74  62  2e  61  63  2e  69  6e  2f  61  72
> 0000100   n   d   g   /   d   o   k   u   w   i   k   i   /   i   n   d
>          6e  64  67  2f  64  6f  6b  75  77  69  6b  69  2f  69  6e  64
> 0000120   e   x   .   p   h   p   /   F   i   l   e   :   U   s   e   r
>          65  78  2e  70  68  70  2f  46  69  6c  65  3a  55  73  65  72
> 0000140   .   j   p   g
>          2e  6a  70  67
> ```
>
> Ayrıca `hexdump (hd)` programı da kullanılabilir.
>
> ```bash
> └─[$]> hd -n 100 pic.jpg
> 00000000  ff d8 ff e0 00 10 4a 46  49 46 00 01 01 01 00 64  |......JFIF.....d|
> 00000010  00 64 00 00 ff fe 00 4e  46 69 6c 65 20 73 6f 75  |.d.....NFile sou|
> 00000020  72 63 65 3a 20 68 74 74  70 3a 2f 2f 77 77 77 2e  |rce: http://www.|
> 00000030  69 74 2e 69 69 74 62 2e  61 63 2e 69 6e 2f 61 72  |it.iitb.ac.in/ar|
> 00000040  6e 64 67 2f 64 6f 6b 75  77 69 6b 69 2f 69 6e 64  |ndg/dokuwiki/ind|
> 00000050  65 78 2e 70 68 70 2f 46  69 6c 65 3a 55 73 65 72  |ex.php/File:User|
> 00000060  2e 6a 70 67                                       |.jpg|
> 00000064
> 
> └─[$]> hd -n 100 dog2.png
> 00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
> 00000010  00 00 00 dc 00 00 01 4a  08 06 00 00 00 76 12 31  |.......J.....v.1|
> 00000020  6b 00 00 00 01 73 52 47  42 00 ae ce 1c e9 00 00  |k....sRGB.......|
> 00000030  00 09 70 48 59 73 00 00  28 c1 00 00 28 c1 01 28  |..pHYs..(...(..(|
> 00000040  3c 5d 19 00 00 01 59 69  54 58 74 58 4d 4c 3a 63  |<]....YiTXtXML:c|
> 00000050  6f 6d 2e 61 64 6f 62 65  2e 78 6d 70 00 00 00 00  |om.adobe.xmp....|
> 00000060  00 3c 78 3a                                       |.<x:|
> 00000064
> ```
>
> 

>_**Extra Bilgi**_
>
>End of file (EOF): Dosyanın bittiğini belirten özel bir karakterdir. Eskiden bu karakter (0x03) dosyaların sonuna eklenip, dosyalarını bittiği yer işaretlenirdir. Günümüzdeki işletim sistemleri dosyaların boyutlarını (kaç byte yer kapladığını) dosyaların başlangıç konumlarıyla birlikte tuttuklarından, artık EOF karakteri kullanılmıyor. 
>
>Bkz: 
>
>- https://unix.stackexchange.com/questions/315151/whats-the-last-character-in-a-file
>- https://stackoverflow.com/questions/24991803/where-is-hex-code-of-the-eof-character
>- https://latedev.wordpress.com/2012/12/04/all-about-eof/

- Dosya isimleri, bulundukları path ile belirlenir. `/home/user` dizini altındaki `cat.txt` dosyasının tam dosya ismi `/home/user/cat.txt`'dir.
    - Dosyalarla işlem yapılırken `relative path` olarak belli bir dizinden itiraberen isimlendirme yapılabilir, fakat işletim sistemlerinde dosyaların tam yollarıyla (`absulute path`) kaydedildiği ve gerçek dosya isimlerinin bu olduğu unutulmamalıdır.

#### Satır Sonu Karakterleri

- Satır sonu karakteri (End of line / EOL or Line Break), bir satırdan yeni bir satıra geçerken eklenen karakterdir.
- Bu karakter, herhangi bir editörde `Enter` ile eklenir ve görsel olarak görünmez.
- International Organization for Standardization (ISO) tarafından, satır sonu karakteri `CR+LF` veya sadece `LF` olarak standartlaştırılmıştır.
    - LF : Line Feed or `\n`
    - CR : Carrige Return or `\r`
- Windows işletim sistemi CR+LF (`\r\n`) kullanırken, Unix ve Mac sistemler satır sonu için LF (`\n`) kullanmaktadırlar.
    - Çok nadir programlar haricinde satır sonunun değişik olması görsel açıdan sorun çıkarmamaktadır.
    - Bununla birlikte proglamada bir dosya satırlarına split edileceği zaman bu ayrıma dikkat edilmesi gerekir.
- (`od` komutuyla satır sonu karakterler incelenebilir.)

#### Chracter Encoding

- Karakterler işlenirken (okunurken veya yazılırken) byte'lar ile karakterler arasında çevrim işlemleri yapılır (çünkü her bilgi hafızaya byte olarak kaydedilir).
- Bu çevrim işlemleri yapılırken kodlama standarları esas alınır. 
- Bu standartlar çok fazla olmasına ve farklı diller için farklı standartlar geliştirilmiş olunmasına karşın, temelde iki encoding standartı kullanılır.
    - **ASCII** : En temel karakter kodlama standartıdır. 128 karakterin byte karşılığını bulundurur. 
    - **Unicode (UTF8)** : En geniş karakter kodlama standartıdır. 1.114.112 karakterin byte karşılığını bulundurur.

## Dosya Açma ve Kapatma

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

```python
file = open('dog_breeds.txt')
# File processing
file.close()
```

- Dosyalar `open()` fonksiyonu ile açıldığında `read-only (salt okunur)` moda geçerler. Bu nedenle dosyaların işlemler bittikten sonra kapatılması gerekir. 
- Dosyalar açıldıktan sonra kapatılmadan önce hataya düşerse, dosya kapatılması tamamlanmadığından dosya hatası alınır ve tekrar kullanılmazlar. Bunu engellemek için `try-finally` blokları kullanılabilir.

```python
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()
```

- Dosyaları otomatik olarak kapatmanın bir diğer yolu da `with` kullanmaktır. Blok bittiğinde `with` ile açılan dosya otomatik olarak kapatılır.

```python
with open('dog_breeds.txt') as reader:
    # Further file processing goes here
```

#### Dosya açma metotları

- Dosyalar `open()` metoduyla açıldığında default olarak `read` modunda açılırlar. Fonksiyona ikinci bir parametre verilerek açılma metodu belirlenebilir.

| Character                  | Meaning                                                      |
| -------------------------- | ------------------------------------------------------------ |
| `'r'`                      | Open for reading (default)                                   |
| `'w'`                      | Open for writing, truncating (overwriting) the file first, create file if not exists |
| `'x'`                      | Open for exclusive creation, failing if the file already exists |
| `'a'`                      | Open for writing, appending to the end of the file if it exists |
| `'b'` (`rb, r+b, wb, w+b`) | Open in binary mode (read/write using byte data)             |
| `'+'` (`r+, w+`)           | Open for updating (reading and writing)                      |

```python
with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here
```

#### File encoding

- Dosyalar açıldığında encoding türü `open()` fonksiyonu içinde `encoding` parametresi ile belirlenebilir.
- Varsayılan encoding değeri, kullanılan platforma göre değişiklik gösterir. (Bkz : https://docs.python.org/3.8/library/functions.html#open)

>In text mode, if *encoding* is not specified the encoding used is platform dependent: `locale.getpreferredencoding(False)` is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave *encoding* unspecified.)

```python
>>> f = open("example.txt")
>>> f.read()
'TÃ¼rkÃ§e kelimeler'
>>> f.close()

>>> f = open("example.txt", encoding="utf8")
>>> f.read()
'Türkçe kelimeler'
>>> f.close()
```

## Dosya Okuma ve Yazma

#### Reading file

- Dosyalar açıldıktan sonra aşağıdaki metotlar kullanılarak okuma yapılabilir.
    - `read()` : Verilen byte boyutuna göre veya tüm dosyayı okur.
    - `readline()` : Verilen karakter sayısına göre veya sıradaki satırı okur.
    - `readlines()` : Tüm dosyayı okuyup liste döndürür.

| Method                                                       | What It Does                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`.read(size=-1)`](https://docs.python.org/3.7/library/io.html#io.RawIOBase.read) | This reads from the file based on the number of `size` bytes. If no argument is passed or `None` or `-1` is passed, then the entire file is read. |
| [`.readline(size=-1)`](https://docs.python.org/3.7/library/io.html#io.IOBase.readline) | This reads at most `size` number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or `None` or `-1` is passed, then the entire line (or rest of the line) is read. |
| [`.readlines()`](https://docs.python.org/3.7/library/io.html#io.IOBase.readlines) | This reads the remaining lines from the file object and returns them as a list. |

```python
>>> with open('dog_breeds.txt', 'r') as reader:
>>>     # Read & print the entire file
>>>     print(reader.read())
Pug
Jack Russell Terrier
English Springer Spaniel
...

>>> with open('dog_breeds.txt', 'r') as reader:
>>>     # Read & print the first 5 characters of the line 5 times
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
Pug

Jack
Russe
ll Te
rrier

>>> f = open('dog_breeds.txt')
>>> f.readlines()  # Returns a list object
['Pug\n', 'Jack Russell Terrier\n', 'English Springer Spaniel\n', 'German Shepherd\n']

>>> f = open('dog_breeds.txt')
>>> list(f)
['Pug\n', 'Jack Russell Terrier\n', 'English Springer Spaniel\n', 'German Shepherd\n']
```

#### Read file iteration

- Büyük boyutlu dosyaları `read()` veya `readlines()` metodlarından biriyle parametre olmadan okumak, tüm içeriğin hafızaya kaydedilmesi anlamına gelir ve bu durum RAM yönetimi açısından sıkıntılıdır.
- Bunun yerine dosyalar `readline()` kullanılarak kısım kısım okunabilir.

```python
>>> with open('dog_breeds.txt', 'r') as reader:
>>>     # Read and print the entire file line by line
>>>     line = reader.readline()
>>>     while line != '':  # The EOF char is an empty string
>>>         print(line, end='')
>>>         line = reader.readline()
Pug
Jack Russell Terrier
English Springer Spaniel
...
```

- Dosya açarken oluşturulan `TextIOWrapper` nesnesi generator yapısındadır ve döngüye alındığında dosya içeriğini satır satır döner. Bu yöntemi kullanmak hem daha basittir hem de RAM yönetimi açısından daha uygundur.

```python
>>> with open('dog_breeds.txt', 'r') as reader:
>>>     for line in reader:
>>>         print(line, end='')
Pug
Jack Russell Terrier
English Springer Spaniel
...
```

#### Writing to file

- Dosyalar yazma modunda açıldığında aşağıdaki metotlarla yazma gerçekleştirilir.
    - `.write()` : Verilen string değişkeni dosyaya yazar.
    - `.writelines()` : Verilen listeyi tek tek dosyaya yazar. Elemanlar sonuna satır sonu karakteri eklemez.

| Method             | What It Does                                                 |
| ------------------ | ------------------------------------------------------------ |
| `.write(string)`   | This writes the string to the file.                          |
| `.writelines(seq)` | This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s). |

## Moving the Read/Write Pointer

- Dosyalar okunduğunda veya yazıldığında, okunma veya yazılma konumunu belirten imlece pointer denir. Dosyalar `r` modunda açıldığında pointer dosyanın başında konumlanır, `a` modunda açıldığında dosyanın sonunda konumlanır. `w` modunda açılırsa dosyanın içeriği silinir ve pointer dosyanın başında konumlanır.
- Dosyada pointer'ın nerede olduğunu `.tell()` fonksiyonu ile öğrenebiliriz. 
- Dosyada pointer'ı `.seek(offset, from_where)` ile hareket ettirebiliriz.
    - from_where = 0 : dosyanın başından say
    - from_where = 1 : pointer'ın mevcut konumundan itibaren say
    - from_where = 2 : dosyanın sonundan say
    - offst = x : Şu kadar ilerle

```python
>>> f = open("test.txt", "w")
>>> f.write("Hello World!")
12
>>> f.close()

>>> f = open("test.txt", "r")
>>> f.tell()
0

>>> f.read(1)
'H'
>>> f.tell()
1
>>> f.read(2)
'el'
>>> f.tell()
3
>>> f.read()
'lo World!'
>>> f.tell()
12
>>> f.read()
''

>>> f.seek(0,0)
0
>>> f.read()
'Hello World!'
```

## Creating Custom Context Manager

- Dosya açma, kapatma ve okuma durumları için özelleştirilmiş context manager sınıfları oluşturulabilir.
- Sınıflarda aşağıdaki magic fonksiyonlar kullanılabilir:
    - `__enter()__` : Class `with` ile çağrıldığında çalıştırılır.
    - `__exit()__` : Class with ile açılmışsa, `with` bitiminde çalıştırılır.

```python
class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    # Additional methods implemented below
    
with my_file_reader('dog_breeds.txt') as reader:
    # Perform custom class operations
    pass
```

- Örnek bir kullanım:
    - Dosyanın uzantısı `__init__` içinde kontrol edilir.
    - `__enter()__` içinde dosya byte olarak açılır ve magic signature kontrolü yapılır.
    - `__exit()__` içinde dosya kapatılır.
    - `__iter()__` ve `__next()__` kullanılarak dosyadan sırayla dosya okuyan generator oluşturulur.
    - `__next()__` içinde nesneden çekilen çıktıya şekil verilir.

```python
class PngReader():
    # Every .png file contains this in the header.  Use it to verify
    # the file is indeed a .png.
    _expected_magic = b'\x89PNG\r\n\x1a\n'

    def __init__(self, file_path):
        # Ensure the file has the right extension
        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' extension")
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')

        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError("The File is not a properly formatted .png file!")

        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        # This and __next__() are used to create a custom iterator
        # See https://dbader.org/blog/python-iterators
        return self

    def __next__(self):
        # Read the file in "Chunks"
        # See https://en.wikipedia.org/wiki/Portable_Network_Graphics#%22Chunks%22_within_the_file

        initial_data = self.__file_object.read(4)

        # The file hasn't been opened or reached EOF.  This means we
        # can't go any further so stop the iteration by raising the
        # StopIteration.
        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            # Each chunk has a len, type, data (based on len) and crc
            # Grab these values and return them as a tuple
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc
```

```python
>>> with PngReader('jack_russell.png') as reader:
>>>     for l, t, d, c in reader:
>>>         print(f"{l:05}, {t}, {c}")
00013, b'IHDR', b'v\x121k'
00001, b'sRGB', b'\xae\xce\x1c\xe9'
00009, b'pHYs', b'(<]\x19'
00345, b'iTXt', b"L\xc2'Y"
...
```