import tkinter
import tkinter.ttk


class ViewRoot(tkinter.Frame):
	def __init__(self,
		_master):
		
		super().__init__(_master)
		
		self.master = _master
		# Maximize window.		
		#self.master.state("zoomed")
		self.master.geometry("800x600")		
		
		
		self.tk_frame_left = None
		self.tk_frame_center = None
		self.tk_frame_left = None
		
		# Construct view.
		self.tk_frame_left_create()
		self.create_frame_center()
		self.create_frame_right()
		
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(1, weight = 8)
		self.grid_columnconfigure(2, weight = 1)	

		self.grid_rowconfigure(0, weight = 10)

		
		# Pack the frames.
		self.pack(
			expand = True,
			fill = tkinter.BOTH)
	
	
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
			
	
	
	def create_frame_center(self):		
	
		self.frame_center = tkinter.Frame(
			self,
			background = "khaki2")
		self.frame_center.grid(
			row = 0,
			column = 1,
			sticky = "nsew")

		
	
	def create_frame_right(self):	
	
		self.frame_right = tkinter.Frame(
			self,
			background = "khaki3")
		self.frame_right.grid(
			row = 0,
			column = 2,
			sticky = "nsew")		
		
		# Add a button.
		self.frame_center_button_new = tkinter.Button(
			self.frame_right,
			text = "Szia")
		self.frame_center_button_new.pack()