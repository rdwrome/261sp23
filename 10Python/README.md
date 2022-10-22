# Python

## Made from Scratch!

## Compiled vs Interpreted Computer Languages
- Compiled: human readable > machine readable
- Interpreted: human readable > interpreter > machine readable

## Compiled languages: Source, Object, Compiler, Executable
- Source: what we write (human readable)
- Compiler: translates from source to object
- Object: binary (machine readable)
- Executable: actually runs program

## Compiled languages
- Fortran
- C
- C++
- Rust

## Interpreted languages
- Python
- Ruby
- JavaScript

## CLI vs IDE

**Command Line Interfaces (CLI)**
- Most commonly used for compiled languages
- "under the hood"

***Most common commands***

	- `say` Do as I say

	- `pwd` Print Working Directory (prints the path to the directory [folder] that you are currently in). Map+Compass.

	- `cd` Change Directory (changes working directory to different directory)
		>You can type `cd` and then drag and drop the folder you'd like to work in, into the Terminal Window. This is much faster than typing out the full path.

	- `ls` Lists the files stored in the Working Directory

	- `clear` clears the Terminal Window

	- `say -v ?` for fun

	- `-o` tag to create an object file

***More advanced commands***

	- `cp` Makes a copy of a file ("cp file.txt filecopy.txt" makes a copy of file.txt and names it filecopy.txt)

	- `mkdir` Makes a new directory (`mkdir NewDirectory` makes a new folder called `NewDirectory`)

	- `&&` Means "and also do this", helpful for inputing multiple commands in the same line

	- `man` opens the manual for Terminal commands ("man man" will open up the manual for the manual!)

	- `~` means home directory

	- `nano` is a text editor within Command-line Interface (isn't Atom great!)

**Additional resources for Terminal and CLI**
- [GNU Bash reference](http://www.gnu.org/software/bash/manual/bashref.html)
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
- [101 Bash Commands and Tips for Beginners to Experts](https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je)

**Integrated Development Environments (IDE)**
- Most commonly used for interpreted languages

## Intro to Python
- High-level
- General but!
	- [Modules and libraries can make it more specific](https://wiki.python.org/moin/UsefulModules)
		- Modules: simple .py file that abstracts out specific information (functions, variables, other things)
		- libraries (or packages) are a collection of modules
- Interpreted (executed by the interpreter vs. compiled)
  - Easier to debug
  - Runs a little slower
- Object-oriented (much more on this later!)
- Scripts are a sequence of definitions and commands executed in the shell
<pre> >>> </pre>
- #nocommentcomment

**[Do You Have Python3?](https://www.python.org/downloads/)**
- More functional standard libraries than 2
- Some things only supported on 2, though
  - python --version
  - python3 --version
- IF YOU'VE DOWNLOADED PYTHON3 TODAY: open "update shell profile command" in the python3 folder
- Check your pip!
	- pip --version
	- pip3 --version

**Running Python**
  - CLI
    - python3 hands.py
  - IDE
		- Run&Debug vs. Run and Debug in VSC

## Debugging in general
- Frustrating
- Most of what programming is
- ALWAYS BE DOCUMENTING (ABD!)
- Think of it as detective work
	- You're given evidence  and have to infer what happened
- Or think of it as a science experiment
	- Analyze the error message + code together
	- Draft a theory as to why you got the bug (with notes!)
		- record of what you've tried to fix it
	- Make a test of your theory
	- Monitor your code with printing functions and breakpoints

## Bugs in the Wild

**Syntax**

- Your code broke a structure/expectation rule
- Classic problems:
	- keyword is a variable name
	- colon after for, while, if, and def statements
	- matching quotation marks in Strings
	- matching brackets
	- = instead of ==
	- indentation
	- ASCII issues

**Runtime**

- Something broke while it was running/just didn't run at all
- Classic problems:
	- Control Flow issues
	- Recursion

**Semantic**

- Something is not right and your computer doesn't know it but you do
- Hardest to figure out!
- Go back to Pseudocoding
- Break everything down into the smallest unit you can