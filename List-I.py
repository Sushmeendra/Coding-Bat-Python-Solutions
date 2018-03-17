def first_last6(nums):
  return(nums[0] == 6 or nums[-1] == 6)


def same_first_last(nums):
  return(len(nums) >= 1 and nums[0] == nums[-1])


def make_pi():
  return([3,1,4])


def common_end(a, b):
  return(a[0] == b[0] or a[-1] == b[-1])


def sum3(nums):
  return(sum(nums))


def rotate_left3(nums):
  nums.append(nums[0])
  nums.remove(nums[0])
  return(nums)


def reverse3(nums):
  nums.reverse()
  return(nums)


def max_end3(nums):
  if(nums[0] > nums[-1]):
    val = nums[0]
  else:
    val = nums[-1]
  nums = [val for i in range(len(nums))]
  return nums


def sum2(nums):
  return(sum(nums) if len(nums) <= 2 else sum(nums[:2]))


def middle_way(a, b):
  return(a[1:2]+b[1:2])


def make_ends(nums):
  return(nums[:1]+nums[-1:])


def has23(nums):
  return((2 in nums) or (3 in nums))
