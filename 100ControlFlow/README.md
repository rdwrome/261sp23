# Control Flow
- In an interpreted language like Python: order in which statements (units of execution) are evaluated by the interpreter.
- When your program contains more than one statement, they're executed top to bottom (procedurally).

## Recursive Control Flow
- A function that calls itself is recursive; the process of executing it is called recursion.
- Factorials (8*7*6*5*4*3*2*1=40320) and the [Fibonacci sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html) are recursive:
  - Marked by self-similarity
  - Expresses a problem in terms of a smaller version of the same problem
- This *can sometimes* be the most efficient way to ask a computer to solve a problem
- Can also be a tricky way to get a computer to solve a problem
<pre>
### good recursion
def factorial(n):
  if n <= 1:
    return 1
  else:
    result = factorial(n-1)
    return n*result
///
factorial(ZZZ)
### can't stop won't stop - infinite recursion! stack overflow!
def func():
  print("Lovely!")
  func()
///
func()
///
### recursion with a stop or base case
def func(count):
  if count < 0:
    return
  print(f"{count} Lovely!")
  func(count - 1)
///
func(ZZZ)
</pre>

## Iterative Control Flow
- Not self-referential

### Conditional Execution
**If**
- Creates branches, new routes to proceed through.
- Uses boolean conditions to check if statements are true before proceeding.
<pre>
midiNote = 64
if midiNote < 0 or midiNote > 127:
  print("\nThe note value entered is an invalid MIDI note.\n")
if midiNote >= 0 and midiNote <= 127:
  print("The note value entered is a valid MIDI note.")
  print("MIDI note value is", midiNote)
</pre>

**Else**
<pre>
midiNote = 64
if midiNote <= 0 or midiNote >= 127:
  print("The note value entered is Invalid.")
else:
  print("The note value entered is valid.")
</pre>

**If/Elif/Else Conditions**
<pre>
midiNote = 64
if midiNote < 64:
  print("MIDI note is smaller than 64.")
elif midiNote > 64:
  print("MIDI note is greater than 64.")
else:
  print("MIDI note is equal to 64.")
</pre>

**Nested If/Else**
<pre>
midiNote = 64
if midiNote < 64:
    print("MIDI note is smaller than 64.")
    if midiNote == 48:
      print(f"The note name for {midiNote} is C2.")
    elif midiNote == 40:
      print(f"The note name for {midiNote} is E1.")
else:
    print("MIDI note is greater than or equal to 64.")
///
number = int(input("Enter a positive integer number: "))
if number > 0:
  if number % 2:
    print("The number is odd.")
  else:
    print("The number is even.")
else:
  print("The number you enter must be a positive integer number.")
</pre>
- With And/Or Statements
<pre>
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
if first == second and second == third:
  print("Three numbers are equal.")
elif first == second or second == third or third == first:
  print("Two numbers are equal.")
else:
  print("None are equal.")
</pre>

#### Group Exercise:
<pre>
- Create a file named `BOSseasons.py`.
- Write a program that prints out the seasons in Boston.
- Ask the user to input a number between 1 ~ 12.
- If the number is between 4 ~ 6, print out "Boston is in Spring".
- If the number is between 7 ~ 9, print out "Boston is in Summer".
- If the number is between 10 ~ 11, print out "Boston is in Autumn".
- If the number is between 12 ~ 3, print out "Boston is in Winter".
- If the number range is out of 1 ~ 12, print out "There are only 12 months in a year."
</pre>

### Loops
- Sends control flow back to some point in the program where it was before to repeat process with same environment.
- We need to keep track of how many times program goes back with an accumulator.
  - count
  - index range
- While loops: you don't know how many times you need to loop
- For loops: you do know how many times you need to loop
- Leave the loop when the condition is no longer satisfied

**While with count**
<pre>
count = 0
while (count < 3): 	
  count = count + 1
  print("Happy Thursday")
</pre>

**While/Else loop**
<pre>
count = 0
while (count < 3): 	
  count = count + 1
  print("Happy Monday")
else:
  print("Happy Tuesday")
</pre>

**For with index range**
<pre>
# Starts at 0 and goes up by one by default
for i in range(128):
  print(f"The next MIDI note value is {i}")
///
# Increment by 2 instead
for i in range(0, 128, 2):
  print(f"The next MIDI note value is {i}")
</pre>

**For with index range and nesting**
<pre>
for index in range(1500, 2701, 1):
  if index % 7 == 0 and index % 5 == 0:
    print(index)
///
for i in range(10):
  for j in range(10):
    if j >= i:
      print(j, end='')
  print()
///  
num = int(input("Enter a number: "))
if num > 0:
  for index in range(num):
    print('*', end='')
    if index % 5 == 4:
      print()
</pre>
