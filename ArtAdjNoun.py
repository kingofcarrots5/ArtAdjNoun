import random
with open ("randomPhrase.txt", "w") as fout:
    mush = open('englisharticles.txt', 'r')
    mush2 = open('englishadjectives.txt', 'r')
    mush3 = open('englishnouns.txt', 'r')
    articles = mush.readlines()
    adjectives = mush2.readlines()
    nouns = mush3.readlines()
    randomArt = random.choice(articles)
    randomAdj = random.choice(adjectives)
    randomNoun = random.choice(nouns)
    randPhrase = ("<h2>" + randomArt + randomAdj + randomNoun + "</h2>")
    print(randPhrase, file=fout)
fout.close()