#Christopher Salley
#Mid-term Problem 2

#The code will ask the user for a phrase.
#An acronym will take the first letter of each word and put them together to make a new word.
#The acronym will be all uppercase even if the phrase is not.

words = input("Please enter a phrase.")
acronym = ''.join(word[0] for word in words.upper().split())
print(acronym)