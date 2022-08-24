import os
import fnmatch


def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):   # we want the path, not the name of the album
            yield song

# As we loop through these, we only look at them as we need them Creating and destroying lists can take a lot of memory
# Generators look at objects more one by one, rather than loading the lot into memory first

album_list = find_albums('music', "black*")
song_list = find_songs(album_list)

# for s in song_list:
#     print(s)

for a in album_list:
    print(a)
