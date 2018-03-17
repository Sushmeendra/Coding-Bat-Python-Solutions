def cigar_party(cigars, is_weekend):
  return((cigars in range(40,61) and not(is_weekend)) or (cigars >= 40 and is_weekend))


def date_fashion(you, date):
  if(you <= 2 or date <= 2):
    return 0
  elif(you >= 8 or date >= 8):
    return 2
  return 1


def squirrel_play(temp, is_summer):
  if(is_summer):
    return (temp in range(60,101))
  return (temp in range(60,91))


def caught_speeding(speed, is_birthday):
  if(is_birthday):
    if(speed <= 65):
      return 0
    if(speed in range(66,86)):
      return 1
    return 2
  else:  
    if(speed <= 60):
      return 0
    if(speed in range(61,81)):
      return 1
    return 2


def sorta_sum(a, b):
  return(a+b if a+b not in range(10,20) else 20)


def alarm_clock(day, vacation):
  if(vacation):
    return('10:00' if day in range(1,6) else 'off')
  return('7:00' if day in range(1,6) else '10:00')


def love6(a, b):
  return(a==6 or b==6 or abs(a-b) ==6 or a+b == 6)


def in1to10(n, outside_mode):
  if(outside_mode):
    return(n <= 1 or n >= 10)
  return(n in range(1,11))


def near_ten(num):
  return(num % 10 in (0,1,2,8,9))
 