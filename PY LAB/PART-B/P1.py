import string

text=input("Enter a string:")

#convert to lower case
text=text.lower()

#remove punctuation
text=text.translate(str.maketrans("","",string.punctuation))

#split the string into words
words=text.split()

# create a dictonary to store words count
word_count={}

#count occurrences
for word in words:
    word_count[word]=word_count.get(word,0)+1

print("\nWord occurrence:")
for word,count in word_count.items():
    print(f"{word}: {count}")