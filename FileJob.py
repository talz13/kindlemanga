__author__="Jeff Byrom"
__date__ ="$Apr 2, 2010 8:54:00 AM$"

class FileJob:

    filename = ''
    seriesName = ''
    volume = 0

    def __init__(self, filename):
        self.filename = filename

    def setSeriesName(self, seriesName):
        self.seriesName = seriesName

    def setVolume(self, volume):
        self.volume = int(volume)


    def getFilename(self):
        return self.filename

    def getSeriesName(self):
        return self.seriesName

    def getVolume(self):
        return self.volume