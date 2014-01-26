# Song.py
#
# This class provides features used by songs. The temporary database is a list of Song objects

class Song():
    fileName = ""
    filePath = ""

    trackTitle = ""
    trackArtist = ""
    trackLength = 0     # seconds
    trackRating = 0
    trackPlayCount = 0

    added = 0


    def __init__(self, fileName, filePath, title, artist, length, rating, playCount):
        self.fileName = fileName
        self.filePath = filePath
        self.trackTitle = title
        self.trackArtist = artist
        self.trackLength = length
        self.trackRating = rating
        self.trackPlayCount = playCount

