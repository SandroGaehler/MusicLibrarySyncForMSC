#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sandro
#
# Created:     09.02.2014
# Copyright:   (c) Sandro 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

SOURCE_LIBRARYPATH = os.path.expanduser("~") + "\\MusicLibrarySync_Source\\ml50.xml"
SOURCE_PLAYLISTFOLDER = os.path.expanduser("~") + "\\MusicLibrarySync_Source\\Playlists"
SOURCE_MUSICFOLDER = os.path.expanduser("~") + "\\MusicLibrarySync_Source\\Music"
DEST_MUSICFOLDER = os.path.expanduser("~") + "\\MusicLibrarySync_Dest\\Music"
DEST_PLAYLISTFOLDER = os.path.expanduser("~") + "\\MusicLibrarySync_Dest\\Playlists"

SPACE = 0.1     # in Gigabytes (1 GB = 1'024 MB = 1'048'576 B)


# File Formats to copy:
MP3 = 1
WMA = 0
OGG = 1
FLAC = 0
MP4 = 0     # AAC a.k.a. .m4a, .m4p, .mp4
OTHERS = 0


# Playlist conversion Look-Up-Table
PLAYLIST_LUT = [["aaa.m3u8", "rock.m3u8"],
                ["bbb.m3u8", "pop.m3u8"],
                ["www.m3u8", "BestOf.m3u8"]]


# Global variables:
songList = []