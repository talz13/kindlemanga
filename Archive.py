# To change this template, choose Tools | Templates
# and open the template in the editor.

#__author__="b010396"
#__date__ ="$Jan 20, 2010 12:54:44 PM$"

import zipfile
import UnRAR2
import os
import StringIO
import FileObject

maxDepth = 3
imageExtensions = ['.jpg', '.jpeg', '.gif', '.png']

class Archive:
    fileList = None
    filename = None
    ext = None
    arc = None
    tmpPath = None
    
    #def __init__(self):
    #    print''

    def ArchiveFile(self, filename):
        self.filename = filename
        self.ext = os.path.splitext(filename)[1]
        if (self.ext == '.zip'):
            self.arc = zipfile.ZipFile(filename, 'r')
        elif (self.ext == '.rar'):
            self.arc = UnRAR2.RarFile(filename)
    def Close(self):
        self.arc.close()
    
    def SetTmpPath(self, tmpPath):
        self.tmpPath = tmpPath

    def CheckImageExtension(self, filename):
        validExtension = False
        #print filename
        #print os.path.splitext(filename)[1].lower()
        #print imageExtensions
        if (os.path.splitext(filename)[1].lower() in imageExtensions):
            validExtension = True
        return validExtension
    
    def ReadZipFiles(self, archive, depth):
        infolist = archive.infolist()
        files = []
        if (depth > maxDepth):
            print "Abandoning, zip files nested too deep..."
        else:
            for info in infolist:
                if (os.path.splitext(info.filename)[1].lower() == '.zip'):
                    nestedArchive = zipfile.ZipFile(StringIO.StringIO(archive.open(info).read()), 'r')
                    #tmpFiles = self.ReadZipFiles(nestedArchive, depth + 1)
                    files += self.ReadZipFiles(nestedArchive, depth + 1)
                elif (os.path.splitext(info.filename)[1] == '.rar'):
                    nestedArchive = UnRAR2.RarFile(StringIO.StringIO(archive.open(info).read()), 'r')
                    files += self.ReadRarFiles(nestedArchive, depth + 1)
                else:
                    if (self.CheckImageExtension(info.filename)):
                        file = FileObject.FileObject(info.filename, archive.open(info).read(), info.file_size, info.date_time)
                        files.append(file)
            return files
    def ReadRarFiles(self, archive, depth):
        files = []
        if (depth > maxDepth):
            print "Abandoning, rar files nested too deep..."
        else:
            extracts = archive.read_files()
            for file in extracts:
                if (os.path.splitext(file[0].filename)[1].lower() == '.zip'):
                    nestedArchive = UnRAR2.RarFile(StringIO.StringIO(file[1]))
                    files += self.ReadZipFiles(nestedArchive, depth + 1)
                elif (os.path.splitext(file[0].filename)[1].lower() == '.rar'):
                    nestedArchive = UnRAR2.RarFile(StringIO.StringIO(file[1]))
                    files += self.ReadRarFiles(nestedArchive, depth + 1)
                else:
                    if (self.CheckImageExtension(file[0].filename)):
                        file = FileObject.FileObject(file[0].filename, file[1], file[0].size, file[0].datetime[0:6])
                        files.append(file)
            return files
    
    def ReadFiles(self):
        files = []
        if (self.ext == '.zip'):
            files = self.ReadZipFiles(self.arc, 0)
        #for file in files:
        #    print file
        #    print file.filename
        if (self.ext == '.rar'):
            files = self.ReadRarFiles(self.arc, 0)
        return files
