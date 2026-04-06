import random
# print(random.randint(1,100))
import numpy as np
dice = random.randint(56, 65)

Coin = random.choice(["Head", "Tail"])

print(dice, Coin)
print(np.random.randint(0, 5, 2))

emails = ["spam"]*20 + ["Not_spam"]*80

p_spam = emails.count("spam")/len(emails)

print(p_spam)
