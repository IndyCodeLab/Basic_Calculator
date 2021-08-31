import math
calc = "yes"
use_result = "no"

while calc == "yes":
    user_math = float(input("What operation would like to perform?\n\t(1) Addition\n\t(2)Subtraction\n\t(3)Multiplication\n\t(4)Division\n\t(5)Exponentation\n\t(6)Square Root\n\t(7)Factorial\n"))
    if user_math == 1:
        if use_result != "yes" :
            num_1 = float(input("Number 1: "))
        else:
            result = num_1
        num_2 = float(input("Number 2: "))
        print(str(num_1) + " + " + str(num_2) + " = " + str(num_1 + num_2))
        result = num_1 + num_2
    elif user_math == 2:
        if use_result != "yes" :
            num_1 = float(input("Number 1: "))
        else:
            result = num_1
        num_2 = float(input("Number 2: "))
        print(str(num_1) + " - " + str(num_2) + " = " + str(num_1 - num_2))
        result = num_1 - num_2
    elif user_math == 3:
        if use_result != "yes" :
            num_1 = float(input("Number 1: "))
        else:
            result = num_1
        num_2 = float(input("Number 2: "))
        print(str(num_1) + " x " + str(num_2) + " = " + str(num_1 * num_2))
        result = num_1 * num_2
    elif user_math == 4:
        if use_result != "yes" :
            num_1 = float(input("Number 1: "))
        else:
            result = num_1
        num_2 = float(input("Number 2: "))
        print(str(num_1) + " / " + str(num_2) + " = " + str(num_1 / num_2))
        result = num_1 / num_2
    elif user_math == 5:
        if use_result != "yes" :
            num_1 = float(input("Base: "))
        else:
            result = num_1
        num_2 = float(input("Exponent: "))
        print(str(num_1) + " ** " + str(num_2) + " = " + str(num_1 ** num_2))
        result = num_1 ** num_2
    elif user_math == 6:
        if use_result != "yes" :
            num_1 = float(input("Number: "))
        else:
            result = num_1
        print("The square root of " + str(num_1) + " = " + str(math.sqrt(num_1)))
        result = math.sqrt(num_1)
    elif user_math == 7:
        if use_result != "yes" :
            num_1 = float(input("Number: "))
        else:
            result = num_1
        print(str(num_1) + " ! = " + str(math.factorial(num_1)))
        result = math.factorial(num_1)
    else:
        print("Invalid Operation")
    calc = input("Would you like to continue operations? (yes/no) ")
    use_result = input("Would you like to use the previous result? (yes/no) ")
    
    
print("Thanks for using my calculator!")
