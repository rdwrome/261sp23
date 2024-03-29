# JavaScript

## Group Project Presentations

## Final Project Proposals

## JavaScript

**Why?**

- Makes websites dynamic
- Both compiled and OOP
- (has nothing to do with java)
- Browser console
- Helpful:
```javascript
	console.log()
	console.clear()
```

**Values and Operators**

- Numbers
	- 8 bytes of memory each, so can be +/- 9 Quadrillion
	- Decimals (not just integers)

- Simple Unary and Binary Operators

```javascript
	typeof
	- (unary and binary)
	+
	/
	*
	++ (shorthand counter up)
	-- (shorthand counter down)
	%
```
- Strings
	- “Bound by Quotations”
	- Can’t be divided, multiplied, subtracted
	- String literal

	```javascript
	`${9/3} little pigs`
	```
- Comparison Operators

```javascript
	> greater than
	< less than
	>= greater than or equal to
	<= less than or equal to
	== equal to
	!= not equal to
```
- Logical Operators

```javascript
	&& and/both
	|| or/either
	! not (like logical negative sign)
```
- Conditional/Ternary Operator
	 - condition ? expression1 : expression2

		```javascript
		let height = prompt('what is your height in inches?');
		let pass = (height > 48) ? "Yes, you may ride the rollercoaster." : "Sorry, you may not ride the rollercoaster.";
		console.log(pass);
		```
- NaN and Empty Values
	- NaN = not a number but *should* have been a number
	- null, undefined = can't compute

**Some Syntax**

- Automatic Type Conversion
- indentation and semi-colons
- Capitalization
- Commenting

**Expressions and Statements**
- Expression: a piece of code that produces a value
- Statement: expressions nested together to form a whole
- Block: thread of statements

**Bindings**

- Environment
- let (can be rebound anytime) vs const (can't be rebound within a block) vs var (works, is just old-school)
- Naming Bindings and Keywords
- scopes (use scope example)
	- local: created and can only be referenced within a function (accidental)
	- global: defined outside of block and can be referenced anywhere (key signature)
	- scoping scope: can look out into environment
- nested scopes (use nested example)

**Control Flow**

- Conditional Execution
	- if/else (chain of fools)
	- switch (switch example)

- Loops
	- while (while example)
	- do (do example) [don't enter anything!]
	- for (for example)
	- break (breaking out example)

**Functions**
- a function is a whole program wrapped up into a Value (quack example)
- Arguments come in
- Return Values come out
- don't confuse functions with side effects!
- examples:

```javascript
	Math.min(10,3)
	Math.max(10,3)
```

**Recursion**
- (use recursive chicken example)

**Debugging in JS**

- "use strict" (use strict example)
- global scope?
- local scope?
- no undeclared bindings
- no escape characters
- [unit testing: a program that verifies part of your code](https://www.smashingmagazine.com/2012/06/introduction-to-javascript-unit-testing/)
