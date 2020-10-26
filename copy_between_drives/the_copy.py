import os


def copy(path_from, path_to):

    os.popen("sudo cp -r {0} {1}".format(path_from, path_to))

    return