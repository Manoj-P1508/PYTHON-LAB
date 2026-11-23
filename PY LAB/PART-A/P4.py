text=input("Enter a string:")
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for char in text:
    if char.isalpha():
        vowel_count+=1
    else:
        consonant_count+=1
print("Number of Vowels:",vowel_count)
print("Number of consonants:",consonant_count)