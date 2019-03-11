from itertools import combinations_with_replacement, starmap


def solver(sections, darts, score):
    candidates = filter(
        lambda solution: sum(solution) == score,
        combinations_with_replacement(sections, r=darts)
    )
    return ['-'.join(str(s) for s in x) for x in candidates]


if __name__ == '__main__':
    print(solver([3, 7, 11, 14, 18, 20, 25], 3, 32))
