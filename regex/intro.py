import re

# findall search sub
# compile

string = 'test this is a regex test'
print(re.search(r'test', string))
print(re.findall(r'test', string))
print(re.sub(r'test', 'Test', string))  # subs all
print(re.sub(r'test', 'Test', string, count=0))  # subs all
print(re.sub(r'test', 'Test', string, count=1))  # subs first

regex = re.compile(r'test')
print(regex.search(string))
print(regex.findall(string))
print(regex.sub('compile', string))
