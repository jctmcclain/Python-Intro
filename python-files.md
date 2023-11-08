## Opening and Reading 
-----
```python 
print('open a text file')
filename = 'mytext.txt'
f = open(filename)

print('Read the file')
contents = f.read()

f.close()

print('Print out the contents \n')
print(contents)

for line in contents; 
	print(line + '\n')


```

## Read vs. Readline
-----
```python
f = open('files.txt')
contents = f.read()
f.close 
print(contents)

# VS
cool_list = []
f = open('files.txt')
for line in f.readline(): 
	cool_list.append = line
print(cool_list[0])

```
## Access Mode 
------

| Mode | Mode Description | 
| ----- | ------------------ | 
| r         | read                        | 
| w        | write                       |                      
| a         | appending             | 



## Readline 
-----
```python
mylist = []
myfile = open("files.txt","r")
myline = myfile.readline()
while myline:
# Stripping whitespace 
# left and right strip whitepace
    # myline = myline.strip()
# left strip whitepace
    myline = myline.lstrip()
# right strip whitepace
    myline = myline.rstrip()
    mylist.append(myline)
    print(myline)
    myline=myfile.readline()
    
myfile.close
print(" ---------- ") 

print(mylist)
print("Split the list apart\n")
print(" ---------- ")
i = 0
for var in mylist:
    print('Index >> {} >> {}'.format(i, var))
    i = i + 1

print(" ---------- ")
```

## Handling Encoding
---
```python
mylist = []
filename = "jabberwocky.txt"

with open(filename,'r',encoding='UTF-8') as myfile:
# myline 
    while myline := myfile.readline():
# Remove whitespace from the right
        myline = myline.rstrip()
# Remove whitespace from the left
        myline = myline.lstrip()
# Remove whitespace from right and left
#       myline = myline.strip()
        mylist.append(myline)
        print(myline)
        myline=myfile.readline()
    
myfile.close
print(" ---------- ") 

print(mylist)
print("Split the list apart\n")
print(" ---------- ")
i = 0
for var in mylist:
    print('Index >> {} >> {}'.format(i, var))
    i = i + 1

print(" ---------- ") 

```
## Writing Files
```python
# Writes the lyrics of the Fast Food Song
# You may not be the same after this video:
# https://youtu.be/rOC9d17vASc?si=lZ01KjDu7YHvOw-E

def do_lyric(var):
    print("Writing a {} to the file...\n".format(var))
    return("{} \n".format(var))

f = open('write_filename.txt','a',encoding='UTF-8')
for i in range(2):
    f.write(do_lyric('The Pizza Hut'))
mystring = 'Kentucky Fried Chicken'
f.write(do_lyric(mystring))
mystring = 'The Pizza Hut'
f.write(do_lyric(mystring))
mystring = 'McDonald\'s'
f.write(do_lyric(mystring))
f.write("--------\n")
f.close()
```
### HTML Converter

```python
# Uses the userdata.txt file
# (filename,'r',encoding='UTF-8')
with open('userdata.txt', 'r') as fin:
    lines = fin.readlines()
    my_dictionary = {}
    for line in lines:
        key, value = line.split(':')

        key = key.replace('"','')
        value = value.replace('"','')

        key = key.strip()
        value = value.strip()

        my_dictionary[key] = value
fin.close()

#print the dictionary 
print('Show the dictionary')
print('-------------------------')
print(my_dictionary)
print('-------------------------')

# Write out the webpage
fout = open('coolwebpage.html','w',encoding='UTF-8')
fout.write('<html>')
fout.write('<head>')
fout.write('<title>Cool Web Page</title>')
fout.write('<style type="text/css">')
fout.write('th {font-weight:bold;font-family:helvetica;}')
fout.write('td {font-family:helvetica;}')
fout.write('</style>')
fout.write('</head>')
fout.write('<body>')
fout.write('<table cellpadding="10" cellspacing="10">')
fout.write('<thead>')
fout.write('<tr><th>User ID</th><th>Username</th></tr>')
fout.write('</thead>')

fout.write('<tbody>')
for k, v in my_dictionary.items():
    fout.write('<tr><td>{}</td><td>{}</td></tr>'.format(k,v))
fout.write('</tbody>')
fout.write('</table>')
fout.write('</body></html>')
fout.close()

```
