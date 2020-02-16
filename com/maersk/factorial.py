def fact(num):
    result = 1
    if num <= 0:
        return result
    else:
        while num >= 1:
            result = result * num
            num = num - 1
        return result


n = int(input("Enter the number: "))
print("The Factorial of", n, "is :", fact(n))
