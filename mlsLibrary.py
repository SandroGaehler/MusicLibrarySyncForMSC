# Library.py
#
# imports the XML library and returns a list of Songs


import mlsSong as sng
from pyItunes import *

import config


def ReadLibrary():

    # read library xml file
    l = Library(config.SOURCE_LIBRARYPATH)


    for id,song in l.songs.items():
        # check if song is found; otherwise skip to next entry
        # ...

        # check if song is of one of the file-types as specified in config.py
        # ...

        config.songList.append( sng.Song(song.location, "", song.size/1024, song.name, song.artist, song.total_time/1000, song.rating, song.play_count) )

        # debug: print song title
        #print( song.artist + " - " + song.name )




def SongListSort():
    # sort the song list:
        # 1. by play count, descending
    config.songList.sort(key=lambda song: song.trackPlayCount, reverse=1)

        # 2. by rating, descending
    config.songList.sort(key=lambda song: song.trackRating, reverse=1)

    # space to implement other (better) sorting algorithms...
    # i.e. copy all songs in a given playlist file first
    # ...
    # ...

    return