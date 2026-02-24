# my Solution
def isPalindrome( x:int) -> bool:
  xString = str(x)
  reverse = xString[::-1]
  if x == int(reverse):
    return True
  else:
    return False

# print(isPalindrome(121))

# Optimal Solution
def isPalindromeOptimal(x:int):
  if x < 0:
    return False
  
  rev = 0
  num = x

  while num != 0:
    rev = rev * 10 + num % 10
    num = num // 10

  return rev == x

print(isPalindromeOptimal(1211))
