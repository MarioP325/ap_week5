def manipulate():
    pass
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