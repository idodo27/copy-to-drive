import os
import elevate
from copy_between_drives import dir_to_list, file_or_dir, files_scan, path_joiner, scan_dir


def the_run(path_from, path_to_1):

    first_dir = dir_to_list.to_list(path_from)

    for obj_1 in first_dir:
        path_to_check_1 = path_joiner.pathy(path_from, obj_1)

        os.rename(path_to_check_1, path_to_check_1.replace(" ", "_"))

        if file_or_dir.check(path_to_check_1) == 1:

            files_scan.scan(path_to_check_1, path_to_1)

        elif file_or_dir.check(path_to_check_1) == 2:

            if scan_dir.scan(path_to_check_1, path_to_1):

                sec_dir = dir_to_list.to_list(path_to_check_1)

                path_to_2 = path_joiner.pathy(path_to_1, obj_1)

                for obj_2 in sec_dir:
                    path_to_check_2 = path_joiner.pathy(path_to_check_1, obj_2)

                    os.rename(path_to_check_2, path_to_check_2.replace(" ", "_"))

                    if file_or_dir.check(path_to_check_2) == 1:

                        files_scan.scan(path_to_check_2, path_to_2)

                    elif file_or_dir.check(path_to_check_2) == 2:

                        if scan_dir.scan(path_to_check_2, path_to_2):
                            third_dir = dir_to_list.to_list(path_to_check_2)

                            path_to_3 = path_joiner.pathy(path_to_2, obj_2)

                            for obj_3 in third_dir:
                                path_to_check_3 = path_joiner.pathy(path_to_check_2, obj_3)

                                os.rename(path_to_check_3, path_to_check_3.replace(" ", "_"))

                                if file_or_dir.check(path_to_check_3) == 1:

                                    files_scan.scan(path_to_check_3, path_to_3)

                                elif file_or_dir.check(path_to_check_3) == 2:

                                    if scan_dir.scan(path_to_check_3, path_to_3):
                                        forth_dir = dir_to_list.to_list(path_to_check_3)

                                        path_to_4 = path_joiner.pathy(path_to_3, obj_3)

                                        for obj_4 in forth_dir:
                                            path_to_check_4 = path_joiner.pathy(path_to_check_3, obj_4)

                                            os.rename(path_to_check_4, path_to_check_4.replace(" ", "_"))

                                            if file_or_dir.check(path_to_check_4) == 1:

                                                files_scan.scan(path_to_check_4, path_to_4)

                                            elif file_or_dir.check(path_to_check_4) == 2:

                                                if scan_dir.scan(path_to_check_4, path_to_4):
                                                    fifth_dir = dir_to_list.to_list(path_to_check_4)

                                                    path_to_5 = path_joiner.pathy(path_to_4, obj_4)

                                                    for obj_5 in fifth_dir:
                                                        path_to_check_5 = path_joiner.pathy(path_to_check_4, obj_5)

                                                        os.rename(path_to_check_5, path_to_check_5.replace(" ", "_"))

                                                        if file_or_dir.check(path_to_check_5) == 1:

                                                            files_scan.scan(path_to_check_5, path_to_5)

                                                        elif file_or_dir.check(path_to_check_5) == 2:

                                                            if scan_dir.scan(path_to_check_5, path_to_5):
                                                                sixth_dir = dir_to_list.to_list(path_to_check_5)

                                                                path_to_6 = path_joiner.pathy(path_to_5, obj_5)


elevate.elevate()

the_run("/drive1", "/drive2")

print("done")
