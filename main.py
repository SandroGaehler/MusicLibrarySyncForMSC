# main.py


import os


from Song import Song
from Playlist import Playlist
from Library import Library, SongListSort



SOURCE_LIBRARYPATH = os.path.expanduser("~") + "\\Desktop\\ml.xml"
SOURCE_PLAYLISTFOLDER = os.path.expanduser("~") + "\\Music\\Playlists"
SOURCE_MUSICFOLDER = os.path.expanduser("~") + "\\Music"
DEST_MUSICFOLDER = "G:\\Music"
DEST_PLAYLISTFOLDER = "G:\\Music\\Playlists"

SPACE = 0.1     # in Gigabytes (1 GB = 1'024 MB = 1'048'576 B)


# File Formats to copy:
MP3 = 1
WMA = 0
OGG = 1
FLAC = 0
MP4 = 0     # AAC a.k.a. .m4a, .m4p, .mp4
OTHERS = 0



def main():


    # read XML file
    Library()

    # sort
    SongListSort()


    # copy as many songs as space available
    usedSpace = 0
    for i in range(songList.__len__()):
        if usedSpace + songList[i].fileSize > SPACE/1048576:
            break
        # copy song i <---
        usedSpace = usedSpace + songList[i].fileSize



    # read existing playlists, write new ones
    Playlist()


    # done
    print("Done!")





if __name__ == '__main__':
    main()