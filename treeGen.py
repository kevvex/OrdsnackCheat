from treelib import Node, Tree

class TreeGenerator:
    tree = None
    word = None
    wordList = []

    def __init__(self, word, wordList):
        self.tree = Tree()
        self.word = word
        self.wordList = wordList

        print(word)
        print(wordList)

    def generateTreeLevels(self, word):
        self.tree.create_node("Root", "root")
        for i in range(len(word), 0, -1):
            self.tree.create_node(f'Level {i}', str(i), parent="root")

    def putWordsOnCorrectLevel(self):
        for w in self.wordList:
            for i in range(len(self.word), 0, -1):
                if len(w) == i:
                    self.tree.create_node(w, parent=str(i))

    def generate(self):
        self.generateTreeLevels(self.word)
        self.putWordsOnCorrectLevel()
        self.tree.show()

    def generate_graphviz(self):
        self.generateTreeLevels(self.word)
        self.putWordsOnCorrectLevel()
        self.tree.to_graphviz()