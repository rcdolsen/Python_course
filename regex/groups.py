# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

# print(re.findall(r'(<([dpiv]{1,3})>.*?<\/\2>)', texto))

# tags = re.findall(r'(<([dpiv]{1,3})>(.*?)<\/\2>)', texto)
tags = re.findall(r'(<([dpiv]{1,3})>(?:.*?)<\/\2>)', texto)

# named group -> (?P<tag>...) ... (?P=tag)
tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.*?)<\/(?P=tag)>', texto)

pprint(tags)
print('')

nif = '147.852.963-12'
nif2 = 'a 147.852.963-12 -12'
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', nif))

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', nif))

print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', nif2))

print(re.sub(r'(<(.*?)>)(.*?)(<\/\2>)', r'\1 need "\3" more\4', texto))


# for tag in tags:
#     # print(tag)
#     one, two, three = tag
#     print('big:', one)
#     print('tag:', two)
#     print('inner:', three)
