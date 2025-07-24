# import numpy, use command pip install numpy if not on computer
import numpy

# Example 1: Using numpy.mean() to calculate the average of random numbers
print("Example 1:")

# Generate an array of 8 random integers between 1 and 50
generated_numbers = numpy.random.randint(1, 51, size=8)
print("Numbers:", generated_numbers) 

# Calculate the mean of the numbers using numpy.mean()
mean_value = numpy.mean(generated_numbers)
print("Mean:", mean_value)  

# Loop through each number and print it if it is greater than the mean
print("Numbers greater than the mean:") 
for num in generated_numbers:
    if num > mean_value:
        print(num)
        
        
#  Example 2: Using numpy.square() to square elements in an array
print("\nExample 2: Using numpy.square() to square elements in an array")

# Create a NumPy array with specific integer values
values = numpy.array([2, 4, 6, 8, 10])

# numpy.square() to square each element in the array
squared = numpy.square(values)
print("Squared Values:", squared)

# Loop through each squared value and print it if it's greater than 30
print("Values greater than 30:")
for val in squared:
    if val > 30:
        print(val)
        
        
# Example 3: numpy.isnan() to identify missing values
print("\nExample 3:")

# Create a NumPy array with some missing nan values
data = numpy.array([7.0, numpy.nan, 12.0, 5.0, numpy.nan])
print("Original Data:", data)

# Loop through each index in the array
# Use numpy.isnan() to check if the value at each index is nan
# If it is, print the index and indicate it's a missing value
print("The Index and value of missing data:")
for i in range(len(data)):
    if numpy.isnan(data[i]):
        print(f"Index {i} is nan")
