#Compute Fibonacci numbers
#Iterative method

def Fib(n): #Failed
 m = 1 
 r = 1
 if (n == 1 or n == 2):
  return 1
 else:
  for i in range(n - 2):
   if (i//2 == 0):
    m = m + r
   else:
    r = r + m
 if (r > m):
  return r
 else:
  return m
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
#1, 2, 3, 4, 5, 6, 7,  8,  9,  10 ...
def Fib2(n):
 if (n == 1 or n == 2):
  return 1
 else:
  return (Fib2(n-1) + Fib2(n-2))

def Fib3(n):
 m = 1 
 r = 1
 s = 0
 if (n == 1 or n == 2):
  return 1
 for i in range(3,n+1):
  s = m + r
  r = m
  m = s
 return s

nm = 3
print("1st result:")
print(nm,"th Fibonacci number:", Fib3(nm))
print("2nd result:")
print(nm,"th Fibonacci number:", Fib2(nm))
