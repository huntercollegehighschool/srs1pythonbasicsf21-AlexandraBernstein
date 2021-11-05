"""
The function below is supposed to return True if the integer entered as the argument is prime, and False if it's not. Fix the code so that it runs the way it's supposed to.
"""

def isprime(num):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        return False
        break
    else:
      return True
  else:
    return False
  

def isprime(number):
  for i in range(2, number//2+1):
    if number % i == 0:
      return False
  return True

n = int(input("Number: "))

print(isprime(n))