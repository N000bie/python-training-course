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
    with __?__:
        for __?__:
            ans = wordstat(__?__, __?__)
    return ans


def stat_to_file(filename, ans):
    with __?__:
        for __?__:
            outf.write(__?__)


def main():
    ans = word_in_file('article.txt')
    stat_to_file('output.txt', ans)


main()
