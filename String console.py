Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "hello world"
>>> type(x)
<class 'str'>
>>> x = 'hello world'
>>> type(x)
<class 'str'>
>>> x = "hello "python""
SyntaxError: invalid syntax
>>> x = 'hello "python"'
>>> print(x)
hello "python"
>>> x = "hello 'python'"
... 
>>> print(x)
hello 'python'
>>> x = "'hello' python"
print(x)
'hello' python
x = "hello \"Python\""
print(x)
hello "Python"
#\ - escape sequence
x = "hello
SyntaxError: unterminated string literal (detected at line 1)
#'' and "" are used to store a character/word/line
x = '''hello
welcome to python
lets learn python'''
print(x)
hello
welcome to python
lets learn python
#'''  - multi line string
#indexing
x = "Python"
x[0]
'P'
x[1]
'y'
x[100000000]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x[100000000]
IndexError: string index out of range
x
'Python'
x1 = "Python1"
#Slicing
x = "hello Python"
x[0:5]
'hello'
x[0:5:1]
'hello'
x[0:5:2]
'hlo'
x[5:]
' Python'
x[:5]
'hello'
x[:]
'hello Python'
x[::-1]
'nohtyP olleh'
#String Methods
x = "pYtHoN"
X
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    X
NameError: name 'X' is not defined. Did you mean: 'x'?
x
'pYtHoN'
len(x)
6
x.upper()
'PYTHON'
x.lower()
'python'
x.swapcase()
'PyThOn'
x
'pYtHoN'
x = "hello welcome to arth Institute"
x.capitalize()
'Hello welcome to arth institute'
x.title()
'Hello Welcome To Arth Institute'
x.find("e")
1
x.rfind("e")
30
x.find("e",2)
7
x.index("e",2)
7
x.find("Arth")
-1
x
'hello welcome to arth Institute'
x.find("arth")
17
x.find("X")
-1
#-1 means not found
x.index("X")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x.index("X")
ValueError: substring not found
