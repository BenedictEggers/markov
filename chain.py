# Ben Eggers <ben.eggers36@gmail.com>
#
# This is the markov chain data structure. Since I'm writing this on a bus and
# want to finish it within two hours (the time it'll take for me to get to Seattle),
# it's pretty basic. Maybe I'll add some more funcionality later.


import random


class MarkovNode:
    """
    Hackish markov chain node class.
    """

    def __init__(self, token):
        self.token = token
        self.children = []

    def add_child(self, token):
        # I know, I know, it's offensive. If it becomes untenable I'll fix it
        self.children.append(token)

    def has_next(self):
        return self.children != []

    def next(self):
        return self.children[random.randint(len(self.children) - 1)]


class Markov:
    def __init__(self):
        self.start = MarkovNode("")
        self.nodes = {}

    def add_word(self, parent, next):
        if parent not in self.nodes:
            self.nodes[parent] = MarkovNode(parent)
        if next not in self.nodes:
            self.nodes[next] = MarkovNode(next)
        self.nodes[parent].add_child(next)

    def add_sentence(self, sent):
        if "" in sent:
            # Error handling? Nahhhhh
            return

        self.add_word("", sent[0])
        for i in xrange(len(sent) - 1):
            add_word(sent[i], sent[i + 1])

    def generate(self):
        sentence = ""
        current = self.start
        while self.nodes(current).has_next():
            current = self.nodes[current].next()
            sentence += current + " "

        return sentence[:-1]
