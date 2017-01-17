import random

noun = ("The man", "The woman", "The dog", "The cat", "The boy", "The girl")
verbs = ("runs", "walks", "talks", "listens", "drives", "sleeps")
adv = ("rapidly", "amanzingly", "incredibly", "horribly", "jokingly", "seriously")
adj = ("fast", "quick", "sweet", "cool", "well", "bad")

word = random.randrange(0,6)
print(noun[word] + ' ' + verbs[word] + ' ' + adv[word] + ' ' + adj[word] + '.')