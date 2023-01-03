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
## Class aboutWindow
###########################################################################

class aboutWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About MINEATORY Player", pos = wx.DefaultPosition, size = wx.Size( 393,498 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"pic/music_albums_fill.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"MINEATORY Beta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer3.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"MINEATORY used to be  my daily playlist on lots of platforms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"MINEATORY Player is a project that could provide users a free sound\nfiles player, free music library with the songs in MINEATORY Playlist, and media conversion service.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText6.Wrap( -1 )

		bSizer3.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"MINEATORY WILL NOT provide you the music files and conversion \nservices for illegal purporses. MINEATORY Player will not be responsible\nfor user's illegal usage.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText7.Wrap( -1 )

		bSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Following components were installed on this computer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.label_installedServicesDisplay = wx.StaticText( self, wx.ID_ANY, u"(You don't have services installed yet...)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_installedServicesDisplay.Wrap( -1 )

		bSizer3.Add( self.label_installedServicesDisplay, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.label_versionDisplay = wx.StaticText( self, wx.ID_ANY, u"(Unknown version for this MINEATORY Player)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_versionDisplay.Wrap( -1 )

		bSizer3.Add( self.label_versionDisplay, 0, wx.ALL, 5 )

		self.btn_openGithubRepo = wx.Button( self, wx.ID_ANY, u"Open Github Repository", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btn_openGithubRepo, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.label_installedServicesDisplay.Bind( wx.EVT_ENTER_WINDOW, self.loadInstalledServices )
		self.label_versionDisplay.Bind( wx.EVT_ENTER_WINDOW, self.loadPlayerVersion )
		self.btn_openGithubRepo.Bind( wx.EVT_BUTTON, self.openGithubRepository )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def loadInstalledServices( self, event ):
		event.Skip()

	def loadPlayerVersion( self, event ):
		event.Skip()

	def openGithubRepository( self, event ):
		event.Skip()


import json
import webbrowser
class PageEvent(aboutWindow):
    
    def __init__(self, parent):
        aboutWindow.__init__(self, parent)
        
    def loadJSONConfigData(self, getType:str):
        with open("./config/about.json", "r") as target_json_config_file:
            config_dict:dict = json.load(target_json_config_file)
            
            if (getType == "installed_services"):
                return config_dict["installed_services"]
            elif (getType == "version"):
                return config_dict["version"]
            elif (getType == "song_database_version"):
                return config_dict["song_database_version"]
            else:
                return "UnknownType"
            
    def loadInstalledServices(self, event):
        installed_services = self.loadJSONConfigData("installed_services")
        installed_services_content = ""
        for i in installed_services:
            installed_services_content = installed_services_content + "|" + i
        self.label_installedServicesDisplay.SetLabel(installed_services_content)
        
    def loadPlayerVersion(self, event):
        player_version = self.loadJSONConfigData("version")
        self.label_versionDisplay.SetLabel(player_version)
        
    def openGithubRepository(self, event):
        webbrowser.open("https://github.com/kimsseTheWolf/MineatoryPlayer")
        
        
if (__name__ == "__main__"):
    app = wx.App(False)
    page = PageEvent(None)
    page.Show(True)
    app.MainLoop()