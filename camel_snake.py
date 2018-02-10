import itertools
import re
import timeit


def c1(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def c2(string):
    """ Convert string into camel case.
    Args:
        string: String to convert.
    Returns:
        string: Camel case string.
    """

    string = re.sub(r"^[\-_\.]", '', str(string))
    if not string:
        return string
    return string[0].lower() + re.sub(r"[\-_\.\s]([a-z])", lambda matched: matched.group(1).upper(), string[1:])


r1 = re.compile('(.)([A-Z][a-z]+)')
r2 = re.compile('([a-z0-9])([A-Z])')

def camel_to_snake(text):
    str1 = re.sub(r1, r'\1_\2', text)
    return re.sub(r2, r'\1_\2', str1).lower()


_reg = re.compile(r'(?!^)(?<!_)([A-Z])')


def camelToSnake(s):
    """ 
    Is it ironic that this function is written in camel case, yet it
    converts to snake case? hmm..
    """
    return _reg.sub(r'_\1', s).lower()


def snake2(s):
    buf = []
    first = True
    lastUpper = False
    normal, lookahead = itertools.tee(s)
    next(lookahead)

    for (c, ahead) in itertools.zip_longest(normal, lookahead):
        if first:
            first = False
            lastUpper = c.isupper()
        elif c.isupper():
            if not lastUpper or (ahead and ahead.islower()):
                buf.append('_')
            lastUpper = True
        else:
            lastUpper = False
        buf.append(c.lower())

    return ''.join(buf)


def snakecase(string):
    """Convert string into snake case.
    Join punctuation with underscore
    Args:
        string: String to convert.
    Returns:
        string: Snake cased string.
    """

    string = re.sub(r"[\-\.\s]", '_', str(string))
    if not string:
        return string
    return string[0].lower() + re.sub(r"[A-Z]", lambda matched: '_' + matched.group(0).lower(), string[1:])


# print(timeit.timeit('c1("__snake_to__CAMel") ', number=10000, globals=globals()))
# print(timeit.timeit('c2("__snake_to__CAMel") ', number=10000, globals=globals()))

s = "IPhoneHysteriaOnceUponATime"

print(timeit.timeit('camel_to_snake(s) ', number=10000, globals=globals()))
print(timeit.timeit('snakecase("IPhoneHysteriaOnceUponATime") ', number=10000, globals=globals()))
print(timeit.timeit('camelToSnake("IPhoneHysteriaOnceUponATime") ', number=10000, globals=globals()))
print(timeit.timeit('snake2("IPhoneHysteriaOnceUponATime") ', number=10000, globals=globals()))

