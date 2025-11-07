def string_and_replace():
    pass

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
motto="Make "+ "haste "+ "slowly." #motto_strong "" .join(motto)
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