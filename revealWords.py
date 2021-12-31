import sys
from itertools import permutations

def findWordPermutations(word):
    return [''.join(p) for p in permutations(word)]

def findWordList(lettersInWord, file):
    perms = findWordPermutations(lettersInWord)
    newList = [e.strip() for e in file.readlines()]
    matchList = []
    for perm in perms:
        for word in newList:
            if perm == word:
                matchList.append(word)
            #print(f'{perm} == {word} -> {foundWord}')

    return set(matchList)

def main():
    file = open('svenska-ord.txt', 'r')
    word = sys.argv[1]
    wordList = findWordList(word, file)

    permWord = findWordPermutations(word)
    print(len(set(permWord)))

    if wordList == set():
        print('No result found')

    for word in wordList:
        print(word)
    file.close()

main()