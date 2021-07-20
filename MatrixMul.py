def Mult(ls1, ls2):
 #print("len ls1:",len(ls1))
 #print("len ls2:",len(ls2))
 ls3 = list()
 ls3.append((ls1[0]*ls2[0]) + (ls1[1]*ls2[2]))
 ls3.append((ls1[0]*ls2[1]) + (ls1[1]*ls2[3]))
 ls3.append((ls1[2]*ls2[0]) + (ls1[3]*ls2[2]))
 ls3.append((ls1[2]*ls2[1]) + (ls1[3]*ls2[3]))
 return ls3

def Power(ls, n):
 #print("Length:",len(ls))
 if (n < 2):
  return ls
 else:
  return Mult(ls, Power(ls, n - 1))
 

def Power2(ls,n):
 if (n < 2):
  return ls
 else:
  ls2 = Power(ls, n//2)
  if (n%2 == 0):
   return Mult(ls2, ls2)
  else:
   return Mult(Mult(ls2, ls2), ls)

A = [1, 1, 1, 0]
n = 9
ls = list()
ls= Power2(A,n)
print(ls[0],ls[1])
print(ls[2],ls[3])


