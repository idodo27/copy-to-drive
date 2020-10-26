import os


def check(path):

    res = 0

    if os.path.isfile(path):

        res = 1

    elif os.path.isdir(path):

        res = 2

    else:

        return 0

    return res