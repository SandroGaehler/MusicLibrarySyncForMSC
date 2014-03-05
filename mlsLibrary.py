# Library.py
#
# imports the XML library and returns a list of Songs


import mlsSong as sng
from pyItunes import *
import os

import config


def ReadLibrary():

    # read library xml file
    l = Library(config.SOURCE_LIBRARYPATH)


    for _id,song in l.songs.items():
        # check if song is within SOURCE_MUSICFOLDER
        if song.location == song.location.replace(config.SOURCE_MUSICFOLDER, ''):
            # nothing replaced, wrong location!
            print "ERROR: Song", song.location, "is not within", config.SOURCE_MUSICFOLDER
        # ... song.location, config.SOURCE_MUSICFOLDER
        #  TO DO

        # check if song is found; otherwise skip to next entry
        if not os.path.exists(song.location):
            print "song not found:", song.location
            continue
##        else:
##            print "song found:", song.location

        # check if song is of one of the file-types as specified in config.py
        fileName, fileExtension = os.path.splitext(song.location)
        doCopy = 0
        if fileExtension.lower()==".mp3" and config.MP3:
            doCopy = 1
        elif fileExtension.lower()==".wma" and config.WMA:
            doCopy = 1
        elif fileExtension.lower()==".ogg" and config.OGG:
            doCopy = 1
        elif fileExtension.lower()==".flac" and config.FLAC:
            doCopy = 1
        elif fileExtension.lower()==".mp4" and config.MP4:
            doCopy = 1
        elif fileExtension.lower()==".m4a" and config.MP4:
            doCopy = 1
        elif fileExtension.lower()==".m4p" and config.MP4:
            doCopy = 1
        elif config.OTHERS:
            doCopy = 1

        # wrong file extension: continue with next song
        if doCopy == 0:
            continue

        config.songList.append( sng.Song(song.location, "", song.size/1024, song.name, song.artist, song.total_time/1000, song.rating, song.play_count) )
        config.songList[-1].fileNameNew = config.songList[-1].fileNameOld.replace(config.SOURCE_MUSICFOLDER, config.DEST_MUSICFOLDER)

        # debug: print song title
##        print _id,
##        #print song.artist # program always hangs here, reason unknown!!!
##        print "-",
##        print song.name

    print len(config.songList), "Songs found in iTunes Library\n\n"

    return




def SongListSort():
    # sort the song list:
        # 1. by play count, descending
    config.songList.sort(key=lambda song: song.trackPlayCount, reverse=1)

        # 2. by rating, descending
    config.songList.sort(key=lambda song: song.trackRating, reverse=1)

    # space to implement other (better) sorting algorithms...
    # i.e. copy all songs in a given playlist file first
    # ...
    # ... TO DO

    print "Songlist sorted\n"

    return




