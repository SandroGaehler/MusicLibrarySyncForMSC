# main.py


import os
import sys


#from Song import Song
import mlsPlaylist as plst
import mlsLibrary as lbr
import mlsSong as sng
import config


# see config.py for hard-coded parameters such as file maths, how much space
# shall be used for the copied files, file formats to copy etc...


def main():
    # check if paths exist
    if not os.path.exists(config.SOURCE_LIBRARYPATH):
        print "Library folder does not exist!"
    if not os.path.exists(config.SOURCE_MUSICFOLDER):
        print "Music folder does not exist!"
    if not os.path.exists(config.SOURCE_PLAYLISTFOLDER):
        print "Playlist folder does not exist!"

    # check if destination music folder exists - otherwise create it
    if not os.path.exists(config.DEST_MUSICFOLDER):
        try:
            os.makedirs(config.DEST_MUSICFOLDER)
        except:
            print "something went wrong creating the destination music folder!"
            sys.exit()

    # check if destination playlist folder exists - otherwise create it
    if not os.path.exists(config.DEST_PLAYLISTFOLDER):
        try:
            os.makedirs(config.DEST_PLAYLISTFOLDER)
        except:
            print "something went wrong creating the destination playlist folder!"
            sys.exit()

    # read iTunes-compatible XML library file with pyitunes
    lbr.ReadLibrary()

    # sort
    lbr.SongListSort()


    # copy as many songs as space available
    usedSpace = 0   # unit: kB = 1024 B
    for i in range(config.songList.__len__()):
        if usedSpace + config.songList[i].fileSize > config.SPACE*1048576:
            break

        # copy song i <---
        # ...
        config.songList[i].added = 1
        usedSpace = usedSpace + config.songList[i].fileSize

        print config.songList[i].trackTitle, "added, used space =", usedSpace



    # read existing playlists, write new ones
    plst.Playlist()


    # done
    print("Done!")





if __name__ == '__main__':
    main()