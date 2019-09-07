from lxml import etree


doc = etree.parse(r'./bookstore.xml')


# iterate child of a tree
for child in doc.getroot():
    print(child.tag)


# access one of children
book1 = doc.getroot().getchildren()[0]
# or by shortcut
author = book1[0]


print('-' * 40)
# attribute can be accessed like normal dict
print('book id:', book1.get('id'))

# access text node
print('author:', author.text)

# children can be searched by tag name
print('title:', book1.find('title').text)

# or by the widely used XPath
print('-' * 40)
for x in doc.xpath('//book[price<=5.0]/title'):
    print('title:', x.text)
    print('author:', x.getparent().xpath('//author')[0].text)
    print('price:', x.getparent().xpath('//price')[0].text)


# ref: https://lxml.de/tutorial.html

