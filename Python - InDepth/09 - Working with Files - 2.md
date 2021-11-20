# Working with Files in Python - 2

> Aşağıdaki örnekler, şu dosya yapısına göre hazırlanmıştır:
>
> ```
> my_directory
> ├── file1.py
> ├── file2.csv
> ├── file3.txt
> ├── sub_dir
> │   ├── bar.py
> │   └── foo.py
> ├── sub_dir_b
> │   └── file4.txt
> └── sub_dir_c
>     ├── config.py
>     ├── file5.txt
>     └── sub_dir_d
>         └── file6.txt
> ```

## Directory Listing

- Dizin listeleme için aşağıdaki metotlar kullanılabilir.

1. `os.listdir(<path>)`
    - String listesi türünde dizin içeriğini döner.
    - Parametre verilmezse mevcut dizin içeriğini döner.

```python
>>> import os
>>> dirlist = os.listdir("my_directory")

>>> type(dirlist)
<class 'list'>

>>> for i in dirlist:
...     print(i)
file1.py
file2.csv
file3.txt
sub_dir
sub_dir_b
sub_dir_c
```

2. `os.scandir()`
    - Python 3.5 ile eklenmiştir.
    - Iterator döner. Her iterator elemanı `DirEntry` türündedir.
        - Obje üzerinden dosyanın birçok özelliğine ulaşıbilir.
        - https://docs.python.org/3/library/os.html#os.DirEntry
    - `DirEntry` içindeki `.stat()` üzerinden dosya bilgilerine ulaşılabilir.
        - https://docs.python.org/3/library/os.html#os.DirEntry.stat
    - "Context Manager Protocol"ü desteklediğinden (içinde `__enter__` ve `__exit__`) metotları olduğundan with ile açılabilir.

```python
>>> import os
>>> dirlist = os.scandir("my_directory")

>>> type(dirlist)
<class 'nt.ScandirIterator'>

>>> for i in dirlist:
...     print(i)
<DirEntry 'file1.py'>
<DirEntry 'file2.csv'>
<DirEntry 'file3.txt'>
<DirEntry 'sub_dir'>
<DirEntry 'sub_dir_b'>
<DirEntry 'sub_dir_c'>

>>> with os.scandir("my_directory") as dirlist:
>>> 	print(dir(next(dirlist)))
[..., 'inode', 'is_dir', 'is_file', 'is_symlink', 'name', 'path', 'stat']

>>> with os.scandir("my_directory") as dirlist:
...     for i in dirlist:
...         print(i.inode(), "dir " if i.is_dir() else "file", i.name.ljust(10), i.path)
91479367431163452 file file1.py   my_directory\file1.py
16044073672740934 file file2.csv  my_directory\file2.csv
18295873486290840 file file3.txt  my_directory\file3.txt
14636698789187599 dir  sub_dir    my_directory\sub_dir
25051272927481908 dir  sub_dir_b  my_directory\sub_dir_b
19140298416558134 dir  sub_dir_c  my_directory\sub_dir_c

>>> with os.scandir("my_directory") as dirlist:
...     print(next(dirlist).stat())
os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0, st_atime=1637350691, st_mtime=1637350651, st_ctime=1637350691)
```

3. `pathlib.Path.iterdir()`
    - İşletim sistemine göre `PosixPath` veya `WindowsPath` objesi döner.
    - `.iterdir()` metoduyla, dizin içeriği iterable olarak döndürülebilir.
    - `pathlib.Path` objesinden, dizin ile ilgili birçok bilgi alınabilir ve işlemler yapılabilir. 
        - Bkz : https://realpython.com/python-pathlib/

```python
>>> from pathlib import Path
>>> dirlist = Path("my_directory")

>>> type(dirlist)
<class 'pathlib.WindowsPath'>

>>> dir(dirlist)
[..., 'absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', 'glob', 'group', 'home', 'is_absolute', 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_file', 'is_mount', 'is_relative_to', 'is_reserved', 'is_socket', 'is_symlink', 'iterdir', 'joinpath', 'lchmod', 'link_to', 'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes', 'read_text', 'readlink', 'relative_to', 'rename', 'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink', 'with_name', 'with_stem', 'with_suffix', 'write_bytes', 'write_text']

>>> for i in dirlist.iterdir():
...     print(i)
my_directory\file1.py
my_directory\file2.csv
my_directory\file3.txt
my_directory\sub_dir
my_directory\sub_dir_b
my_directory\sub_dir_c
```

## Using `os.path`

- `os.path` class özelliklerini kullanarak, verdilen path hakkında birçok bilgiye ulaşılabilir.

```python
import os
>>> print(dir(os.path))
[...,
 'abspath',		# Verilen path'in tam yolunu (absulute path) verir.
 'altsep',
 'basename',
 'commonpath',
 'commonprefix',
 'curdir',
 'defpath',
 'devnull',
 'dirname',
 'exists',		# path'in olup olmadığnı verir.
 'expanduser',
 'expandvars',
 'extsep',
 'genericpath',
 'getatime',	# epoc formatında : time of last access of path
 'getctime',	# epoc formatında : time of create date
 'getmtime',	# epoc formatında : time of last modification of path
 'getsize',		# dosyanın veya dizinin boyutunu byte cinsinden verir.
 'isabs',
 'isdir',		# path'in dizin olup olmadığını kontrol eder.
 'isfile',		# path'in dosya olup olmadığını kontrol eder.
 'islink',		# path'in link olup olmadığını kontrol eder.
 'ismount',
 'join',		# İki path parçasını birleştirir. "/" yoksa aralara ekler.
 'lexists',
 'normcase',
 'normpath',
 'os',
 'pardir',
 'pathsep',
 'realpath',
 'relpath',
 'samefile',
 'sameopenfile',
 'samestat',
 'sep',
 'split',		# path'in dosya yolu ile dosya ismini ayırır.
 'splitdrive',
 'splitext',
 'stat',
 'supports_unicode_filenames',
 'sys']
```

```python
# path.abspath
>>> os.path.abspath("my_directory")
'C:\\Users\\serhat\\Desktop\\python-test\\my_directory'

# path.exists
>>> os.path.exists("my_directory/file1.py")
True
>>> os.path.exists("my_directory/file2.py")
False
>>> os.path.exists("my_directory/sub_dir")
True

# times
>>> os.path.getatime("my_directory/sub_dir")
1637353175.8169107
>>> os.path.getctime("my_directory/sub_dir")
1637350624.6791203
>>> os.path.getmtime("my_directory/sub_dir")
1637350716.017144

# path.getsize
>>> os.path.getsize("my_directory")
4096
>>> os.path.getsize("my_directory/file2.csv")
17

# path.isfile
>>> os.path.isfile("my_directory/file1.py")
True

# path.isdir
>>> os.path.isdir("my_directory/file1.py")
False
>>> os.path.isdir("my_directory/sub_dir")
True

# path.join
>>> os.path.join("my_directory", "sub_dir", "bar.py")
'my_directory\\sub_dir\\bar.py'

# path.split
>>> os.path.split("my_directory/file2.csv")
('my_directory', 'file2.csv')
>>> os.path.split("python-test/my_directory/file2.csv")
('python-test/my_directory', 'file2.csv')
```

- Örnekler:

```python
>>> import os
>>> from datetime import datetime
>>> basepath = "my_directory"

	# list only files in a path
    # ---------------------------------------------

>>> for entry in os.listdir(basepath):
...     if os.path.isfile(pth := os.path.join(basepath, entry)):
...         print(pth)
my_directory\file1.py
my_directory\file2.csv
my_directory\file3.txt

	# list only files in a path
    # ---------------------------------------------

>>> [k.name for k in os.scandir(basepath) if k.is_file()]
['file1.py', 'file2.csv', 'file3.txt']

	# list dirs and subdirs
    # ---------------------------------------------

def tree(basepath, prefix = ""):
    for entry in os.scandir(basepath):
        if entry.is_file():
            print("f", prefix + entry.name)
        else:
            print("d", prefix + entry.name)
            tree(os.path.join(basepath, entry.name), prefix + "- ")
        
tree("my_directory")

# f file1.py
# f file2.csv
# f file3.txt
# d sub_dir
# f - bar.py
# f - foo.py
# d sub_dir_b
# f - file4.txt
# d sub_dir_c
# f - config.py
# f - file5.txt
# d - sub_dir_d
# f - - file6.txt

	# Print last modified date
    # ---------------------------------------------
    
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files(basepath):
    dir_entries = os.scandir(basepath)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
get_files("my_directory")

# file1.py        Last modified:  04 Oct 2018
# file3.txt       Last modified:  17 Sep 2018
# file2.txt       Last modified:  17 Sep 2018
```

## Create Directory

- Aşağıdaki metotlarla dizin oluşturulabilir:
    - `os.mkdir()` : 
        - Tek dizin oluşturur, sub dizin oluşturmaz, dizin varsa hata verir.
    - `os.makedirs()` : 
        - Tek dizin oluşturur, sub dizin oluşturabilir, dizin varsa hata verir.
        - Parametre olarak dosya izinleri tanımlanabilir.
    - `pathlib.Path.mkdir()` 
        - Tek dizin oluşturur, sub dizin oluşturabilir, dizin varsa hata verir.

| Function               | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `os.mkdir()`           | Creates a single subdirectory                                |
| `pathlib.Path.mkdir()` | Creates single or multiple directories                       |
| `os.makedirs()`        | Creates multiple directories, including intermediate directories |

```python
>>> import os
>>> import pathlib

>>> os.mkdir("test")
>>> os.mkdir("test")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [WinError 183] Halen varolan bir dosya oluşturulamaz: 'test'
[WinError 183] Halen varolan bir dosya oluşturulamaz: 'test'
    
>>> try:
...     os.mkdir("test")
... except FileExistsError:
...     print("Path exists")
Path exists

>>> os.mkdir("test/sub")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 3] Sistem belirtilen yolu bulamıyor: 'test/sub'
[WinError 3] Sistem belirtilen yolu bulamıyor: 'test/sub'

>>> os.makedirs("test/sub")
>>> os.makedirs('2018/10/05', mode=0o770)

>>> p = pathlib.Path('2018/10/05')
>>> p.mkdir(parents=True)
```

## Traversing Directories with `os.walk()`

- `os.walk()` fonksiyonu ile dizinler ve alt dizineler listelenebilir.
- Generator yapısındadır.
- `next()` ile her eleman çekildiğinde 3 tane bilgi verir:
    1. O an bulunan dizinin ismi (string)
    2. O an bulunan dizinin altındaki dizinler (string listesi)
    3. O an bulunan dizinin altındaki dosyalar (string listesi)
- Bkz : https://docs.python.org/3/library/os.html#os.walk

```python
>>> for dirname, dirs, files in os.walk("my_directory"):
...     print("Dirname : ", dirname)
...     print("Dirs    : ", dirs)
...     print("Files   : ", files, end="\n\n")

Dirname :  my_directory
Dirs    :  ['sub_dir', 'sub_dir_b', 'sub_dir_c']
Files   :  ['file1.py', 'file2.csv', 'file3.txt']

Dirname :  my_directory\sub_dir
Dirs    :  []
Files   :  ['bar.py', 'foo.py']

Dirname :  my_directory\sub_dir_b
Dirs    :  []
Files   :  ['file4.txt']

Dirname :  my_directory\sub_dir_c
Dirs    :  ['sub_dir_d']
Files   :  ['config.py', 'file5.txt']

Dirname :  my_directory\sub_dir_c\sub_dir_d
Dirs    :  []
Files   :  ['file6.txt']
```

## Making Temporary Files and Directories

- `tempfile` modülü kullanılarak geçici dosyalar ve dizinler oluşturulabilir.
    - https://docs.python.org/3/library/tempfile.html
- Geçici dosyalar ve dizinler, bilgisayarın geçici dosya saklama alanlarında (`/tmp` gibi) oluşturulur.

#### a. Temporary Files

- `tempfile.TemporaryFile()` ile geçici dosyalar oluşturulabilir.
    - `tempfile.TemporaryFile(*mode='w+b'*, *buffering=- 1*, *encoding=None*, *newline=None*, *suffix=None*, *prefix=None*, *dir=None*, ***, *errors=None*)`
    - https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryFile
- `mode` parametresi, `open()` fonksiyonunun içindeki mode parametresi ile aynı değerleri alır.
    - https://docs.python.org/3/library/functions.html#open
- `.TemporaryFiles()` return olarak `file-like object` döner. File ile yapılan tüm işlemler burda da yapılabilir. 
    - https://docs.python.org/3/glossary.html#term-file-like-object

```python
from tempfile import TemporaryFile

# Create a temporary file and write some data to it
>>> fp = TemporaryFile('w+t')
>>> fp.write('Hello universe!')
15

# Go back to the beginning and read data from file
>>> fp.seek(0)
>>> fp.read()
'Hello universe!'

# Get filename of temporary file
>>> fp.name
'C:\\Users\\serhat\\AppData\\Local\\Temp\\tmp4ndak9fl'

# Close the file, after which it will be removed
fp.close()
```

- Geçici dosyalar `.close()` ile kapatıldıktan hemen sonra sistemden silinirler.
- `.TemporaryFile()` context manager yapısında olduğundan `with` ile açılabilir.

```python
with TemporaryFile('w+t') as fp:
    fp.write('Hello universe!')
    fp.seek(0)
    fp.read()
# File is now closed and removed
```

#### b. Temporary Directories

- `tempfile.TemporaryDirectory` ile geçici dizinler oluşturulabilir.
    - `tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None, ignore_cleanup_errors=False)`
    - https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory

```python
>>> import os
>>> import tempfile

>>> with tempfile.TemporaryDirectory() as tmpdir:
...     print('Created temporary directory ', tmpdir)
...     os.path.exists(tmpdir)
...
Created temporary directory  /tmp/tmpoxbkrm6c
True

# Directory contents have been removed

>>> tmpdir
'/tmp/tmpoxbkrm6c'
>>> os.path.exists(tmpdir)
False
```

## Delete Files and Directories

#### Delete files

- `os.remove()` ve `os.unlink()` fonksiyonları kullanılarak dosyalar sistemden silinebilir. İki fonksiyon da aynı işlevi görür.

```python
import os

data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data1.txt'
os.remove(data_file)

data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data2.txt'
os.unlink(data_file)
```

- Eğer belirtilen dosyalar sistemde mevcut değilse `FileNotFoundError (OsError)` hatası döner.

```python
>>> import os
>>> path = "foo/bar.jpg"

	# FileNotFoundError

>>> os.remove(path)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 3] Sistem belirtilen yolu bulamıyor: 'foo/bar.jpg'
[WinError 3] Sistem belirtilen yolu bulamıyor: 'foo/bar.jpg'
    
	# Delete file with try/catch
    
>>> try:
...     os.remove(path)
... except FileNotFoundError:
...     print("File not exists!")
File not exists!

>>> try:
...     os.remove(path)
... except OSError:
...     print("File not exists!")
File not exists!

	# Delete file with control os.path.exists()
    
>>> if os.path.exists(path):
...     os.remove(path)

>>> if os.path.isfile(path):
...     os.unlink(path)
```

#### Delete Directories

- Aşağıdaki fonksiyonlar kullanılarak dizinler silinebilir.
    - `os.rmdir()` : Dizin ve altındaki dizinleri siler, dizinler boş değilse hata verir.
    - `pathlib.Path.rmdir()` : Dizin ve altındaki dizinleri siler, dizinler boş değilse hata verir.
    - `shutil.rmtree()` : Dizinleri, altındaki dizinleri ve içindeki tüm dosyaları siler, dosyalar boş değilse hata vermez.

```python
>>> import os
>>> import shutil
>>> from pathlib import Path

>>> path0 = "foo/baz" # exists
>>> path1 = "foo/bar" # not exists
>>> path2 = "sub_dir_c/sub_dir_d" # exists, there are files inside

	# os.rmdir()

>>> os.rmdir(path0)

>>> os.rmdir(path1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 2] Sistem belirtilen dosyayı bulamıyor: 'foo/bar'
[WinError 2] Sistem belirtilen dosyayı bulamıyor: 'foo/bar'
    
>>> os.rmdir(path2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [WinError 145] Dizin boş değil: 'sub_dir_c/sub_dir_d'
[WinError 145] Dizin boş değil: 'sub_dir_c/sub_dir_d'
    
	# pathlib.Path.rmdir()
    
>>> Path(path0).rmdir()
>>> Path(path2).rmdir()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Program Files\Python39\lib\pathlib.py", line 1363, in rmdir
    self._accessor.rmdir(self)
OSError: [WinError 145] Dizin boş değil: 'sub_dir_c\\sub_dir_d'
[WinError 145] Dizin boş değil: 'sub_dir_c\\sub_dir_d'
   
	# shutil.rmtree()

>>> shutil.rmtree(path0)
>>> shutil.rmtree(path2)
```

- ÖZET:

| Function                | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `os.remove()`           | Deletes a file and does not delete directories               |
| `os.unlink()`           | Is identical to `os.remove()` and deletes a single file      |
| `pathlib.Path.unlink()` | Deletes a file and cannot delete directories                 |
| `os.rmdir()`            | Deletes an empty directory                                   |
| `pathlib.Path.rmdir()`  | Deletes an empty directory                                   |
| `shutil.rmtree()`       | Deletes entire directory tree and can be used to delete non-empty directories |

### Copy, Move and Renaming Files and Directories

- `shutil` kütüphanesi ile ilgili ayrıntılı bilgi için bkz: 
    - https://docs.python.org/3/library/shutil.html

- `shutil.copy(src, dest)` : Dosyaları kopyalar. Unix sistemindeki `cp` fonksiyonunu baz alır. Dosyalanın içeriğini ve izinlerini kopyalar ama metadatasını (access time, modif. time etc.) kopyalamaz. Dosya varsa override yapar, hata vermez.

```python
>>> import shutil

>>> src = 'path/to/file.txt'
>>> dst = 'path/to/dest_dir'

>>> shutil.copy(src, dst)
'path/to/dest_dir/file.txt'
```

- `shutil.copytree(src, dest)` : Dizinleri ve tüm içeriğini recursive şekilde kopyalar.

```python
>>> import shutil

>>> shutil.copytree('data_1', 'data1_backup')
'data1_backup'
```

- `shutil.move(src, dest)` : Dosya veya dizini taşır. Eğer dest. varsa, src dosya veya dizinini içine taşır; dest. yoksa src dosya veya dizininin ismini değiştirir.

```python
>>> import shutil

>>> shutil.move('dir_1/', 'backup/')
'backup'
```

- `os.rename(src, dest)`, `pathlib.Path.rename(new_name)` : Dosya veya dizinin ismini değiştirir.

```python
>>> import os
>>> os.rename('first.zip', 'first_01.zip')

>>> from pathlib import Path
>>> data_file = Path('data_01.txt')
>>> data_file.rename('data.txt')
```
