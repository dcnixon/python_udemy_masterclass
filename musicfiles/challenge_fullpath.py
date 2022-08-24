# Start at a specified directory, use Start as an argument
# Return a relative directory
# extension as a second parameter

# Optional extra - make paths absolute
import os
import fnmatch


def file_path(start, extension):

    for path, _, files in os.walk(start):
        for file in fnmatch.filter(files, '*.' + extension):
            absolute_path = os.path.abspath(path)       # create absolute path
            yield os.path.join(absolute_path, file)     # use it in yielded values


for f in file_path('music', 'emp3'):
    print(f)