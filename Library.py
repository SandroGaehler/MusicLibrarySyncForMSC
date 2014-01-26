# Library.py
#
# imports the XML library and returns a list of Songs


from Song import Song

def Library():

    # read library xml file
    # for i in len(library):
    #     getNextTrack(libraryFile)
    #     check if song exists
    #     songList.append(newSong)

    songList = []
    print("bla")



def SongListSort(songList):
    # sort the song list:
        # 1. by play count, descending
    songList.sort(key=lambda song: song.trackPlayCount, reverse=1)

        # 2. by rating, descending
    songList.sort(key=lambda song: song.trackRating, reverse=1)

    # space to implement other (better) sorting algorithms...
    # ...
    # ...

    return songList