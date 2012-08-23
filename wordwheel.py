#!/usr/bin/env python
def word_filter(word, special_letter, letters_count):
    if special_letter not in word:
        return False
    if len(word) < 4:
        return False
    p_letters_count = letters_count.copy()
    for letter in word:
        if letter in p_letters_count and p_letters_count[letter] > 0:
            p_letters_count[letter] -= 1
        else:
            return False
    return True

def dictionary_filter(special_letter, letters, dictionary_file = open('/usr/share/dict/words', 'r')):
    special_letter = special_letter.lower()
    letters = letters.lower()

    letters = letters + special_letter

    letters_count = {}
    for letter in letters:
        letters_count[letter] = letters_count.get(letter, 0) + 1
    for word in dictionary_file:
        if word_filter(word.strip(), special_letter, letters_count):
            yield word.strip()
    
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 3 and len(argv[1]) == 1:
        special_letter = argv[1]
        letters = argv[2]
    elif len(argv) == 1:
        special_letter = 'e'
        letters = 'eeppprtu'
    else:
        print "usage: %s [special_letter, other_letters]" % argv[0]
        print
        print "Script to help solve the wordwheel newspaper puzzle."
        print "The challenge is to find as many words as possible containing the special letter and atleast 3 of the letters but no other letters."
        from sys import exit
        exit(1)

    for word in dictionary_filter(special_letter, letters):
        print word
