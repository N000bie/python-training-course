dummy_data = {
    0: ['a', 'b', 'c'],
    1: ['I', 'II', 'III', 'IV'],
    2: ['01', '02'],
}


class Response(object):
    __slots__ = ['data']

    def __init__(self, data):
        self.data = data

    def __bool__(self):
        return bool(self.data)


def fetch(url, page):
    return Response(dummy_data.get(page))


def pull_data(url):
    page = 0
    while True:
        response = fetch(url, page)
        if not response:
            break
        for r in response.data:
            yield r
        page += 1


print(list(pull_data('http://dummy.com/data')))
