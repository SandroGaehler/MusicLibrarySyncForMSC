# main.py


import os
import sys
import shutil
import unicodedata

#from Song import Song
import mlsPlaylist as plst
import mlsLibrary as lbr
import mlsSong as sng
import config


# see config.py for hard-coded parameters such as file maths, how much space
# shall be used for the copied files, file formats to copy etc...


def main():
    print "Welcome to MusicLibrarySyncForMSC 0.1"

    # check if paths exist
    if not os.path.exists(config.SOURCE_LIBRARYPATH):
        print "ERROR: Library file does not exist!"
        sys.exit()
    if not os.path.exists(config.SOURCE_MUSICFOLDER):
        print "ERROR: Music folder does not exist!"
        sys.exit()
    if not os.path.exists(config.SOURCE_PLAYLISTFOLDER):
        print "ERROR: Playlist folder does not exist!"
        sys.exit()

    # check if destination music and playlist folders exists; otherwise create it
    if not os.path.exists(config.DEST_MUSICFOLDER):
        try:
            os.makedirs(config.DEST_MUSICFOLDER)
        except:
            print "ERROR: something went wrong creating the destination music folder!"
            sys.exit()
    if not os.path.exists(config.DEST_PLAYLISTFOLDER):
        try:
            os.makedirs(config.DEST_PLAYLISTFOLDER)
        except:
            print "ERROR: something went wrong creating the destination playlist folder!"
            sys.exit()

    # read iTunes-compatible XML library file with pyitunes
    print "\nStart reading the Library..."
    lbr.ReadLibrary()

    # sort
    print "\nStart Sorting..."
    lbr.SongListSort()


    # copy as many songs as space available
    print "\nStarted Copying...\n"
    usedSpace = 0   # unit: kB = 1024 B
    for i in range(len(config.songList)):
        if usedSpace + config.songList[i].fileSize > config.SPACE*1048576:
            break

        # check if song i exists already
        if os.path.exists(config.songList[i].fileNameNew):
            print config.songList[i].trackTitle, "already present at destination"

        # if not: copy song i
##        source = unicodedata.normalize('NFKD', config.songList[i].fileNameOld).encode('ascii', 'ignore')
##        dest   = unicodedata.normalize('NFKD', config.songList[i].fileNameNew).encode('ascii', 'ignore')
        dir = os.path.dirname(config.songList[i].fileNameNew)
        if not os.path.exists(dir):
            os.makedirs(dir)
        try:
            shutil.copy2(config.songList[i].fileNameOld, config.songList[i].fileNameNew)
        except:
            print "ERROR: Copying failed:", config.songList[i].trackTitle
            continue
        else:
##            print"success!"
            pass

        config.songList[i].added = 1
        config.songList[i].fileNameNew = config.songList[i].fileNameNew.replace(config.SOURCE_MUSICFOLDER, config.DEST_MUSICFOLDER)
        usedSpace = usedSpace + config.songList[i].fileSize

        # debug:
##        print config.songList[i].trackTitle, "added, used space =", usedSpace

    print i, "Songs copied."


    # additional feature:
    # delete everything that was already there and shouldn't be anymore
    # (TO DO)



    # read existing playlists, write new ones
    plst.Playlist()


    # done
    print("Done!")





if __name__ == '__main__':
    main()