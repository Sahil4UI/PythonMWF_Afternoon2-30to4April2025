Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 9
y = 8
x+y
17
x-y
1
x*y
72
x/y
1.125
x//y#quotient comes in integer form
1
3**3
27
24%7#modulus - remainder
3
2**0.5
1.4142135623730951

#library
import math
math.pow(2,4)
16.0
math.sqrt(81)
9.0
math.cbrt(27)
3.0
math.factorial(5)
120
5*4*3*2*1
120
math.lcm(2,3,4)
12
math.gcd(81,72,900)
9
math.floor(3.14)
3
math.ceil(3.14)
4

======================== RESTART: Shell ========================
math.fabs()#mod
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    math.fabs()#mod
NameError: name 'math' is not defined. Did you forget to import 'math'?
>>> import math
>>> math.fabs(-90)
90.0
>>> math.perm(3,2)
6
>>> math.comb(3,2)
3
>>> math.pi
3.141592653589793
\
>>> math.e
2.718281828459045
>>> math.tau
6.283185307179586
>>> 
>>> help(math)

