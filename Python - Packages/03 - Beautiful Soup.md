# Beautiful Soup

( DOC : https://www.crummy.com/software/BeautifulSoup/bs4/doc/ )

- Parser çeşitleri ve kurulumları

```python
>>> from bs4 import BeautifulSoup
>>> s = BeautifulSoup('<p class="body" id="test"></p>', 'html.parser')
```

- Örnekler (source : statics/files/soup-example.html)

```python
>>> from bs4 import BeautifulSoup
>>> def opn():
...     with open("./statics/files/soup-example.html") as f:
...         return BeautifulSoup(f.read(), "html.parser")
>>> soup = opn()

	# getting elements by tag name

>>> soup.html.title
<title>A simple example for Beautiful Soup!</title>

	# elements name and contents

>>> soup.html.title.name
'title'
>>> soup.html.title.text
'A simple example for Beautiful Soup!'
>>> soup.html.title.string
'A simple example for Beautiful Soup!'

	# elements attributes

>>> soup.html.meta
<meta content="Simple Project" name="description"/>
>>> soup.html.meta["content"]
'Simple Project'
>>> soup.html.meta.attrs
{'name': 'description', 'content': 'Simple Project'}

>>> soup.body.p
<p class="cls1 cls2" data-foo="bar" id="part1">Foo bar</p>
>>> soup.body.p.attrs
{'id': 'part1', 'class': ['cls1', 'cls2'], 'data-foo': 'bar'}
>>> soup.body.p["class"]
['cls1', 'cls2']

	# search in html by tag ( find() - find_all() )
    
>>> soup.find("p")
<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>
>>> soup.find("p", class_="cls3")
<p class="cls3" data-baz="foo" id="part2">foo bar</p>
>>> soup.find("p", id="part1")
<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>
>>> soup.find("p", class_="cls3", id="part2")
<p class="cls3" data-baz="foo" id="part2">foo bar</p>

>>> soup.find_all("p")
[<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>, <p class="cls3" data-baz="foo" id="part2">foo bar</p>]
>>> soup.find_all("p", limit=1)
[<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>]
>>> soup.find_all("p", id="part2")
[<p class="cls3" data-baz="foo" id="part2">foo bar</p>]
>>> soup.find_all("p", class_="cls2")
[<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>]

	# search in html by attribute
    
>>> soup.find("a")
<a href="example.com" id="part3">Example web page</a>
>>> soup.find(href="example.com")
<a href="example.com" id="part3">Example web page</a>
>>> soup.find(id = "part3")
<a href="example.com" id="part3">Example web page</a>

>>> soup.find(data-foo="bar")
## Syntax error!
>>> soup.find(attrs={"data-foo" : "bar"})
<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>

	# css selector
    
>>> soup.select("p")
[<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>, <p class="cls3" data-baz="foo" id="part2">foo bar</p>]
>>> soup.select("body a")
[<a href="example.com" id="part3">Example web page</a>]
>>> soup.select("#part1")
[<p class="cls1 cls2" data-foo="bar" id="part1">foo bar</p>]
>>> soup.select("p.cls3")
[<p class="cls3" data-baz="foo" id="part2">foo bar</p>]
>>> soup.select("p:nth-of-type(2)")
[<p class="cls3" data-baz="foo" id="part2">foo bar</p>]

# Other find methods
	# find_parent() and find_parents()
	# find_next_siblings() and find_next_sibling()
    # find_previous_siblings() and find_previous_sibling()
    # find_all_next() and find_next()
    # find_all_previous() and find_previous()
    
  	# Going down ( .contents - .children )
    
>>> soup.find("div", id="part4").contents
['\n', <p>foo</p>, '\n', <p>bar</p>, '\n', <p>baz</p>, '\n']
>>> soup.find("div", id="part4").children
<list_iterator object at 0x000001951B6BE1C0>
>>> [k for k in soup.find("div", id="part4").children]
['\n', <p>foo</p>, '\n', <p>bar</p>, '\n', <p>baz</p>, '\n']
>>> [k for k in soup.find("div", id="part4").children if k != "\n"]
[<p>foo</p>, <p>bar</p>, <p>baz</p>]

	# Going up ( .parent - .parents )
    
>>> soup.find(id="part6")
<p id="part6">foo</p>
>>> soup.find(id="part6").parent
<div id="part5">
    <p id="part6">foo</p>
    <p>bar</p>
</div>
>>> soup.find(id="part6").parents
<generator object PageElement.parents at 0x000001951B4D2BA0>

	# Going sideway ( .next_sibling - .next_siblings - .previous_sibling - .previous_siblings )
    
>>> soup.find(id="part6").next_sibling
'\n'
>>> soup.find(id="part6").next_sibling.next_sibling
<p>bar</p>
>>> soup.find(id="part6").next_siblings
<generator object PageElement.next_siblings at 0x0000019520E19F90>
>>> [k for k in soup.find(id="part6").next_siblings]
['\n', <p>bar</p>, '\n']

>>> soup.find(id="part6").previous_sibling
'\n'
>>> [k for k in soup.find(id="part6").previous_siblings]
['\n']
```

