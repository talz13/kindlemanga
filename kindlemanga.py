import os
import sys
import wx
import Archive
import FileObject
import FileJob
import ProcessImages
import KindleMangaFile
import KindleMangaLayout
#import wx.lib.filebrowsebutton

#app = wx.App(False)
#frame = MainWindow(None, "Sample editor")
#app.MainLoop()


class MainFrame(KindleMangaLayout.KindleMangaFrame):

    fileList = []
    outDir = ''

    #class newOutput:
    #    #wxTextCtrl_display = None
    #    #
    #    #def __init__(self, wxTextCtrl_display):
    #    #    self.wxTextCtrl_display = wxTextCtrl_display
    #    #
    #    def write(self, string):
    #        self.m_textCtrl_console.AppendText(text)
    #out = newOutput
    #sys.stdout = newOutput()

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
            #arg = 'none'
            #print 'arg: ' + arg
            #if (not job.endswith('kindlemanga.py') and not job.endswith('kindlemanga')):
            filename = job.getFilename()
            #filename = 'C:\\pictures2.rar'
            #filename = 'C:\\volume_001.zip'
            #filename = 'C:\\Highschool_of_the_Dead_[XLG]_v3_c10_LQ.zip'
            #filename = 'C:\\Highschool_of_the_Dead_[XLG]_v3_c10_LQ.rar'
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
                #tempDirName = 'kindleMangaTemp'
                tempDirName = os.getenv('APPDATA') + '\\' + 'kindleMangaTemp'

            #tempDir = os.getenv('APPDATA') + '\\' + tempDirName + '\\'
            tempDir = tempDirName + '\\' # + seriesName + '_' + ('%03d' % volume)
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


class newOutput:
    wxTextCtrl_display = None

    def __init__(self, wxTextCtrl_display):
        self.wxTextCtrl_display = wxTextCtrl_display

    def write(self, string):
        self.wxTextCtrl_display.AppendText(text)

#class MainWindow(wx.Frame):
#    def __init__(self, parent, title):
#        wx.Frame.__init__(self, parent, title = title, size = (200,200))
#        #self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
#        self.CreateStatusBar()
#
#        filemenu = wx.Menu()
#        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file")
#        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
#        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")
#
#        menuBar = wx.MenuBar()
#        menuBar.Append(filemenu, "&File")
#        self.SetMenuBar(menuBar)
#
#        # panel to hold selector box:
#        selectorPanel = wx.Panel(self)
#        box1 = wx.BoxSizer(wx.VERTICAL)
#
#        box1Text = wx.StaticText(selectorPanel, -1, "Choose your file")
#        box1Text.SetSize(box1Text.GetBestSize())
#        box1.Add(box1Text, 0, wx.ALL, 10)
#
#        fileBrowseButton = wx.lib.filebrowsebutton.FileBrowseButton(selectorPanel, labelText='Select a manga archive:', fileMask='*.rar;*.zip')
#
#        selectorPanel.SetSizer(box1)
#        selectorPanel.Layout()
#
#        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
#        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
#        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
#
#        self.Show(True)
#
#    def OnOpen(self, e):
#        self.dirname = ''
#        dlg = wx.FileDialog(self, "Choose a file", self.dirname, '', 'Rar, zip files (*.rar;*.zip)|*.rar;*.zip', wx.OPEN)
#        if dlg.ShowModal() == wx.ID_OK:
#            self.filename = dlg.GetFilename()
#            self.dirname = dlg.GetDirectory()
#            f = open(os.path.join(self.dirname, self.filename), 'r')
#            self.control.SetValue(f.read())
#            f.close()
#        dlg.Destroy()
#
#    def OnAbout(self, e):
#        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
#        dlg.ShowModal()
#        dlg.Destroy()
#
#    def OnExit(self, e):
#        self.Close(True)