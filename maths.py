# This program takes two integers input by the user.  The program should return the following:
# sum,difference,product,quotient,remainder,exponent

first_number_entered=int(input("Enter your first number:"))
second_number_entered=int(input("Enter your second number:"))

# Preform and store results of operations in variables
sum_nums = first_number_entered + second_number_entered
difference = first_number_entered - second_number_entered
product = first_number_entered * second_number_entered
quotient = first_number_entered / second_number_entered
remainder = first_number_entered % second_number_entered
exponent = first_number_entered ** second_number_entered

# Print operations 
print("Sum", sum_nums)
print("Difference", difference)
print("Product", product)
print("Quotient", quotient)
print("Remainder", remainder)
print("Exponent", exponent)
