# Assignment A4
# CS 1400
# Starter code by David Johnson
# Assignment completed by Jason Nguyen

# The multiply function computes the product of two factors with repeated adding
def multiply(factor1, factor2):
    product = 0
    for counter in range(factor2):
        product += factor1
    return product

#ADD YOUR FUNCTIONS BELOW HERE (AND REMOVE THIS LINE)
 #Choose larger func
def choose_larger(num1,num2):
    if num1 >= num2:
        return num1
    else:
        return num2
# Input numbers for num1-2
choose_number = choose_larger(1, 20)
print(choose_number)

# Describe number func
def describe_number(number):
    if number ==0:
        return "zero"
    elif number > 0:
        return "positive"
    elif number < 0:
        return "negative"
# Input 0 to test code
input_number = describe_number(0)
print(input_number)


# ADD YOUR (FUNCTIONS) ABOVE HERE (AND REMOVE THIS LINE)

# Main tests all the functions and reports on their results
def main():
    print("Testing the multiply function")
    print("Testing multiply(2,3). Expecting a result of 6 and computed a result of", str(multiply(2,3)) + ".")
    print("Testing multiply(5,6). Expecting a result of 30 and computed a result of", str(multiply(5,6)) + ".")
    print()

if __name__=="__main__":
    main()