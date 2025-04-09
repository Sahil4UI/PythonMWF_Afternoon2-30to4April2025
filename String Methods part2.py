Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "python is a high level programming"
>>> x.split()
['python', 'is', 'a', 'high', 'level', 'programming']
>>> x.split()[-1]
'programming'
>>> x
'python is a high level programming'
>>> x.split("h")
['pyt', 'on is a ', 'ig', ' level programming']
>>> x = ["how","are","you"]
>>> " ".join(x)
'how are you'
>>> "#".join(x)
'how#are#you'
>>> x  = "python"
>>> len(x)
6
>>> x.center(7)
' python'
x.center(20)
'       python       '
x.center(21,"*")
'********python*******'
x
'python'
x.zfill(10)
'0000python'
x = "A"
ord(x)#ascii value
65
chr(65)
'A'
x = '''hello
lets learn python
welcome to class
welcome to arth institute'''
x.splitlines()
['hello', 'lets learn python', 'welcome to class', 'welcome to arth institute']
x.splitlines()[0]
'hello'
