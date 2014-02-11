# Playlist.py
#
# reads all available playlists, adjusts song paths, removes not copied songs,
# writes resulting playlist to destination



import mlsSong as sng
import config

import glob
import os
import sys


def Playlist():

    # get a list of all playlists
    playlists = glob.glob(config.SOURCE_PLAYLISTFOLDER + "\\*.m3u*")

    # Winamp fail: playlists are saved with pretty random-looking names.
    # Look up the new names in a look-up file. Playlists that are not found
    # won't be copied.
    for playlist in playlists:
        for lutPlaylist in config.PLAYLIST_LUT:
##            print playlist
##            print config.SOURCE_PLAYLISTFOLDER + "\\" + lutPlaylist[0]
            if config.SOURCE_PLAYLISTFOLDER + "\\" + lutPlaylist[0] == playlist:
                currentPlaylist = lutPlaylist[1]
                print "Playlist name conversion: from", playlist, "to", currentPlaylist
                break

        # "s" as in Source_playlist
        # -------------------------
        # open source playlist
        try:
            s = open(playlist, 'r')
        except:
            print "Playlist", playlist, "could not be read!"

        # "d" as in Destination_playlist
        # ------------------------------
        # check if destination playlist file already exists
        try:
            d = open(config.DEST_PLAYLISTFOLDER + "\\" + currentPlaylist, 'r')
        except:
            # file does not exist, create it
            #d.close()   # ??
            d = open(config.DEST_PLAYLISTFOLDER + "\\" + currentPlaylist, 'w')
        else:
            # file already exists, delete it and create a new one
            d.close()
            os.remove(config.DEST_PLAYLISTFOLDER + "\\" + currentPlaylist)
            d = open(config.DEST_PLAYLISTFOLDER + "\\" + currentPlaylist, 'w')
        # write header line
        d.write("#EXTM3U\n")

        # read first line, it should be '#EXTM3U'
        b = s.readline()
        print b
        if b == '#EXTM3U':
            print "EXTM3U playlist."
            extm3u = True
        else:
            extm3u = False
            # I'm pretty sure b is already the first song, so don't read another
            # line before properly processing it
            skipFirst = True

        for lines in s:
            if extm3u:
                a = s.readline()    # 'EXTINF:' song.trackLength,Artist - Title
                                    # This line can be left unchanged.

            if not skipFirst:
                b = s.readline()    # file path: strip SOURCE_MUSICFOLDER, replace it with DEST_MUSICFOLDER
            else:
                skipFirst = False

            # process b:
            #  - if b is a relative path, convert it to absolute
            # ... TO DO

            #  - find song, where config.songList[x].fileNameOld = b
            # ... TO DO

            #  - if config.songList[x].added == 0: continue (song was not copied; don't add it to playlist)
            # ... TO DO

            # write new path to b
            b = config.songList[x].fileNameNew + "\n"

            if not extm3u:
                # create line a
                a = "EXTINF:" + config.songList[x].trackLength + ","
                a = a + config.songList[x].trackArtist + " - "
                a = a + config.songList[x].trackTitle + "\n"
            d.write(a)
            d.write(b)

        s.close()
        d.close()









