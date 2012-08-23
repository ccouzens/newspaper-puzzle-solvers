#!/usr/bin/env python

clue = "[bl][ua][sp][st]"
#clue = "c.."
word_knowledge = []
while clue != '':
    if clue[0] == '.':
        word_knowledge.append(set(chr(x) for x in xrange(97, 97+26)))
        clue = clue[1:]
    elif clue[0] == '[':
        potential = []
        clue = clue[1:]
        while clue[0] != ']':
            potential.append(clue[0])
            clue = clue[1:]
        clue = clue[1:]
        word_knowledge.append(set(potential))
    else:
        word_knowledge.append(clue[0])
        clue = clue[1:]

for word in open('/usr/share/dict/words', 'r'):
    word = word.strip()
    if len(word) != len(word_knowledge):
        continue
    valid = True
    for letter, clue in zip(word, word_knowledge):
        if letter not in clue:
            valid = False
            break
    if not valid:
        continue
    print word
