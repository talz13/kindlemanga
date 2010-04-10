# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 17 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

toolAddID = 1000
toolRemoveID = 1001
toolProcessID = 1002

###########################################################################
## Class KindleMangaFrame
###########################################################################

class KindleMangaFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"KindleManga", pos = wx.DefaultPosition, size = wx.Size( 700,540 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem_open = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"&Open"+ u"\t" + u"Ctrl + O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem_open )
		
		self.m_menubar1.Append( self.m_menu1, u"&File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Output Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer3.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl_outDir = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl_outDir, 0, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 5 )
		
		self.m_button_outDir = wx.Button( self.m_panel2, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button_outDir, 0, wx.ALL, 5 )
		
		bSizer6.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		self.m_listCtrl1 = wx.ListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES )
		bSizer6.Add( self.m_listCtrl1, 1, wx.EXPAND, 5 )
		
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_EXTENDED|wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		self.m_listBox1.Enable( False )
		self.m_listBox1.Hide()
		
		bSizer6.Add( self.m_listBox1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText41 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Archive Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		fgSizer4.Add( self.m_staticText41, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText_archiveName = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_archiveName.Wrap( -1 )
		fgSizer4.Add( self.m_staticText_archiveName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Series:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer4.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl_series = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl_series.SetMaxLength( 100 ) 
		fgSizer4.Add( self.m_textCtrl_series, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Volume / Chapter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl_volume = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl_volume.SetMaxLength( 10 ) 
		fgSizer4.Add( self.m_textCtrl_volume, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		sbSizer2.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		bSizer6.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		self.m_textCtrl_console = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer6.Add( self.m_textCtrl_console, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		self.m_panel2.SetSizer( fgSizer1 )
		self.m_panel2.Layout()
		fgSizer1.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolBar1.AddLabelTool( toolAddID, wx.EmptyString, wx.Bitmap( u"gui/add.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Add files to list", wx.EmptyString ) 
		self.m_toolBar1.AddLabelTool( toolRemoveID, wx.EmptyString, wx.Bitmap( u"gui/remove.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Remove files from list", wx.EmptyString ) 
		self.m_toolBar1.AddLabelTool( toolProcessID, wx.EmptyString, wx.Bitmap( u"gui/process.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Process files", wx.EmptyString ) 
		self.m_toolBar1.Realize()
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnOpen, id = self.m_menuItem_open.GetId() )
		self.m_textCtrl_outDir.Bind( wx.EVT_TEXT, self.OnOutDir )
		self.m_button_outDir.Bind( wx.EVT_BUTTON, self.OnOutDirButton )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnSelectCtrlJob )
		self.m_listBox1.Bind( wx.EVT_LISTBOX, self.OnSelectJob2 )
		self.m_textCtrl_series.Bind( wx.EVT_TEXT, self.OnTextSeries )
		self.m_textCtrl_volume.Bind( wx.EVT_TEXT, self.OnTextVolume )
		self.Bind( wx.EVT_TOOL, self.OnOpen, id = toolAddID )
		self.Bind( wx.EVT_TOOL, self.OnRemove, id = toolRemoveID )
		self.Bind( wx.EVT_TOOL, self.OnProcess, id = toolProcessID )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOpen( self, event ):
		event.Skip()
	
	def OnOutDir( self, event ):
		event.Skip()
	
	def OnOutDirButton( self, event ):
		event.Skip()
	
	def OnSelectCtrlJob( self, event ):
		event.Skip()
	
	def OnSelectJob2( self, event ):
		event.Skip()
	
	def OnTextSeries( self, event ):
		event.Skip()
	
	def OnTextVolume( self, event ):
		event.Skip()
	
	
	def OnRemove( self, event ):
		event.Skip()
	
	def OnProcess( self, event ):
		event.Skip()
	

###########################################################################
## Class dialog_dir_not_found
###########################################################################

class dialog_dir_not_found ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Directory not found...", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Output directory not found.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Do you want to create it?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_button_dir_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button_dir_ok, 0, wx.ALL, 5 )
		
		self.m_button_dir_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button_dir_cancel, 0, wx.ALL, 5 )
		
		bSizer4.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

