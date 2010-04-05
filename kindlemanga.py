__author__="Jeff Byrom"
__date__ ="$Jan 20, 2010 12:54:44 PM$"

import os
import sys
import wx
import Archive
import FileJob
import ProcessImages
import KindleMangaFile
import KindleMangaLayout

class MainFrame(KindleMangaLayout.KindleMangaFrame):

    fileList = []
    outDir = ''

    def __init__(self, parent):
        KindleMangaLayout.KindleMangaFrame.__init__(self, parent)
        sys.stdout = self.m_textCtrl_console
        sys.stderr = self.m_textCtrl_console
        
        self.m_textCtrl_outDir.SetValue(os.getenv('USERPROFILE') + '\\My Documents')

    def OnOpen(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose file(s) to add to list", self.dirname, '', 'Rar, zip files (*.rar;*.zip)|*.rar;*.zip', wx.FLP_CHANGE_DIR|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            print os.getcwd()
            self.filenames = dlg.GetFilenames()
            self.dirname = dlg.GetDirectory() + '\\'
            #print self.dirname
            #print self.filenames
            for index, filename in enumerate(self.filenames):
                tempFilename = self.dirname + filename
                if tempFilename.find('\\\\') > 0:
                    tempFilename = tempFilename.replace('\\\\','\\')
                self.filenames[index] = tempFilename
                # filename, data, size, datetime, dir=None
                self.fileList.append(FileJob.FileJob(tempFilename))
            print self.filenames
            self.m_listBox1.InsertItems(self.filenames, self.m_listBox1.GetCount())
        dlg.Destroy()
        return [self.dirname, self.filenames]

    def OnRemove(self, event):
        self.selections = self.m_listBox1.GetSelections()
        print self.selections
        for index in self.selections:
            del self.fileList[index]
            self.m_listBox1.Delete(index)

    def OnProcess(self, event):
        self.ProcessAll(self.fileList, self.m_textCtrl_outDir.GetValue())

    def OnTextSeries(self, event):
        #print "OnTextSeries"
        selected = self.m_listBox1.GetSelections()
        if len(selected) == 1:
            index = selected[0]
            self.fileList[index].setSeriesName(self.m_textCtrl_series.GetValue())
            #print self.fileList[index].getSeriesName()
    
    def OnTextVolume(self, event):
        selected = self.m_listBox1.GetSelections()
        if len(selected) == 1:
            index = selected[0]
            if (self.m_textCtrl_volume.GetValue().isdigit()):
                self.fileList[index].setVolume(self.m_textCtrl_volume.GetValue())
            #print self.fileList[index].getVolume()

    def OnOutDir(self, event):
        self.outDir = self.m_textCtrl_outDir.GetValue()

    def OnOutDirButton(self, event):
        self.dirname = ''
        if self.m_textCtrl_outDir.GetValue() != '':
            self.dirname = self.m_textCtrl_outDir.GetValue()
        else:
            self.dirname = os.getcwd()

        print "Opening dir: " + self.dirname
        dlg = wx.DirDialog(self, "Choose directory to create output files", self.dirname)
        if dlg.ShowModal() == wx.ID_OK:
            print os.getcwd()
            self.dirname = dlg.GetPath()
            print self.dirname
            self.m_textCtrl_outDir.SetValue(self.dirname)
        dlg.Destroy()

    def OnSelectJob(self, event):
        selected = self.m_listBox1.GetSelections()
        if len(selected) == 1:
            index = selected[0]
            self.m_textCtrl_series.SetValue(self.fileList[index].getSeriesName())
            self.m_textCtrl_volume.SetValue(str(self.fileList[index].getVolume()))

    def ProcessAll(self, fileJobList, outDir):
        unknownVol = 0;
        for job in fileJobList:
            filename = job.getFilename()
            print 'filename: ' + filename

            filepath = os.path.split(filename)
            print 'filepath: ' + str(filepath)
            volume = job.getVolume()
            if (job.getSeriesName() != ''):
                seriesName = job.getSeriesName()
            else:
                seriesName = 'Unknown'
                unknownVol += 1
                volume = unknownVol
            if (outDir != ''):
                tempDirName = outDir
            else:
                tempDirName = os.getenv('APPDATA') + '\\' + 'kindleMangaTemp'

            tempDir = tempDirName + '\\' # + seriesName
            print tempDir
            os.chdir(tempDir)
            print os.getcwd()
            #if job.getSeriesName().len > 0:
            #
            #imageDir = os.path.splitext(filepath[1])[0]
            #tempImageDir = raw_input('set imageDir: [' + imageDir + ']: ')
            tempImageDir = seriesName + '_' + ('%03d' % volume)
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

            ProcessImages.ProcessAndSave(entries, targetHeight, maxWidth)
            KindleMangaFile.WriteMangaFiles()
        print 'done'

    def printBox(self, text):
        self.m_textCtrl_console.AppendText(text)

class Gui(wx.App):
    def OnInit(self):
        self.m_frame = MainFrame(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

    

print 'starting gui...'
app = Gui(0)
app.MainLoop()