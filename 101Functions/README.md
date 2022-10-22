# Functions

## Pyramids and FizzBuzz!

## Functions
- takes input value, does a process to it, returns an output value
- we've been using many that are already in python, now we'll write our own!

- Function Definition + Call
  - definition has to come before call, but call happens where call happens
<pre>
#function
def circle_area(x):
  return x * x * 3.14
#call
circle_area(3.0)
</pre>

- More fun functions
<pre>
#function
def minimum(x,y):
  if x < y:
    return x
  return y
#call
minmum (3, 4)
///
#function
def cube(n):
  return n * n * n
#call
cube(2)
///
#function
def sqr(x, n):
  return x ** n
#call
sqr(2, 3)
</pre>

- Passing parameters into function calls
<pre>
def sqr(x, n):
  return x ** n
base = 2
exponent = 3
print(f"{base} to the power of {exponent} is:", sqr(base, exponent))
///
def print_stars(n):
  while n > 0:
    print('*',end='')
    n -= 1
  print()
number = 3
print_stars(number)
///
def get_radius(circumference):
  return circumference / 3.14 / 2
number = 15
print(f"The radius of circle with circumference of {number} is {get_radius(number)}")
///
#function
def sumup(n):
  sum = 0
  for i in range(n + 1):
    sum += i
  return sum
#call
sumup(ZZZ)
</pre>

- Nesting Function Calls
<pre>
#function
def print_lyrics():
  print("I'm gonna take my horse to the old town road.")
  print("I'm gonna ride 'til I can't no more.")

def repeat_lyrics():
  print_lyrics()
  print_lyrics()
#call
repeat_lyrics()
///
#function
def sqr(n):
  return n * n

def pow4(n):
  return sqr(n) * sqr(n)
#call
pow4(ZZZ)
</pre>

- Multiple Inputs
<pre>
def add(a, b):
	return a + b

print("The result of addition is: ", add(2,3))
</pre>

- Multiple Outputs
<pre>
def getInstruments():
  return 'Drum', 'Guitar', 'Bass'

primary, secondary, tertiary = getInstruments()

print("My Instruments are: ", primary, secondary, tertiary)
</pre>

- Function Definition with accumulator
<pre>
#function
def func(count):
  for i in range(count + 1):
    print(f"{count - i} Lovely!")
#call
func(ZZZ)
</pre>

- Function with if/else
<pre>
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

n = ZZZ

print(f"Factorial of {n} is {factorial(n)}")
</pre>

## Variables

- Local Variables
 - Only hold meaning with single function calls
 - "the accidental of variables"
 -
 <pre>
 def print_favorite_instrument():
   instrument = input("What is your favorite instrument? ")
   print("Your favorite instrument is: ", instrument)

 def print_least_favorite_instrument():
   instrument = input("What is your least favorite instrument? ")
   print("Your least favorite instrument is: ", instrument)

 print_favorite_instrument()
 print_least_favorite_instrument()
 </pre>
- Global Variables
  - persist between function calls
  - can be called from within a function with the keyword `global`
  - mostly used for boolean statements
  - "the keysignature of variables"

## Functions in Processing

## The midterm is coming
