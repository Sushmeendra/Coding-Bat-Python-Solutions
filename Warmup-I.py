def sleep_in(weekday, vacation):
  return(not(weekday) or vacation)

def monkey_trouble(a_smile, b_smile):
  return(a_smile and b_smile) or (not a_smile and not b_smile) 

def sum_double(a, b):
  return(2*(a+b) if a==b else a+b)

def diff21(n):
  return(2*abs(n-21) if n>21 else abs(n-21))

def parrot_trouble(talking, hour):
  return(talking and ((hour < 7) or (hour > 20)))

def makes10(a, b):
  return((a == 10 or b == 10) or (a+b == 10))

def near_hundred(n):
  return((abs(n-100) <= 10) or (abs(n-200) <= 10))  

def pos_neg(a, b, negative):
  return(a<0 and b<0 if(negative) else (a>0 and b<0)or(a<0 and b>0))

def not_string(str):
  return(str if(str[:3] == 'not') else 'not '+str)

def missing_char(str, n):
  l=list(str)
  l[n:n+1]=''
  return(''.join(l))
  
def front_back(str):
  return(str[-1]+str[1:-1]+str[0] if len(str) > 1 else str)

def front3(str):
  return(3*str[:3] if len(str) > 3 else 3*str)
