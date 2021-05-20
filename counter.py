import random
random.seed(696969)
with open("champs.txt","r") as f:
    stuff = f.read().split("\n")
    stuff = stuff[:-1]

tiers = [[], [], [], [], [], []]

for champ in stuff:
    score = random.randrange(0,155)
    if (score > 150):
        tiers[0].append(champ)
        continue
    if (score > 135):
        tiers[1].append(champ)
        continue
    if (score > 100):
        tiers[2].append(champ)
        continue
    if (score > 60):
        tiers[3].append(champ)
        continue
    if (score > 30):
        tiers[4].append(champ)
        continue
    else:
        tiers[5].append(champ)

tier_names = ["Z", "A", "B", "C", "D", "DONT"]
for tier in range(len(tiers)):
    print("%s TIER:" % (tier_names[tier]))
    for champ in tiers[tier]:
        print("\t",champ)
