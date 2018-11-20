#!/bin/python3

n = int(input())

# Complete the factorial function below.
def factorial(n):
  if n == 1:
    return 1
  else:
    return factorial(n - 1)*n

if n < 0:
  print ("No factorial for negetive numbers!")
elif n == 0:
  print ("Factorial of 0 i 1")
else:
  print ("The factorial of", n, "is", factorial(n))
