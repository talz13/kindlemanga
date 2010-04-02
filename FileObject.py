# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Jeff Byrom"
__date__ ="$Jan 21, 2010 9:40:00 AM$"

class FileObject:
    dir = None
    filename = None
    data = None
    size = None
    datetime = None

    def __init__(self, filename, data, size, datetime, dir=None):
        self.filename = filename
        self.data = data
        self.size = size
        self.datetime = datetime
        self.dir = dir


    def __cmp__(self, other):
        return cmp(self.filename, other.filename)

    def PrintInfo(self):
        print self.dir + ',',
        print self.filename + ',',
        print str(self.size) + ',',
        print self.datetime