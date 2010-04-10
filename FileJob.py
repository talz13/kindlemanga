__author__="Jeff Byrom"
__date__ ="$Apr 2, 2010 8:54:00 AM$"

import os

class FileJob:

    filename = ''
    seriesName = ''
    volume = ''

    def __init__(self, filename):
        self.filename = filename
        names = os.path.split(filename)
        self.seriesName = names[0][names[0].rindex('\\') + 1:len(names[0])]

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