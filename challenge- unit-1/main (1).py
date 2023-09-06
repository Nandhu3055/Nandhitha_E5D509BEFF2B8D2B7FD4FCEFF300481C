def factorial(factno):
  if factno==0:
    return 1
  elif factno==1:
    return 1
  else:
    return factno*factorial(factno-1)
num = int(input("Enter any number to find its factorial = "))
print("Factorial of ",num," = ",factorial(num))