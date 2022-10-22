## Assignment - Pyramid

## Program
- Create a file named `{yourlastname}pyramid.py`.
- Write a program that prints out a pyramid that looks like this:

		       #
		      ##
		     ###
		    ####
		   #####
		  ######
		 #######
		########

- Each hash (`#`) is a bit taller than it is wide, so the pyramid itself is also be taller than it is wide.
- Have a variable named `stacks` that decides how tall the pyramid should be for a positive integer between 1 and 8.
- Ask the user how tall (1 ~ 8) the pyramid should be.
- If the number is out of range, make sure to let the user know and exit the program.
- Here's how the program might work when the `stack` variable is `8`:

		       #
		      ##
		     ###
		    ####
		   #####
		  ######
		 #######
		########

- Here's how the program might work when the `stack` variable is `4`:

		   #
		  ##
		 ###
		####

- Here's how the program might work when the `stack` variable is `2`:

		 #
		##

- Here's how the program might work when the `stack` variable is `1`:

		#

- Just as Scratch has a `Repeat` block, so does Python have a `for` loop, via which you can iterate some number of times. Perhaps on each iteration, `i`, you could print that many hashes?
- You can actually *nest* loops, iterating with one variable (e.g., `i`) in the *outer* loop and another (e.g., `j`) in the *inner* loop. For instance, here's how you might print a square of height and width `n`, below. Of course, it's not a square that you want to print :)

```python
for i in range(num):
  for j in range(num):
    print('#', end='')
  print()
```

## MarkDown file
- Explain your choices and the problems you faced
