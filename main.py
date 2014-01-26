# main.py


import os


from Song import Song
from Playlist import Playlist
from Library import Library, SongListSort



LIBRARYPATH = "C:\Users\RalpH\Desktom"

def main():


    # read XML file
    Library()

    # sort
    SongListSort()


    # copy as many songs as space available



    # read existing playlists, write new ones
    Playlist()


    # done
    print("Done!")





if __name__ == '__main__':
    main()