def double_char(str):
  s=""
  for i in range(len(str)):
    s += (2)*str[i]
  return s


def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if(str[i] == 'h' and str[i+1] == 'i'):
      count += 1
  return count 


def cat_dog(str):
  num_cat = 0
  num_dog = 0
  
  for i in range(len(str) - 2):
    if(str[i:i+3] == 'cat'):
      num_cat += 1
    elif(str[i:i+3] == 'dog'):
      num_dog += 1
  if(num_cat == num_dog):
    return True
  return False 


def count_code(str):
  count = 0
  for i in range(len(str) -3):
    if(str[i:i+2] == 'co' and str[i+3:i+4] == 'e'):
      count += 1
  return count


def end_other(a, b):
  
  for i in range(len(a) - (len(b)-1)):
    if(a[-len(b):].lower() == b.lower()):
      return True
  for i in range(len(b) - (len(a)-1)):
    if(b[-len(a):].lower() == a.lower()):
      return True
  return False


def xyz_there(str):
  if('xyz' not in str):
    return False
  
  for i in range(len(str) - 2):
    if(str[i:i+3] == 'xyz' and str[i-1] != '.'):
      return True
  return False
