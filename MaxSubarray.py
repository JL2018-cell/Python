#MaxSubarray

def MaxSubArray(ls):
 max = 0
 for i in range(len(ls)):
  sum = 0
  for j in range(i, len(ls)):
   sum = sum + ls[j]
  if (sum > max):
   max = sum
 return max



ls = [-4, 6, -3, -1, 6, 1, -2]
print(MaxSubArray(ls))
