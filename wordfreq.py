import re
def word_freq(book, word):
    # Check edge case if book is None or empty array/list
    if book is None or word is None or len(book) == 0 or word == "":
        return -1

    # Initialize a counter to count all occurrences of the word
    count = 0
    
    # Loop through every string in the book
    for s in range(0, len(book)):
        # Convert string to all lowercase to remove case sensitivity
        book[s] = book[s].strip(" ").lower()
        # Check to see if s is equal to the word.
        # We also convert the word to lowercase to remove case sensitivity.
        if book[s] == word.lower():
            # If the element in the book and word are equal, increase counter
            count += 1
        # Else, do nothing
    return count
book = [" The", "dog", "jumped", "in", "the", "dog", "house"]
word = "the"
book_1 = [" The", "dog", "jumped", "in", "the", "dog", "house"]
word_1 = ""
print(word_freq(book, word))
print(word_freq(book_1, word_1))