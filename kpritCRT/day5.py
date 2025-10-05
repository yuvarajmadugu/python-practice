# #store the following word meaning in a pythonn dictionary:
# worddict = {
#     "table":[
#         "a piece of furniture",
#         "list of facts"
#     ],
#     "cat":"a small animal"
# }
# # worddict["table"][0] = "ok"
# # print(worddict)
# print(worddict["table"][1])



# #wap to take user marks, store in dict
# mydict = {}
# for i in range(1,4):
#     sub = input(f"Enter name of subject {i}: ")
#     marksOfSub = input(f"Enter marks of {sub}: ")
#     mydict.update({sub : marksOfSub})
# print(mydict)


# #wap to create a dict where the key is a num from 1-10 and the values is the square of the key
# mydict = {}
# for i in range(1,11):
#     mydict.update({i:(i*i)})
#     # print({i:(i*i)},sep="\n")
# print(mydict)


#Implement a frequency counter for words in a paragraph using dictionaries.
import string

# Sample paragraph
paragraph = """
Python is a powerful programming language. It is widely used in data science, machine learning, and web development. 
Python is loved for its simplicity and readability.
"""

# Convert the paragraph to lowercase and remove punctuation
cleaned_paragraph = paragraph.lower().translate(str.maketrans('', '', string.punctuation))

# Split the paragraph into words
words = cleaned_paragraph.split()

# Create an empty dictionary to store word frequencies
word_freq = {}

# Count the frequency of each word
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Display the word frequency
for word, count in word_freq.items():
    print(f"{word}: {count}")
