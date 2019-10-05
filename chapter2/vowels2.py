vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
# A dictionary is a collection of key/value pair,
#  where each unique key has a value associated with it.
# They are unordered and mutable. Pytnon stores them in no partular order.
# A dictionary lookup is fast due to a built-in hashing algorithm.
# In computer science and other programming language it's an associate array.
# In C++ and Java they are "map", in Perl and Ruby they are "hash".
# Data that conforms to the dictionary model is easy to spot:
#  There are two columns with multiple rows. Check Chapter 3.
found = {} # An empty dictionary. It'll be stored like {a:0, e:0, ...}
for letter in word: # For every letter in the word variable.
    if letter in vowels: # If the letter in the word is in the vowels list...
        # To stop the KeyError in Python since nothing was set in the found dictionary.
        # Add a vowel letter as a key and set initial value to 0. 
        # If the letter key exists nothing will happen. 
        found.setdefault(letter, 0)
        # Increment by one everytime the letter is found.
        found[letter] += 1 # Remember the value of the keys is an integer.
        # On page 119, in Okular 159 of 624.
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
