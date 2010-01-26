import os
import sys
import Archive
import ProcessImages
import KindleMangaFile

print sys.argv

for arg in sys.argv:
    #arg = 'none'
    #print 'arg: ' + arg
    if (not arg.endswith('kindlemanga.py') and not arg.endswith('kindlemanga')):
        filename = arg
        #filename = 'C:\\pictures2.rar'
        #filename = 'C:\\volume_001.zip'
        #filename = 'C:\\Highschool_of_the_Dead_[XLG]_v3_c10_LQ.zip'
        #filename = 'C:\\Highschool_of_the_Dead_[XLG]_v3_c10_LQ.rar'
        print 'filename: ' + filename

        filepath = os.path.split(filename)
        print 'filepath: ' + str(filepath)
        tempDirName = 'kindleMangaTemp'
        tempDir = os.getenv('APPDATA') + '\\' + tempDirName + '\\'
        os.chdir(tempDir)
        print os.getcwd()
        imageDir = os.path.splitext(filepath[1])[0]
        tempImageDir = raw_input('set imageDir: [' + imageDir + ']: ')
        if (len(tempImageDir) != 0):
            imageDir = tempImageDir


        # height of kindle display - 40 pixel status bar:
        targetHeight = 760
        maxWidth = 600

        # check if tmp directory exists, creat if it does not:
        if (not os.path.isdir(imageDir)):
            os.mkdir(imageDir)

        os.chdir(imageDir)
        print

        archive = Archive.Archive()
        archive.ArchiveFile(filename)

        entries = archive.ReadFiles()
        entries.sort()

        archive.Close()
        #entries = []

        ProcessImages.ProcessAndSave(entries, targetHeight, maxWidth)
        KindleMangaFile.WriteMangaFiles()
print 'done'