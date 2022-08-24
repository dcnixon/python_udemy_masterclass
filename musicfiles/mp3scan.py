import os
import fnmatch
import id3reader_p3 as id3reader


def file_path(start, extension):

    for path, _, files in os.walk(start):
        for file in fnmatch.filter(files, '*.' + extension):
            absolute_path = os.path.abspath(path)       # create absolute path
            yield os.path.join(absolute_path, file)     # use it in yielded values


error_list = []   # initialise the list to store problem file names catch errors
for f in file_path('music', 'emp3'):
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}, \nFile: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title'),
            f
        ))
    except:
        error_list.append(f)

# print the files that caused errors
if len(error_list) > 0:
    print("There was an error precessing the following file(s):")
    for error_file in error_list:
        print(error_file)

    # Modify program to handle exceptions raised by id3reader module
    # If exception is found record the filename in a list and move to the next
    # Print list of files that caused  errors