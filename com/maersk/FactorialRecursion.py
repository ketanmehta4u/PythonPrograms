# Write a Python Function to find factorial of given number using tail recursion.

def factorial(n, a = 1):
 
    if (n == 0):
        return a
 
    return fact(n - 1, n * a)
 
# Driver program to test
#  above function
print("factorial of 5 is: ", factorial(5))
