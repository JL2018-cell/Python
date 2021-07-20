#Find maximum number in an array using recursion.
def max(ls):
 if (len(ls) == 1):
  return ls[0]
 else:
  temp = max(ls[0:len(ls)-1])
  if (ls[len(ls)-1] > temp):
   return ls[len(ls)-1]
  else:
   return temp


def max2(ls):
 if (len(ls) == 1):
  return ls[0]
 elif (len(ls) == 2):
  if (ls[0] > ls[1]):
   return ls[0]
  else:
   return ls[1]
 else:
  tmp1 = max2(ls[0:(len(ls)//2)])
  tmp2 = max2(ls[(len(ls)//2):len(ls)])
  if (tmp1 > tmp2):
   return tmp1
  else:
   return tmp2



opp = [19,2,9,4,50,6,7,8,9]
print("Result 1:",max(opp))
print("Result 2:",max2(opp))




