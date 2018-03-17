def count_evens(nums):
  count = 0
  for ele in nums:
    if(ele % 2 == 0):
      count += 1
  return count


def big_diff(nums):
  return(max(nums) -min(nums))


def centered_average(nums):
  
  nums.remove(min(nums))
  nums.remove(max(nums))
  flag = 1
    
  c_avg =0
  for ele in nums:
        c_avg += ele
      
  return(c_avg / len(nums))



def sum13(nums):
  Sum = 0
  seen_thirteen = 0
  for i in range(len(nums)):
    if(seen_thirteen == 1):
      seen_thirteen = 0
      pass
    elif(nums[i] == 13):
      seen_thirteen = 1
    elif(seen_thirteen == 0):
      Sum += nums[i]

  return Sum



def sum67(nums):
  set_intvl = 0
  Sum = 0
  
  for i in range(len(nums)):
    if(nums[i] == 6):
      set_intvl = 1
    elif(set_intvl == 1 and nums[i] != 7):
      pass
    elif(set_intvl == 1 and nums[i] == 7):
      set_intvl = 0
    elif(set_intvl == 0):
      Sum += nums[i]
  return Sum



def has22(nums):
  
  seen_2 = 0

  for ele in nums:
  	#found
  	if(seen_2 == 1 and ele == 2):
  		return True

  	elif(ele == 2):
  		seen_2 = 1
  	else:
  		seen_2 = 0
  return False

