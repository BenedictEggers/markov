# Ben Eggers <ben.eggers36@gmail.com>
#
# Main program for the Markov Chain. Makes it easier to interact with.


import markov


def main():
    c = markov.Chain()

    action = get_action()

    while action is not 'q':
        if action is 'g':
            times = int(raw_input("How many sentences would you like to generate? "))
            for _ in xrange(times):
                print c.generate()
        elif action is 't':
            train(c)
        elif action is 'c':
            c.clear()
        else:
            print "I don't recognize that."

        action = get_action()


def get_action():
    return raw_input("Would you like to (g)enerate, (t)rain, (c)lear, or (q)uit? ")


def train(c):
    fname = raw_input("What file would you like to train on? ")
    try:
        f = open(fname)
        tokens = ''.join(f.readlines()).split(" ")
        sentences = [[]]

        for t in tokens:
            sentences[-1].append(t)
            if terminal_token(t):
                sentences.append([])

        for s in sentences:
            c.add_sentence(s)

    except IOError:
        print "That's not a valid file name."


def terminal_token(t):
    return t.endswith('.') or t.endswith('!') or t.endswith('?') or t.endswith(';')


if __name__ == "__main__":
    main()
