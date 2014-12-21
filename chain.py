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

    def next(self):
        return self.children[random.randint(len(self.children) - 1)]


class Markov:
    def __init__(self):
        self.start = 
