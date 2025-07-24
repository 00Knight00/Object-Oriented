# This program will convert the following phrase "The only thing we have to fear is fear itself"
# into Hetay onlyway hingtay eway avehay otay earfay isway earfay itselfway 
# If a word starts with a vowel it adds way to the end of the word.
# If a word starts with a consonant it moves the first letter to the 
# end of the word and adds "ay".
# After converting all words it will capitalize the first word and print the final result.

# Convert the phrase to a list of words
phrase = "The only thing we have to fear is fear itself"
words = phrase.split()

# Create a new empty list to store the results
secret_words = []

# Defining Vowels
vowels = "aeiouAEIOU"

# Loop through each word and then apply the conversion
for word in words:
    if word[0] in vowels:
        new_word = word + "way"
    else:
        new_word = word[1:] + word[0] + "ay"
    secret_words.append(new_word)

# Capitalize the first word and join the list into a string and print
secret_words[0] = secret_words[0].capitalize()
result = " ".join(secret_words)
print(result)
