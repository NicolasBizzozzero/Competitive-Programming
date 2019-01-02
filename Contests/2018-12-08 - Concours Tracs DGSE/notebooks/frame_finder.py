import os
import operator
from typing import Dict


PATH_DIR = "frames"


def list_files_by_size(path_dir: str) -> Dict[str: int]:
    """ Compute the size in bytes of all files in a directory.
    Ignore all directories. Follows symbolic links.
    """
    files = dict()
    for file in os.listdir(path_dir):
        if os.path.isfile(file):
            path_file = os.path.join(path_dir, file)
            size = os.path.getsize(path_file)
            files[path_file] = size
    return files


files = list_files_by_size(PATH_DIR)
sorted_x = sorted(files.items(), key=operator.itemgetter(1))
print(sorted_x)
