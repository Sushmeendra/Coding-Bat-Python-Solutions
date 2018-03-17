def make_bricks(small, big, goal):
  
  #max_possible is the max val you 
  #can make using given bricks
  max_possible = small + big*5
  if(max_possible < goal):
    return False
  
  #min_smalls is the minimum no of 'small'
  #bricks needed to arrive at 'goal'
  min_smalls = goal % 5
  if(small < min_smalls):
    return False
  
  return True


def lone_sum(a, b, c):
  l=[a,b,c]
  Sum = 0
  
  for ele in l:
    if(l.count(ele) > 1):
      pass
    else:
      Sum += ele
  return Sum    


def lucky_sum(a, b, c):
  l=[a,b,c]
  Sum = 0
  
  for ele in l:
    if(ele == 13):
      return Sum
    else:
      Sum += ele
  return Sum    


def no_teen_sum(a, b, c):
  l = [a,b,c]
  Sum = 0
  for ele in l:
    if(fix_teen(ele)):
      Sum += ele
  return Sum 
#return False if no doesent contribute to Sum else True
def fix_teen(n):
  if(n in range(13,20) and n not in (15,16)):
    return False
  return True



def round_sum(a, b, c):
  l=[a,b,c]
  roundSum = 0
  
  for ele in l:
    roundSum += round10(ele) 
  return roundSum
#returns no. rounded to nearest 10
def round10 (num):
  if(num % 10 >= 5):
    temp = num % 10
    if(temp > 5):
      temp = 10 - temp
    num += temp
    return num 
  else:
    return(num - num%10)
  

def close_far(a, b, c):
  l = [a,b,c]
  
  if(abs(a-b) in range(0,2) and abs(c-a) >=2 and abs(c-b) >=2):
    return True
  elif(abs(a-c) in range(0,2) and abs(b-a) >=2 and abs(b-c) >=2):
    return True
  return False


def make_chocolate(small, big, goal):
  
  max_possible = small + big*5
  if(max_possible < goal):
    return -1
  
  req_small = 0
  if(goal >= big*5):
    req_small = goal - big*5
    return req_small
  
  if(goal < big*5):
    while(1):
      if(goal - 5 < 0):
        if(goal > small):
          return -1
        else:
          return goal
      goal = goal - 5
    return -1    
    
 
    