# python program for a calculator (simple)

# Add functions to add two numbers (can be more numbers)
def add (num1, num2):
    return num1 + num2

# function to subtract
def subtract (num1, num2):
    return num1 - num2

# function to multiply
def multiply (num1, num2):
    return num1 * num2

# function to divide
def divide (num1, num2):
    return num1 / num2

# selecting the operation
print("please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")

#take an input from the user
select = int(input("select from one of the following operations: 1, 2, 3, 4 :"))

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if select == 1:
    print(number_1, "+", number_2, "=" ,
                    add (number_1, number_2))
    
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
        

