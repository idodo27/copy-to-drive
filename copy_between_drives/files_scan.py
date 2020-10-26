import os

from copy_between_drives import path_joiner, the_copy, dir_to_list


def scan(path_from, path_to):

    path_for = dir_to_list.to_list(path_to)

    file_to_copy = path_from.rsplit("/", 1)[1]

    if file_to_copy not in path_for:

        the_copy.copy(path_from, path_to)

    else:

        return True
