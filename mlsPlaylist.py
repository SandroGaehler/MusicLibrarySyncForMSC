# Playlist.py
#
# reads all available playlists, adjusts song paths, removes not copied songs, writes resulting playlist to destination



import mlsSong as sng
import config

import glob
import os
import sys


def Playlist():
    # check if playlist folder exists
    # ...
    if not os.path.exists(config.DEST_PLAYLISTFOLDER):
        try:
            os.makedirs(config.DEST_PLAYLISTFOLDER)
        except:
            print "something went wrong creating the destination playlist folder!"
            sys.exit()

    # get a list of all playlists
    playlists = glob.glob(config.SOURCE_PLAYLISTFOLDER + "*.m3u*")

    # Winamp fail: playlists are saved with pretty random-looking names.
    # Look up the new names in a look-up file. Playlists that are not found
    # won't be copied.
    for i in len(playlists):
        for j in len(config.PLAYLIST_LUT):
            if config.PLAYLIST_LUT[j][0] == playlists[i]:
                currentPlaylist = config.PLAYLIST_LUT[j][1]
                # check if file exists
                try:
                    f = open(config.DEST_PLAYLISTFOLDER + currentPlaylist, 'r')
                except:
                    # file does not exist, create it
                    f.close()
                    f.open(config.DEST_PLAYLISTFOLDER + currentPlaylist, 'w')
                break

        # get list of songs in original playlist
        # ...

        # for j in len(listOfSongs):
        #     if song.added:
        #         f.writeline( .... )









