import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

#looping over numbers 1-10
for number in range(1, 11):
    contains = False
    for ranNum in my_randoms:
        if ranNum == number:
            contains = True
    print(
        f"my_randoms list {f'does contain {number}' if contains else f'does not contain {number}'}"
    )
