def sol(disc,frm,to,temp):
  if disc == 1:
    print("Move",disc,"frm",from,"to",to,sep=' ')
  if disc != 1:
    sol(disc-1,frm,temp,to) #Shift intermediate Tower frm a stick to another stick
    print("Move",disc,"frm",frm,"to",to,sep=' ')
    sol(disc-1,temp,to,frm) #Shift intermediate Tower frm a stick to another stick

disc = int(input("How many discs?"))
frm = 1
to = 3
temp = 2
sol(disc,frm,to,temp)