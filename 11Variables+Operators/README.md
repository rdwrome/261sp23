

## Previously on LMSC-261
**Python**
- High-level
- General but!
	- [Modules and libraries can make it more specific](https://wiki.python.org/moin/UsefulModules)
		- Modules: simple .py file that abstracts out specific information (functions, variables, other things)
		- libraries (or packages) are a collection of modules
- Interpreted
  - Easier to debug
  - Runs a little slower
- Object-oriented
- Scripts are a sequence of definitions and commands executed in the shell
<pre> >>> </pre>
- #nocommentcomment

**Objects**
- Made up up values (result of calculation) and variables
- What Python manipulates

**Variables**
- Binds names to objects
- Variables are really easy to assign and reassign
- We can parameter pass
- CODE ALONG
	<pre>
	one = 1
	two = 2
	three = one + two
	print(three)
	</pre>

**Operators**
- Simple
<pre>
+
-
*
/
%
// - floor division (ignores the remainder) i.e 6//4 is 1 because 4 only goes into 6 once.
** - raised to the power of</pre>
- PEMDAS (parentheses, exponents, multiplication, division, addition, subtraction) applies!

- Boolean/Comparison
	- Checks for truth!
![Boolean Diagram](bool.png)

**Expressions**
- Made up of objects+operators

**Keywords**
- Only variable naming rules
<pre>
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
</pre>

## Python + Memory Address

**Strings**
	<pre>
	#len function
	len('rachel devorah wood rome')
	///
	#indexing
	myName = 'rachel'
	///
	myName[3]
	///
	#slicing
	myName[0:3]
	///
	myName[2:4]
	///
	myName[0:]
	#concatenation
	'yum'+'my'
	'yum' * 3
	</pre>

## Input and Output
- type
<pre>
type(10)
type(10.5)
type("Hello, World!")
type(True)
</pre>
- Get String
<pre>
str = input("Name: ")
print("Hello,", str)
</pre>
- Printing paramenters and f-String
<pre>
#str = input("Name: ")
print("Hello,", str, sep='')
///
#str = input("Name: ")
print(f"Hello, {str}")
</pre>
- Printing floating points
	- what is π?
<pre>
z = 3.14159265358979323846264338327950288419716939937510
///
print(f"{z}")
print(f"{z:.50f}")
</pre>
- f-String math
	- int
<pre>
bags = 3
bananas = 12
print(f"{bananas} bananas were split into {int(bananas / bags)}groups to fit into {bags} bags.")
</pre>
	- float (with parameter passing)
<pre>
f = 99
c = (f - 32) * 5 / 9
print(f, f"Fahrenheit is: {c:.2f} Celsius")
</pre>
- Special characters
- tab and new line
<pre>
print("col1\tcol2\tcol3\ncol1\tcol2\tcol3\ncol1\tcol2\tcol3")
</pre>

## Object-oriented programming
- Some languages can do it, some languages must do it, e.g. javaScript *can* do it, Python *must* do it
- Principles of OOP
    - Encapsulation
  		- object: independent part of the program that manages itself (own rules and ways of doing things)
      - objects are made up of values + variables
      - objects are what Python manipulates
      - objects are reusable
      - a specific realization of an object is a
  	- Inheritance
      - objects get their functions from classes
      - class: template, blueprint for creating objects
  		- superclass is parent, class is child
  		- class inherits attributes of parent (through abstraction) but modifies, evolves
      - classes are reusable
  	- Polymorphism
  		- change the way something works by overriding and overloading
      - change type, have multiple types work together
  		- overriding: walk to moon walk
  		- overloading: walk to run

## Abstraction Redux
	- Abstraction: to deal with complex systems, we can ignore inessential details of other parts of the program as long as we understand what they do
	- In Python, modules and packages make the general language more specific with this use of abstraction

## Python Modules and Packages
	- Modules: simple .py file that abstracts out specific information (functions, variables, other things)
	- Packages (or libraries) are a collection of modules
	 - out-of-date dependencies can be the root of all your evils

## [ThinkDSP](https://greenteapress.com/thinkdsp/html/index.html)
- [First Tutorial in Colab](https://colab.research.google.com/github/AllenDowney/ThinkDSP/blob/master/code/chap01.ipynb)

## [Other Python Packages](https://pypi.org/)

## Ways Rachel is using Python Modules for Music
  - [Troop](https://github.com/Qirky/Troop)
  - [Magenta](https://github.com/magenta/magenta/tree/main/magenta/models)
    - [Coconet](https://github.com/magenta/magenta/tree/main/magenta/models/coconet)s