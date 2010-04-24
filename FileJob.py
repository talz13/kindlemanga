__author__="Jeff Byrom"
__date__ ="$Apr 2, 2010 8:54:00 AM$"

import os
import re
#from decimal import *

class FileJob:

    filename = ''
    seriesName = ''
    volume = ''
    ch = ''
    myRE = re.compile('\d+')

    def __init__(self, filename):
        self.filename = filename
        names = os.path.split(filename)
        self.seriesName = names[0][names[0].rindex('\\') + 1:len(names[0])]
        #print self.seriesName

        vIndex = 0
        chIndex = 0

       # print names[1]
        try:
            extIndex = names[1].rindex ('.')
            try:
                vIndex = names[1].lower().rindex('v')

                volSection = names[1][vIndex:extIndex]
                #print volSection
                volSearch = self.myRE.search(volSection)
                self.volume = str(int(volSection[volSearch.start():volSearch.end()]))
                #print 'Volume: ', self.volume
            except ValueError:
                self.volume = ''

            try:
                chIndex = names[1].lower().rindex('c')
                #print chIndex
                if (chIndex > vIndex and chIndex < extIndex):
                    chSection = names[1][chIndex:extIndex]
                    #print chSection
                    chSearch = self.myRE.search(chSection)
                    #print 'chSearch = ', chSearch
                    if (chSearch != None):
                        self.ch = str(int(chSection[chSearch.start():chSearch.end()]))
                #self.volume += '.' + ch
                #print 'Chapter: ', self.ch
            except ValueError:
                self.ch = ''
        except ValueError:
            self.volume = ''
            self.ch = ''

    def setSeriesName(self, seriesName):
        self.seriesName = seriesName

    def setVolume(self, volume):
        self.volume = str(int(volume))

    def setChapter(self, chapter):
        self.ch = str(int(chapter))


    def getFilename(self):
        return self.filename

    def getSeriesName(self):
        return self.seriesName

    def getVolume(self):
        return self.volume

    def getChapter(self):
        return self.ch