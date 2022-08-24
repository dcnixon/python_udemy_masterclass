def average(*args):
    print(type(args))
    print("args is: {}".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    """Takes a variable number of arguments and returns a tuple containing the values passed to it"""
    return args


def average_word_len(*args):
    """Takes a variable number of words and returns the average word length"""
    mean = 0
    for arg in args:
        mean += len(arg)
    return mean / len(args)


def smallest(*args):
    """returns the smallest number passed to it"""
    return min(args)


def print_backwards(*args, **kwargs):
    """my own solution for the challenge of the case when the user specifies end="""
    print(kwargs)
    if 'end' in kwargs.keys():
        for word in args[::-1]:
            print(word[::-1], **kwargs)
    else:
        for word in args[::-1]:
            print(word[::-1], end=' ', **kwargs)


def print_backwards2(*args, end=' ', **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


def print_backwards3(*args, **kwargs):
    print(kwargs)
    kwargs.pop('end')
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)

def print_backwards0(*args, **kwargs):
    end_char = kwargs.pop('end', '\n')
    sep_char = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:
        print(word[::-1], end=sep_char, **kwargs)
    print(args[0][::-1], end=end_char, **kwargs)
    # print(end=end_char)

# print(average(1, 2, 3, 4))

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
# print(type(message_tuple))
# print(message_tuple)
#
# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)
#
# print(average_word_len(*message_tuple))
# print(smallest(*number_tuple))

print_backwards0(*message_tuple, end='\n')
print("Another String")

print()
print(*message_tuple, end='', sep='|')
print_backwards0(*message_tuple, end='', sep='|')
print("=" * 10)