def gcd(a, b) :
  num = min(a,b)
  while num > 0:
    if (a % num == 0) and (b % num == 0):
      return num
    num -= 1
  return -1




print(gcd(48,18))