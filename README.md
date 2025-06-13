# Bookbot 📘 

Bookbot is my first [Boot.dev](https://www.boot.dev) project! 
It is a Python program that analyzes novels in `.txt` format and prints a statistical report featuring:
- Word count
- A list of characters and their count

## Installation

1. Either clone this repository or download it as ZIP and unzip
2. Within the project directory (`bookbot`), create a directory called `books` and add the book(s) you would like to analyze  

## Usage 

To use Bookbot, you must provide a path to your book file when executing `main.py`:

```bash
$ python3 main.py <path_to_book>
```

## Example 

```bash
$ python3 main.py books/mobydick.txt
============ BOOKBOT ============
Analyzing book found at books/mobydick.txt...
----------- Word Count ----------
Found 215838 total words
--------- Character Count -------
e: 119351
t: 89874
a: 79226
o: 70809
n: 66782
i: 66675
s: 65138
h: 63769
r: 53593
l: 43351
d: 38840
u: 27205
m: 23626
c: 23319
w: 22557
g: 21287
f: 21252
p: 17873
y: 17244
b: 17203
v: 8725
k: 8228
q: 1581
j: 1178
x: 1064
z: 636
æ: 23
œ: 5
é: 5
è: 3
ח: 1
ו: 1
ϰ: 1
η: 1
τ: 1
ο: 1
ς: 1
â: 1
============== END ==============
```