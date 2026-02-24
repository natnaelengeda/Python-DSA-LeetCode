# My Solution
def Powx(x, n):
   value = 1
   for i in range(n):
      value = value * x
   return value
      

# print(Powx(2, 4))

# Optimal Solution
def PowxOptimal(x, n):
    if n == 0:
      return 1
   
    if n < 0:
      x = 1 / x
      n = -n

    result = 1

    while n > 0:
        if n % 2 == 1:
          result *= x
        x *= x
        n //=2

    return result

print(PowxOptimal(2,-2))