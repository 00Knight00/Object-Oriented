# This program will process a list of employee names and sort the names by last name
# create usernames by using the first 5 letters of the last names and first 2 of the first name 
# by using lambda functions

# The list of names
names_list = ['Frank Harrelson', 'Bob Charles', 'Bob Franklin', 'Bob Brody', 'Frank Charles', 'Bob Harrelson',
    'Mack Dobson', 'John Jones', 'Rob Franklin', 'Tom Simpson', 'Rob Harrelson', 'John Brody',
    'Frank Jones', 'John Harrelson', 'Frank Charles', 'Tom Charles', 'Frank Franklin', 'Frank Charles',
    'John Charles', 'John Franklin', 'Frank Dobson', 'Diane Jones', 'Bob Dobson', 'Tom Harrelson',
    'Rob Simpson', 'Tom Brody', 'Rob Harrelson', 'John Charles', 'Bob Dobson', 'Bob Brody']

# Sort the names alphabetically by last name using a lambda function
# x.split()[1] gets the last name from the full name string
names_list.sort(key=lambda x: x.split()[1])

# Create the usernames first 5 letters of last name + first 2 of first name
usernames = list(map(lambda x: x.split()[1][:5].lower() + x.split()[0][:2].lower(), names_list))

# Print to the sorted names
print("The Sorted Names:")
print(names_list)

# Print the usernames made
print("\nThe Usernames:")
print(usernames)
