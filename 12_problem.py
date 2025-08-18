# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

# creating dict
words = { 
    "khana": "eat",
    "madad": "help",
    "khelna": "play"
}

# taking user input
word = input("Enter your word: ")

# final result
print(words[word])
