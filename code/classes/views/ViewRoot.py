import tkinter
import tkinter.ttk

from code.constants.Root import ConstantsRoot_HUN as CONSTANTSROOT


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
		# Frame left
		self.tkinter_frame_left = None
		
		# Frame center
		self.tkinter_frame_center = None
		
		# Frame right
		self.tkinter_frame_right = None
		
		
		# Master
		self.master = _master		
		self.master.geometry("800x600")			
		# Maximize window.
		self.master.state("zoomed")
		
		# Menü
		self.tk_menu_create()
		
		# Ablakok
		self.tk_frame_left_create()
		self.tk_frame_center_create()
		self.tk_frame_right_create()
		
		self.configure_columns()
		self.configure_rows()
		
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
			
			
		# A 'fájl' menüt hozzáfűzöm.
		self.tkinter_menu.add_cascade(
			label = "Fájl",
			menu = self.tkinter_menu_file)
	
	
	def tk_frame_left_create(self):
		self.tk_frame_left = tkinter.Frame(
			self,
			background = "khaki1")
		self.tk_frame_left.grid(
			row = 0,
			column = 0,
			sticky = "nsew")			
		
		# Új nyelv button.
		self.frame_left_button_new = tkinter.Button(
			self.tk_frame_left,
			text = "Új nyelv")			
		self.frame_left_button_new.pack(
			fill = tkinter.X)
			
		
		# Nyelv nyit button.
		self.frame_left_button_open = tkinter.Button(
			self.tk_frame_left,
			text = "Nyelv nyit")
		self.frame_left_button_open.pack(
			fill = tkinter.X)
		
		# Ment button.
		self.frame_left_button_save = tkinter.Button(
			self.tk_frame_left,
			text = "Ment")
		self.frame_left_button_save.pack(
			fill = tkinter.X)
			
	
	
	def tk_frame_center_create(self):		
		self.frame_center = tkinter.Frame(
			self,
			background = "khaki2")
		self.frame_center.grid(
			row = 0,
			column = 1,
			sticky = "nsew")

		
	
	def tk_frame_right_create(self):	
		self.frame_right = tkinter.Frame(
			self,
			background = "khaki3")
		self.frame_right.grid(
			row = 0,
			column = 2,
			sticky = "nsew")		
		
		# Szótár
		self.frame_center_button_dictionary = tkinter.Button(
			self.frame_right,
			text = "Szótár")
		self.frame_center_button_dictionary.pack(
			fill = tkinter.X)
		
		# Egyik ötből
		self.frame_center_button_one_out_of_five = tkinter.Button(
			self.frame_right,
			text = "Egyik ötből")
		self.frame_center_button_one_out_of_five.pack(
			fill = tkinter.X)
		
		# Egyik a másik után.
		self.frame_right_buitton_one_after_the_other = tkinter.Button(
			self.frame_right,
			text = "Egyik a másik után")
		self.frame_right_buitton_one_after_the_other.pack(
			fill = tkinter.X)
		
		# Gyakorlat teszi a mestért.
		self.frame_right_button_practice_makes_perfect = tkinter.Button(
			self.frame_right,
			text = "Gyakorlat teszi a mestért")
		self.frame_right_button_practice_makes_perfect.pack(
			fill = tkinter.X)
			
			
	def configure_columns(self):
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(1, weight = 8)
		self.grid_columnconfigure(2, weight = 1)	
		
		
	def configure_rows(self):	
		self.grid_rowconfigure(0, weight = 10)	