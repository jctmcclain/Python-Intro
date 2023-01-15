# Introduction to Python Scripts

### What's your name
--------------------------------------------
```python
name = raw_input("What is your name?\n")
print("Hi there, " + name)
```

### Average Calculator
--------------------------------------------
```python
print "Welcome to the TIU Average Calculator.. \n"
one = raw_input("Please enter your first reading .. \n")
two = raw_input("Please enter your second reading .. \n")
three = raw_input("Please enter your third reading .. \n")
av = (int(one) + int(two) + int(three))/3
print " ---------------------------- "
print "Your average is .. " + str(av)
print "\n Have a Ducky Day .. \n"
print " ---------------------------- "
```


### Turtles
--------------------------------------------
#### Hexagon
```python
import turtle
t = turtle.Pen()
for x in range(1,8):
	t.forward(100)
	t.rt(60)
	t.forward(100)
t.reset()
```	
#### Hexagon Simplified 
```python
----------------------
import turtle
t = turtle.Pen()
for x in range(6):
	t.circle(100)
	t.left(60) 
```
	
--------------------------------------------
Something Cool
import turtle
t = turtle.Pen()
c = ["red","yellow","blue", "green"]
for x in range(100):
	t.pencolor(c[x%4])
	t.forward(x)
	t.left(91)
	
Something Cooler
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
c = ["red","yellow","blue", "green"]
for x in range(100):
	t.pencolor(c[x%4])
	t.forward(x)
	t.left(91)
	

	
