from treelib import Node, Tree

class TreeGenerator:
    tree = None
    word = None
    wordList = []

    def __init__(self, word, wordList):
        self.tree = Tree()
        self.word = word
        self.wordList = wordList

    def generateTreeLevels(self, word):
        self.tree.create_node("Root", "root")
        for i in range(len(word), 0, -1):
            self.tree.create_node(f'Level {i}', str(i), parent="root")

    def putWordsOnCorrectLevel(self, listWords):
        for w in listWords:
            for i in range(len(self.word), 0, -1):
                if len(w) == i:
                    self.tree.create_node(w, parent=str(i))

    def generate(self):
        self.generateTreeLevels(self.word)
        self.putWordsOnCorrectLevel(listWords)
        self.tree.show()

    def generate_graphviz(self):
        self.generateTreeLevels(self.word)
        self.putWordsOnCorrectLevel(listWords)
        self.tree.to_graphviz()

listWords = ['lösning', 'ösning', 'löning', 'snöig', 'sling', 'sölig', 'lönn', 'glis', 'sinn', 'lögn', 'gnöl', 'lins', 
'slig', 'ösig', 'lin', 'gin', 'lös', 'göl', 'slö', 'sil', 'söl', 'sin', 'gös', 'gli', 'sig', 'lön', 'snö', 
'si', 'in', 'is', 'il', 'ös', 'öl', 'ö', 'i', 'n', 's', 'l', 'g']
treegen = TreeGenerator('lösning', listWords)
#treegen.generate()
#tree.to_graphviz()