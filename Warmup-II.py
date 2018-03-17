def string_times(str, n):
  return(n*str)


def front_times(str, n):
  return(n*str[:3] if len(str) > 3 else n*str)


def string_bits(str):
  return(str[::2])


def string_splosion(str):
  if str == '' :
    return str
  return string_splosion(str[:-1]) + str


def last2(str):
  if(len(str) <= 2):
      return 0
  count = 0
  x=0
  y=2
  last = str[-2:]
  if(last in str):
    for i in range(len(str) - 2):
      if(str[x:y] == last):
        count += 1
      x += 1
      y += 1
  return count  	

#OR

'''
def last2(str):
	if(len(str) <= 2):
    	return 0
  	count = 0
  	x=0
  	y=2
  	last = str[-2:]
  	if(last in str):
    	for i in range(len(str) - 1):
      		if(str[x:y] == last):
        		count += 1
     	x += 1
     	y += 1
  	return (count -1)

#decrementing count by one because we dont want to 
#include the last two chars in the count
'''    

def array_count9(nums):
  count = 0
  for ele in nums:
    if(ele == 9):
      count += 1
  return count

def array_front9(nums):
  for ele in nums[:4]:
    if(ele == 9):
      return True
  return False

def array123(nums):
  x=0
  y=3
  for i in range(len(nums)-2):
    if(nums[x:y] == [1,2,3]):
      return True
    x += 1
    y += 1
  return False

def string_match(a, b):
  p=0
  q=2
  x=0
  y=2
  count = 0
  
  if(len(a) >len(b)):
    z=len(a)
  else:
    z=len(b)
    
  for i in range(z-1):
    if(a[p:q] == b[x:y]):
      count += 1
    p += 1
    q += 1
    x += 1
    y += 1
  return count