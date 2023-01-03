# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class playerWindow
###########################################################################

class playerWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MINEATORY PLAYER", pos = wx.DefaultPosition, size = wx.Size( 557,381 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		self.player_menubar = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menu_file_openLibrary = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open Library", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_openLibrary )

		self.menu_file_open = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open a media file...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_open )

		self.menu_file.AppendSeparator()

		self.menu_file_about = wx.MenuItem( self.menu_file, wx.ID_ANY, u"About Mineatory Player...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_about )

		self.menu_file.AppendSeparator()

		self.menu_file_preferences = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_preferences )

		self.menu_file.AppendSeparator()

		self.menu_file_exit = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Exit Mineatory Player...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_exit )

		self.player_menubar.Append( self.menu_file, u"File" )

		self.menu_source = wx.Menu()
		self.menu_source_update = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Update source from Mineatory Server", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_update )

		self.menu_source_clear = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Clear my Source", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_clear )

		self.menu_source.AppendSeparator()

		self.menu_source_download = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Download songs from Mineatory Server", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_download )

		self.menu_source_manager = wx.MenuItem( self.menu_source, wx.ID_ANY, u"Open Source Manager", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_source.Append( self.menu_source_manager )

		self.player_menubar.Append( self.menu_source, u"Source" )

		self.menu_play = wx.Menu()
		self.menu_play_pause = wx.MenuItem( self.menu_play, wx.ID_ANY, u"Pause / Play (Space)", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_play.Append( self.menu_play_pause )

		self.menu_play_end = wx.MenuItem( self.menu_play, wx.ID_ANY, u"End this song", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_play.Append( self.menu_play_end )

		self.menu_play.AppendSeparator()

		self.menu_play_front = wx.MenuItem( self.menu_play, wx.ID_ANY, u"Jump 5 seconds front", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_play.Append( self.menu_play_front )

		self.menu_play_back = wx.MenuItem( self.menu_play, wx.ID_ANY, u"Jump 5 seconds back", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_play.Append( self.menu_play_back )

		self.menu_play.AppendSeparator()

		self.menu_play_info = wx.MenuItem( self.menu_play, wx.ID_ANY, u"Display song info...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_play.Append( self.menu_play_info )

		self.player_menubar.Append( self.menu_play, u"Play" )

		self.SetMenuBar( self.player_menubar )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Playlist", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		list_playListChoices = []
		self.list_playList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_playListChoices, 0 )
		bSizer1.Add( self.list_playList, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_addSong = wx.Button( self, wx.ID_ANY, u"Add songs...", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btn_addSong, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.btn_deleteSong = wx.Button( self, wx.ID_ANY, u"Delete Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btn_deleteSong, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )


		gSizer1.Add( bSizer1, 0, wx.EXPAND, 5 )

		btn_list_add = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"pic/music_albums_fill.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		btn_list_add.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label_songTitle = wx.StaticText( self, wx.ID_ANY, u"Not Playing Right now...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.label_songTitle.Wrap( -1 )

		self.label_songTitle.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		btn_list_add.Add( self.label_songTitle, 0, wx.ALL|wx.EXPAND, 5 )

		self.slider_progressDisplay = wx.Slider( self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		btn_list_add.Add( self.slider_progressDisplay, 0, wx.ALL|wx.EXPAND, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.btn_back = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,50 ), wx.BU_AUTODRAW|0 )

		self.btn_back.SetBitmap( wx.Bitmap( u"pic/angle-double-left (1).bmp", wx.BITMAP_TYPE_ANY ) )
		wSizer1.Add( self.btn_back, 0, wx.ALL, 5 )

		self.btn_play = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,50 ), wx.BU_AUTODRAW|0 )

		self.btn_play.SetBitmap( wx.Bitmap( u"pic/play circle.bmp", wx.BITMAP_TYPE_ANY ) )
		wSizer1.Add( self.btn_play, 0, wx.ALL, 5 )

		self.btn_pause = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,50 ), wx.BU_AUTODRAW|0 )

		self.btn_pause.SetBitmap( wx.Bitmap( u"pic/pause circle.bmp", wx.BITMAP_TYPE_ANY ) )
		wSizer1.Add( self.btn_pause, 0, wx.ALL, 5 )

		self.btn_front = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,50 ), wx.BU_AUTODRAW|0 )

		self.btn_front.SetBitmap( wx.Bitmap( u"pic/angle-double-right.bmp", wx.BITMAP_TYPE_ANY ) )
		wSizer1.Add( self.btn_front, 0, wx.ALL, 5 )


		btn_list_add.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		gSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.slider_volume = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gSizer4.Add( self.slider_volume, 1, wx.ALL|wx.EXPAND, 5 )


		btn_list_add.Add( gSizer4, 0, wx.EXPAND, 5 )


		gSizer1.Add( btn_list_add, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.openAbout, id = self.menu_file_about.GetId() )
		self.btn_addSong.Bind( wx.EVT_BUTTON, self.openMusicFile )
  
	def __del__( self ):
		pass
	
	# Virtual event handlers, override them in your derived class
	def openAbout( self, event ):
		event.Skip()

	def openMusicFile( self, event ):
		event.Skip()

import os
import pydub
from pydub.playback import play
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Player():
    
    def __init__(self):
        self.target_media_file = None # Originally opened file in Python
        self.target_media_file_location = "" # File location in string
        self.target_file_type = "" # Recorded file extension
        self.playing_file = None # File for Pydub
        
    # Basic functions
    def getFileExtension(target_file_location:str):
        extensionName:str = ""
		# For loop into every characters of the string
        fileExtensionStartLocation = target_file_location.find(".")
        extensionName = target_file_location[fileExtensionStartLocation+1:]
        print(extensionName)
        return extensionName
    
    # Non Basic functions
    def openFile(self, file_location:str, uploadToPydub:bool = True):
        "Open the target file in the file location of this class. System will automatically override the current file"
        # Apply the file location
        self.target_media_file_location = file_location
        # Identify the file extenstion
        self.target_file_type = self.getFileExtension(self.target_media_file_location)
        # Open the file and apply to a variable
        self.target_media_file = open(self.target_media_file_location, "rb")
        # Upload the file to Pydub
        if (uploadToPydub == True):
            self.playing_file = pydub.AudioSegment.from_file(self.target_media_file)
        
    def closeFile(self):
        "Close the target file in the class."
        # Close and reset the identities
        self.target_media_file.close()
        self.target_media_file_location = ""
        self.target_file_type = ""
        
    def playMusicFromFile(self):
        "Start the play the music from the file in the class"
        # Open the file with pydub
        play(self.playing_file)


class PageEvent(playerWindow):
    def __init__(self, parent):
        playerWindow.__init__(self, parent)
        self.Player = Player
        
    def openAbout(self, event):
        try:
            os.system("python about.py")
            return
        except:
            os.system("python3 about.py")
            return
        
    def openMusicFile(self, event):
        try:
            fileLocation = filedialog.askopenfilename(filetypes=[("MP3 Media File", "*.mp3"), ("WAV Media File", "*.wav")])
            fileExtention = self.Player.getFileExtension(fileLocation)
            messagebox.showinfo("File type test", fileLocation+"|"+fileExtention)
        except:
            messagebox.showerror("Open file error", "Mineatory cannot open the file that you specific.")

if (__name__ == "__main__"):
    root = Tk()
    root.withdraw()
    app = wx.App(False)
    page = PageEvent(None)
    page.Show(True)
    app.MainLoop()