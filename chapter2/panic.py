# You will want to read Chapter 2.
phrase = "Don't panic!"
plist = list(phrase) # Return each character in the phrase string as a list item. 
                     # Store the list items in a 'plist' list to hold.

print(phrase)
print(plist)

for i in range(4): # We are going to do this 4 times.
    plist.pop() # pop() without a parameter removes last item(s) in the list.

# The following lines are methods for lists. Use help(list.pop), help(list.remove), etc.
plist.pop(0) # We count starting with 0 in programming. Remove first index in the list.
plist.remove("'") # Remove the char ['] in whatever location it is in the list if it exist.
# Think 'extend' as append with multiple calls to it.
plist.extend([plist.pop(), plist.pop()]) # Doing this will swap (flip) the last two characters with each other.
plist.insert(2, plist.pop(3)) # Will place on index 2 what was removed on index 3 which here was the space character " ".

new_phrase = ''.join(plist) # Make plist a string.
print(plist)
print(new_phrase)
