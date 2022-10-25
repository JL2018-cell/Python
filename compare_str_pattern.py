# You are allowed to create new strings, 
# but otherwise you are not allowed to construct 
# extra data structures to solve this problem (no list, set, dictionary, etc).

def detect_pattern(s1, s2): # this function takes two parameters as strings to compare.
  # Keep in mind that this method should return the same value 
  # no matter what order the two strings are passed
  
  # Insert your code here
  tmp = ""

  if len(s1) != len(s2):
    return False
  else:
    for i in range(len(s1)):
      if i == 0:
        tmp += s1[i]
        tmp += s2[i]
      else:
        if s1[i] in tmp:
          idx = tmp.find(s1[i])
          if tmp[idx+1] != s2[i]:
            return False
        else:
          tmp += s1[i]
          tmp += s2[i]
    return True


print(detect_pattern("xyzxyz", "toetoa"))
