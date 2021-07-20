def Hanoi(start,intm,end,num_dsk):
 if (num_dsk == 1):
  print("Move disk ", num_dsk, " from ",start, " to ",end)
 else:
  Hanoi(start,end,intm,num_dsk - 1)
  print("Move disk ", num_dsk, " from ", start, " to ", end)
  #Hanoi(start,intm,end,num_dsk - 1)
  Hanoi(intm,start,end,num_dsk - 1)


print("Hello!")
a = 1
b = 2
c = 3
d = 4
Hanoi(a, b, c, d)
