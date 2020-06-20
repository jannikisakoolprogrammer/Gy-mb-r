import tkinter
import tkinter.ttk

from code.constants.Root import ConstantsRoot as CONSTANTSROOT


class ViewRoot(tkinter.Frame):
	def __init__(self,
		_master):
		super().__init__(_master)
		
		# Init instance members used throughout the entire class with a default
		# value.
		self.master = None
		
		
		# Menu
		self.tkinter_menu = None
		self.tkinter_menu_file = None
		
		# Frames
		self.tkinter_frame = None
		
		# Master
		self.master = _master		
		self.master.geometry("400x400")			
		
		# Menü
		self.tk_menu_create()
		
		# Ablakok
		self.tk_frame_create()
		
		self.configure_columns()
		#self.configure_rows()
		
		# Pack all controls.
		self.pack(
			expand = True,
			fill = tkinter.BOTH)
	
	
	def tk_menu_create(self):
		# Elöszőr előállítom a gyökér menüt.
		# Minden másik menük összekötik vele.
		self.tkinter_menu = tkinter.Menu(self.master)
		self.master.config(menu = self.tkinter_menu)
		
		# Most a fájl menüt előállítom.
		self.tkinter_menu_file = tkinter.Menu(
			self.tkinter_menu,
			tearoff = 0)
		
		# Az 'Új nyelv' menü gombot a fájl menühoz hozzáfűzöm.
		self.tkinter_menu_file.insert(
			CONSTANTSROOT.NEW_BUTTON,
			"command",
			label = "Új nyelv")
			
		# A 'Nyit nyelv' menü gombot a fájl menühoz hozzáfűzöm.
		self.tkinter_menu_file.insert(
			CONSTANTSROOT.OPEN_BUTTON,
			"command",
			label = "Nyit nyelv")
			
		# A 'Ment' menü gombot a fájl menühoz hozzáfűzöm.
		self.tkinter_menu_file.insert(
			CONSTANTSROOT.EXIT_BUTTON,
			"command",
			label = "Ment")			
			
			
		# A 'fájl' menüt hozzáfűzöm.
		self.tkinter_menu.add_cascade(
			label = "Fájl",
			menu = self.tkinter_menu_file)
	
	
	def tk_frame_create(self):
		self.tk_frame = tkinter.Frame(
			self,
			background = "khaki1")
		self.tk_frame.grid(
			row = 0,
			column = 0,
			sticky = "nsew")
			
		# Szótár
		self.frame_center_button_dictionary = tkinter.Button(
			self.tk_frame,
			text = "Szótár")
		self.frame_center_button_dictionary.pack(
			fill = tkinter.X)
		
		# Egyik ötből
		self.frame_center_button_one_out_of_five = tkinter.Button(
			self.tk_frame,
			text = "Egyik ötből")
		self.frame_center_button_one_out_of_five.pack(
			fill = tkinter.X)
		
		# Egyik a másik után.
		self.tk_frame_buitton_one_after_the_other = tkinter.Button(
			self.tk_frame,
			text = "Egyik a másik után")
		self.tk_frame_buitton_one_after_the_other.pack(
			fill = tkinter.X)
		
		# Gyakorlat teszi a mestért.
		self.tk_frame_button_practice_makes_perfect = tkinter.Button(
			self.tk_frame,
			text = "Gyakorlat teszi a mestért")
		self.tk_frame_button_practice_makes_perfect.pack(
			fill = tkinter.X)				
			
			
	def configure_columns(self):
		self.grid_columnconfigure(0, weight = 1)	
		
		
	def configure_rows(self):	
		self.grid_rowconfigure(0, weight = 10)	