from copy_between_drives import dir_to_list, the_copy


def scan(path_from, path_to):

    dirs = dir_to_list.to_list(path_to)

    dir_to_cop = path_to.rsplit("/", 1)[1]

    if dir_to_cop not in dirs:

        the_copy.copy(path_from, path_to)

    else:

        return True
