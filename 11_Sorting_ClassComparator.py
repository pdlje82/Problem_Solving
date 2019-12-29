'''
https://www.hackerrank.com/challenges/ctci-comparator-sorting
'''
from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        print("player name: ", self.name)
        # print("player score: ", self.score)

    def comparator(self, other):
        if self.score < other.score:
            return 1
        elif self.score == other.score:
            if self.name < other.name:
                return -1
            elif self.name == other.name:
                return 0
            else:
                return 1
        else:
            return -1

data = []
input = [["smith", 20],
        ["jones", 15],
        ["jones", 20]]


for e in input:
    name, score = e[0], e[1]
    score = int(score)
    player = Player(name, score)
    data.append(player)
#print(data)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
