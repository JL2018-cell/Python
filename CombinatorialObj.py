#Generate all n-bit strings, each entry = 0 or 1.
def f(n,ls):
 if (n == 1):
  for i in range(2):
   ls.append([i])
  return ls
 else:
  ls = f(n - 1,ls)
  ls2 = list()
  for j in range(len(ls)):
   ls2.append(ls[j] + [0])
   ls2.append(ls[j] + [1])
  return ls2

#Generate all subsets given a list
def subList(ls, chkLs):
 result = list()
 tmp = list()
 for i in range(len(chkLs)):
  for j in range(len(chkLs[i])):
   if (chkLs[i][j]): #Correct indexing of list
    tmp.append(ls[j])
  result.append(tmp)
  tmp = []
 return result

#Generate all its subsets with size <= x
def pickList(ls,n):
 result = list()
 for i in range(len(ls)):
  if (len(ls[i]) <= n):
   result.append(ls[i])
 return result

#Display a list and length of the list
def showList(ls):
 for i in range(len(ls)):
  print(ls[i])
 print("Length of list =",len(ls))

ls = f(4,[])
showList(ls)

givenLs = [1,2,3,4,5,6]
resultLs = subList(givenLs, f(len(givenLs),[])) #f(.) requires 2 arguments, not 1.
showList(resultLs)
#Length of list = Number of ways to choose any elements from the list = 2^(len(ls))

filteredList = pickList(resultLs, 3)
showList(filteredList)

#Example: choose subsets with <- 3 elements from a list of length = 6.
#Then, Number of ways = 6C0 + 6C1 + 6C2 + 6C3






