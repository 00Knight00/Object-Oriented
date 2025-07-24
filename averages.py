# This program calculates the sum, count, and average of numbers entered by the user.
# The user can enter as many numbers and then type q to finish.
# It will print to screen the results

# Initialize variables
total = 0
count = 0

# Start a loop to get user input and check if a user wants to quit by inputting q and exit the loop
while True:
    user_input = input("Enter a number or 'q' to quit: ")

    if user_input == 'q':
        break  

# Convert the input to a number and update total and count
    number = float(user_input)
    total += number
    count += 1

# Will only show results if atleast one number is entered
if count > 0:
    average = total / count  # Calculate average

    print(f"The sum of the numbers is {total}.")
    print(f"The count of the numbers is {count}.")
    print(f"The average of the numbers is {average}.")
else:
    print("No number was inputted")
