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
        myline = myline.rstrip()
        myline = myline.lstrip()
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

