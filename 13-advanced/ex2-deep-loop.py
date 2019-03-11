from itertools import product

print([
    'B{}C{}S{}P{}'.format(b,c,s,p) for b,c,s,p in product(
        range(1, 3), range(1, 4), range(1, 3), range(1, 4)
    )
])
