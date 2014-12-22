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
        return self.children[random.randint(0, len(self.children) - 1)]


class Chain:

    def __init__(self):
        self.start = MarkovNode("")
        self.nodes = {}


    def add_sentence(self, sent):
        if len(sent) is 0:
            return

        self.start.add_child(sent[0])
        for i in xrange(len(sent) - 1):
            if sent[i] not in self.nodes:
                self.nodes[sent[i]] = MarkovNode(sent[i])
            self.nodes[sent[i]].add_child(sent[i + 1])

        if not sent[-1] in self.nodes:
            self.nodes[sent[-1]] = MarkovNode(sent[-1])


    def generate(self):
        sentence = ""

        if not self.start.has_next():
            # Hasn't been trained yet
            return ""

        current = self.start.next()
        if not self.nodes[current].has_next():
            # One-word sentence
            return current

        while self.nodes[current].has_next():
            sentence += " " + current
            current = self.nodes[current].next()

        return sentence[1:] + current


    def clear(self):
        self.nodes = {}

