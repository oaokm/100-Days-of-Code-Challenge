# Password Generator

## About 
This program is a Generator for password, and the generator has three levels:
* Level One: Easy, `example`: hn9zotg0
* Level two: Medium, `example`: bx8iodAl
* Level Three: Hard, `example`: &BUeo5Y#

The generator generates numbers from 8 to infinity.

## How to used?
You can use in two ways:

### **The First Method: Command Line**
The Command Line alos has two method:

#### One: A Quick:
How to type fast on the command line:
```sh
$ python3 main.py [level(f:E+f:M+f:H)] [length of password]
```

* Level One: Easy
```sh
$ python3 main.py f 8

<OUTPUT>
	[PASSWORD GENERATOR]
('e4mgq59w', 8)
```
* Level Two: Medium
```sh
 python3 main.py ff 8

<OUTPUT>
	[PASSWORD GENERATOR]
('6N41arVX', 8)
```
* Level Three: Hard
```sh
 python3 main.py fff 8

<OUTPUT>
	[PASSWORD GENERATOR]
('A*QQiLA@', 8)
```
 > Note1: Of course, you can write the level without typing the length of the password, automatically the program will put the length of 8.
 > Note2: You can write length of the password to infinity.
 ```sh
 python3 main.py fff 

<OUTPUT>
	[PASSWORD GENERATOR]
('9#p/v83E', 8)
```
 ```sh
 python3 main.py fff 50

<OUTPUT>
	[PASSWORD GENERATOR]
('HiXDwLMl*FGx4Pe*d!Eg+WtV!C.hseB)fBR.1^Vf&P^pk9YY9C', 50)
```

#### Two: **Run the program:**
The method of entering the required information is not the same.

```sh
$ python3 main.py 
	[PASSWORD GENERATOR]
Enter the level the password and the length, like -> (level(f:E,f:M,f:H) long_password) 
 > [Enter Here!]
```
For example:
```sh
$ python3 main.py 
	[PASSWORD GENERATOR]
Enter the level the password and the length, like -> (level(f:E,f:M,f:H) long_password) 
 > ff  100
 ('qQUBZ7T4xSBaS0ROOtpdUs9DddzToMjm6LSuk9ZwK1BDpMOmllpyQ7GG8X52XKcIB3yysoeNEfP72xZAb5UjjJlQHiW61fEGjEIr', 100)
```

*End*
