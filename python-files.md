## Opening and Reading 

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

```python
f = open('files.txt')
contents = f.read()
f.close 
print(contents)

# VS>
cool_list = []
f = open('files.txt')
for line in f.readline(): 
	cool_list.append = line
print(cool_list[0])

```
