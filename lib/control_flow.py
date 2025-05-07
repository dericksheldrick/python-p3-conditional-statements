#!/usr/bin/env python3

def admin_login(username, password):
    if ((username == "admin" or username == "ADMIN") and password == "12345"):
        print("Access granted")
        return "Access granted"
    else:
        print("Access denied")
        return "Access denied"
    
admin_login("admin","1234")


def hows_the_weather(temperature):

    if (temperature < 40):
        response = "brisk"
    elif(temperature >= 40 and temperature <= 65):
        response = "a little chilly"
    elif(temperature > 85):
        response = "too dang hot"
    else:
        response = "perfect"
    
    print(f"It's {response} out there!")
    return f"It's {response} out there!"

hows_the_weather(33)


def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return  "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    else:
        return num
    
print (fizzbuzz(13))

def calculator(operation, num1, num2):

    if (operation == "+"):
        return num1 + num2
    elif(operation == "-"):
        return num1 - num2
    elif(operation == "*"):
        return num1 * num2
    elif(operation == "/"):
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    
    # Match case is only used in version 3.10 but I'm using 3.8 but below is the syntax
        # match operation:
    #     case "+":
    #         return num1 + num2
    #     case "-":
    #         return num1 + num2
    #     case "*":
    #         return num1 * num2
    #     case "/":
    #         return num1 / num2
    #     case:
    #         print("Invalid Operation!")

print((calculator("+", 4, 7.3)))