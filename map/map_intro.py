import timeit

text = "what have the romans ever done for us"


def capitals():
    return [char.upper() for char in text]


# use map
def map_capitals():
    return list(map(str.upper, text))


def words():
    return [word.upper() for word in text.split(' ')]


# use map
def map_words():
    return list(map(str.upper, text.split(' ')))


if __name__ == '__main__':
    print(capitals())
    print(map_capitals())
    print(words())
    print(map_words())

    print(timeit.timeit(capitals, number=100000))
    print(timeit.timeit(map_capitals, number=100000))
    print(timeit.timeit(words, number=100000))
    print(timeit.timeit(map_words, number=100000))
