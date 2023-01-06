# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class libraryWindow
###########################################################################

class libraryWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Library - MINEATORY", pos = wx.DefaultPosition, size = wx.Size( 775,473 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.panel_mainTagPage = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel_mainTagPage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		self.panel_library = wx.Panel( self.panel_mainTagPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_library.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( self.panel_library, wx.ID_ANY, u"Welcome to Library!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer9.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.panel_library, wx.ID_ANY, u"Your other songs and recently played will display at here! Start your free music journey from here!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		bSizer9.Add( self.m_staticText19, 0, wx.ALL, 5 )

		list_libraryListChoices = []
		self.list_libraryList = wx.ListBox( self.panel_library, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), list_libraryListChoices, 0 )
		self.list_libraryList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		bSizer9.Add( self.list_libraryList, 1, wx.ALL|wx.EXPAND, 5 )

		listProcessHandler1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.btn_addFileFromLocalLib = wx.Button( self.panel_library, wx.ID_ANY, u"Add a song from local", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_addFileFromLocalLib.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		listProcessHandler1.Add( self.btn_addFileFromLocalLib, 0, wx.ALL, 5 )

		self.btn_addFileFromLibLib = wx.Button( self.panel_library, wx.ID_ANY, u"Add a file from library", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_addFileFromLibLib.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		listProcessHandler1.Add( self.btn_addFileFromLibLib, 0, wx.ALL, 5 )

		self.btn_deleteSongLib = wx.Button( self.panel_library, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_deleteSongLib.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		listProcessHandler1.Add( self.btn_deleteSongLib, 0, wx.ALL, 5 )

		self.btn_addToQueneLib = wx.Button( self.panel_library, wx.ID_ANY, u"Add to Quene", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_addToQueneLib.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		listProcessHandler1.Add( self.btn_addToQueneLib, 0, wx.ALL, 5 )

		self.btn_addAllToQuene = wx.Button( self.panel_library, wx.ID_ANY, u"Play all", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_addAllToQuene.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		listProcessHandler1.Add( self.btn_addAllToQuene, 0, wx.ALL, 5 )


		bSizer9.Add( listProcessHandler1, 0, wx.EXPAND, 5 )


		self.panel_library.SetSizer( bSizer9 )
		self.panel_library.Layout()
		bSizer9.Fit( self.panel_library )
		self.panel_mainTagPage.AddPage( self.panel_library, u"a page", False )
		self.panel_playlist = wx.Panel( self.panel_mainTagPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter1 = wx.SplitterWindow( self.panel_playlist, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

		self.m_panel3 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Select a playlist or create a new one", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer7.Add( self.m_staticText12, 0, wx.ALL, 5 )

		list_playListUniteChoices = []
		self.list_playListUnite = wx.ListBox( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_playListUniteChoices, 0 )
		bSizer7.Add( self.list_playListUnite, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_create = wx.Button( self.m_panel3, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.btn_create, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_deletePlaylist = wx.Button( self.m_panel3, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.btn_deletePlaylist, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( gSizer4, 0, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer7 )
		self.m_panel3.Layout()
		bSizer7.Fit( self.m_panel3 )
		self.m_panel4 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.label_targetPlaylistName = wx.StaticText( self.m_panel4, wx.ID_ANY, u"YOUR PLAYLIST NAME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_targetPlaylistName.Wrap( -1 )

		bSizer8.Add( self.label_targetPlaylistName, 0, wx.ALL, 5 )

		self.btn_playThisPlaylist = wx.Button( self.m_panel4, wx.ID_ANY, u"Play this playlist in player", wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		bSizer8.Add( self.btn_playThisPlaylist, 0, wx.ALL, 5 )

		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
		bSizer8.Add( self.m_listBox3, 1, wx.ALL|wx.EXPAND, 5 )

		listProcessHandler = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.btn_addFileFromLocal = wx.Button( self.m_panel4, wx.ID_ANY, u"Add a song from local", wx.DefaultPosition, wx.DefaultSize, 0 )
		listProcessHandler.Add( self.btn_addFileFromLocal, 0, wx.ALL, 5 )

		self.btn_addFileFromLib = wx.Button( self.m_panel4, wx.ID_ANY, u"Add a file from library", wx.DefaultPosition, wx.DefaultSize, 0 )
		listProcessHandler.Add( self.btn_addFileFromLib, 0, wx.ALL, 5 )

		self.btn_deleteSong = wx.Button( self.m_panel4, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		listProcessHandler.Add( self.btn_deleteSong, 0, wx.ALL, 5 )

		self.btn_addToQuene = wx.Button( self.m_panel4, wx.ID_ANY, u"Add to Quene", wx.DefaultPosition, wx.DefaultSize, 0 )
		listProcessHandler.Add( self.btn_addToQuene, 0, wx.ALL, 5 )


		bSizer8.Add( listProcessHandler, 0, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer8 )
		self.m_panel4.Layout()
		bSizer8.Fit( self.m_panel4 )
		self.m_splitter1.SplitVertically( self.m_panel3, self.m_panel4, 0 )
		bSizer5.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


		self.panel_playlist.SetSizer( bSizer5 )
		self.panel_playlist.Layout()
		bSizer5.Fit( self.panel_playlist )
		self.panel_mainTagPage.AddPage( self.panel_playlist, u"a page", False )
		self.panel_download = wx.Panel( self.panel_mainTagPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.downloadTitle = wx.StaticText( self.panel_download, wx.ID_ANY, u"All your downloaded songs on this machine will show up at here", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.downloadTitle.Wrap( -1 )

		bSizer91.Add( self.downloadTitle, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self.panel_download, wx.ID_ANY, u"Normally, all your songs firstly will download to cache automaticall except you upload from local or download source", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer91.Add( self.m_staticText17, 0, wx.ALL, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.btn_download_playAll = wx.Button( self.panel_download, wx.ID_ANY, u"Play all in player", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.btn_download_playAll, 0, wx.ALL, 5 )

		self.btn_download_openDownloadManager = wx.Button( self.panel_download, wx.ID_ANY, u"Open Download Manager", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.btn_download_openDownloadManager, 0, wx.ALL, 5 )

		self.btn_download_addSongs = wx.Button( self.panel_download, wx.ID_ANY, u"Add new songs to download", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.btn_download_addSongs, 0, wx.ALL, 5 )

		self.btn_download_deleteSong = wx.Button( self.panel_download, wx.ID_ANY, u"Delete selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.btn_download_deleteSong, 0, wx.ALL, 5 )


		bSizer91.Add( wSizer4, 0, 0, 5 )

		list_downloadSongsDisplayChoices = []
		self.list_downloadSongsDisplay = wx.ListBox( self.panel_download, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_downloadSongsDisplayChoices, 0 )
		bSizer91.Add( self.list_downloadSongsDisplay, 1, wx.ALL|wx.EXPAND, 5 )


		self.panel_download.SetSizer( bSizer91 )
		self.panel_download.Layout()
		bSizer91.Fit( self.panel_download )
		self.panel_mainTagPage.AddPage( self.panel_download, u"a page", False )
		self.panel_source = wx.Panel( self.panel_mainTagPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		searchBar = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_textCtrl2 = wx.TextCtrl( self.panel_source, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 650,30 ), 0 )
		searchBar.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.btn_source_search = wx.Button( self.panel_source, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		searchBar.Add( self.btn_source_search, 0, wx.ALL, 5 )


		bSizer10.Add( searchBar, 0, wx.EXPAND, 5 )

		list_source_onlineSourceListChoices = []
		self.list_source_onlineSourceList = wx.ListBox( self.panel_source, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_source_onlineSourceListChoices, 0 )
		bSizer10.Add( self.list_source_onlineSourceList, 1, wx.ALL|wx.EXPAND, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.btn_source_playSelected = wx.Button( self.panel_source, wx.ID_ANY, u"Play Selected Song", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.btn_source_playSelected, 0, wx.ALL, 5 )

		self.btn_source_addToQuene = wx.Button( self.panel_source, wx.ID_ANY, u"Add Selected Song to Quene", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.btn_source_addToQuene, 0, wx.ALL, 5 )

		self.btn_source_downloadSelected = wx.Button( self.panel_source, wx.ID_ANY, u"Download Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.btn_source_downloadSelected, 0, wx.ALL, 5 )


		bSizer10.Add( wSizer6, 0, wx.EXPAND, 5 )


		self.panel_source.SetSizer( bSizer10 )
		self.panel_source.Layout()
		bSizer10.Fit( self.panel_source )
		self.panel_mainTagPage.AddPage( self.panel_source, u"a page", True )

		bSizer4.Add( self.panel_mainTagPage, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menu_file_close = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Close Media Library", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_close )

		self.menu_file_preference = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_preference )

		self.menu_file_openPLayer = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open Player", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_openPLayer )

		self.menu_file.AppendSeparator()

		self.menu_file_about = wx.MenuItem( self.menu_file, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_about )

		self.m_menubar2.Append( self.menu_file, u"File" )

		self.menu_source = wx.Menu()
		self.menu_source_add = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Add new songs from Mineatory Server", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_add )

		self.menu_source_checkMySource = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Open my local source", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_checkMySource )

		self.menu_source.AppendSeparator()

		self.menu_source_openLocal = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Upload a local file to source", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_openLocal )

		self.menu_source_checkDownload = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Open Downloads", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_checkDownload )

		self.m_menubar2.Append( self.menu_source, u"Source" )

		self.menu_playlist = wx.Menu()
		self.menu_playlist_openPlaylistPanel = wx.MenuItem( self.menu_playlist, wx.ID_ANY, u"Open Playlist Manager", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_playlist.Append( self.menu_playlist_openPlaylistPanel )

		self.menu_playlist.AppendSeparator()

		self.menu_playlist_create = wx.MenuItem( self.menu_playlist, wx.ID_ANY, u"Create a new Playlist", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_playlist.Append( self.menu_playlist_create )

		self.m_menubar2.Append( self.menu_playlist, u"Playlist" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 0 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )



  
class PageEvent(libraryWindow):
    
    def __init__(self, parent):
        libraryWindow.__init__(self, parent)


if (__name__ == "__main__"):
    app = wx.App(False)
    page = PageEvent(None)
    page.Show(True)
    app.MainLoop()