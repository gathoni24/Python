temperature = 13

if temperature > 25:
    print("it is hot")
else:
    print("it is cold")

# Program that returns the largest number among 3 numbers
num1 = 45
num2 = 56
num3 = 21

if num1 > num2 and num1 > num3:
    print(num1,"is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2,"is the largest number")
else:
    print(num3,"is the largest number")

# Program that returns the smallest number among 3 numbers

if num1 < num2 and num1 < num3:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")

# Program that checks whether a number is odd or even
number = 0

if number % 2 == 0 :
    print(number, "is even")
else :
    print(number,"is odd")

# Program that checks whether a number is a prime number
num = 5
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


