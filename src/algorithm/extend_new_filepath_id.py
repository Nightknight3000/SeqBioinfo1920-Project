import os


def extend_new_filepath_by_copy_id(new_filepath, directory):
    list_of_files = os.listdir(directory)
    if new_filepath.split('/')[-1] in list_of_files:
        new_filepath = '.'.join(new_filepath.split('.')[:-1]) + '_' \
                       + str(sum([1 if file.startswith(new_filepath.split('/')[-1]) else 0
                                  for file in list_of_files]) + 1) \
                       + ".fasta"
    return new_filepath
