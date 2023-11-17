# JSON - API

```python
import urllib.request as request
import json
# JavaScript Object Notation - JSON
"""
from - https://www.json.org/json-en.html
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write.
It is easy for machines to parse and generate.
It is based on a subset of the
JavaScript Programming Language Standard ECMA-262 3rd Edition - December 1999.
JSON is a text format that is completely language independent but uses conventions
that are familiar to programmers of the C-family of languages,
including C, C++, C#, Java, JavaScript, Perl, Python, and many others.
These properties make JSON an ideal data-interchange language.
"""

myurl = 'https://jc-testing.juniata.edu/sampledata/swimmers.json'

with request.urlopen(myurl) as response:
    source = response.read()
    data = json.loads(source)
"""
firstName
lastName
swimevents
sy
hometown
highschool
"""
def dowriteln(dotme):
    lineme =''
    for i in range(dotme):
        lineme += "-"
    # lineme += "\n"
    print(lineme)

print(data)
dowriteln(10)
#type(data)
print(len(data))
for i in range(len(data)): 
    print(data[i]['firstName'])
    dowriteln(10)
    print("All events...")
    print((data[i]['swimevents']))
    dowriteln(10)
    print("Individual event(s)..")
    pprint = ''
    for j in range(len(data[i]['swimevents'])):
        # print(data[i]['swimevents'][j])
        if j == 0:
            pprint += data[i]['swimevents'][j]
        else:
            pprint += ", " + data[i]['swimevents'][j]
    print(pprint)
    dowriteln(20)
    dowriteln(20)
```