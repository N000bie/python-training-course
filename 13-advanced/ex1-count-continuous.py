def count_continuous(lst):
    last = None
    count = 0
    for ele in lst:
        if last == ele:
            count += 1
            continue
        else:
            if last is not None:
                yield last, count
            last = ele
            count = 1
    yield last, count


if __name__ == '__main__':
    # print(count_continuous([1, 1, 1, 2, 3, 3, 1, 1, 1]))
    print(list(count_continuous([1, 1, 1, 2, 3, 3, 1, 1, 1])))
