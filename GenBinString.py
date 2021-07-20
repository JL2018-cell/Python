#Generate all n-bit strings, each entry = 0 or 1.
#ls = [], n = length of string.
def genBin(n,ls):
 if (n == 1):
  for i in range(2):
   ls.append([i])
  return ls
 else:
  ls = genBin(n - 1,ls)
  ls2 = list()
  for j in range(len(ls)):
   ls2.append(ls[j] + [0])
   ls2.append(ls[j] + [1])
  return ls2

#Set up and Write result to output.txt if output.txt does not exist.
#Input is a list of numbers.
def writeFile(subResultList):
 fin = open("output.txt","w")
 for i in range(len(subResultList)- 1):
  fin.write(str(subResultList[i]) + ", ")
 fin.write(str(subResultList[len(subResultList) - 1]))
 fin.close()

def writeFail():
 fin = open("output.txt","w")
 fin.write("No such a subset!")
 fin.close()

#Display a list and length of the list
def showList(ls):
 for i in range(len(ls)):
  print("Length of list =",len(ls))

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


fin = open('input.txt')
readList = list()
resultList = list()
for i in fin: #i is a line in the file.
  readList.append(int(i))
fin.close()

n = readList[0] #length of array
x = readList[1] #aimed size of array
S = readList[2] #aimed sum

numList = readList[3:len(readList)]

prstAbsList = genBin(n, [])

allSubsetList = subList(numList, prstAbsList)

for i in range(len(allSubsetList)):
 if (sum(allSubsetList[i]) == S and len(allSubsetList[i]) <= x):
  resultList.append(allSubsetList[i])


if (len(resultList)):
 writeFile(resultList[0])
else:
 writeFail()

'''
Found:
1, 2, 3
Not found:
output "No such a subset!"
'''

