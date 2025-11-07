def advance_slice():
        pass
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
def extraction():
    pass
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(len(quote))
print(quote[83:98])