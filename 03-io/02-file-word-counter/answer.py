# -*- encoding: utf-8 -*-


def filter_non_alpha(s):
    return s.translate(str.maketrans('', '', ',.|@-"\''))


def wordstat(s, ans):
    if ans is None:
        ans = dict()
    for word in s.split():
        ans[word] = ans.get(word, 0) + 1
    return ans


def word_in_file(filename):
    ans = None
    with open(filename, 'r') as inf:
        for line in inf:
            ans = wordstat(filter_non_alpha(line).lower(), ans)
    return ans


def stat_to_file(filename, ans):
    with open(filename, 'w') as outf:
        for k, v in ans.items():
            outf.write('%s %s\n' % (k, v))


def main():
    ans = word_in_file('article.txt')
    stat_to_file('output.txt', ans)


main()
