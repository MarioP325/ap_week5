# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
magic= "abracadabra"
print(magic[5])
print(magic[9])
print(magic.find("c"))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
hij=alphabet[7:10]
hij_index=alphabet.index("hij")
print(hij_index)
print(alphabet[7:10])
am=alphabet[1:13]
print(alphabet[0:13:2])
print(am[::2])
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(len(quote))
print(quote[83:98])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
info = "Python is fun. Fun is good. Good is subjective."
print(info.rfind("subjective"))
print(info[36:])
print(info.split()[::3])
print(info[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
force="MAY THE FORCE BE WITH YOU."
print(force.lower())
print("MAY THE FORCE BE WITH YOU.".lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
motto="Make "+ "haste "+ "slowly."
print(motto)
print(motto.split("a"))
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence="Life is what happens when you are busy making other plans."
print(sentence.replace("busy", "distracted"))
new_sentence=(sentence.replace("busy", "distracted"))
print(new_sentence.replace("plans", "mistakes"))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
iteration="Iteration"
print(iteration * 7)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote1="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(quote1.find("moonlight"))
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
quote3="Supercalifragilisticexpialidocious"
print(len(quote3))
print(quote3.count("i"))