from code.Base.Model import Model

import random
import os.path


class ModelMainWindow(Model):
	def __init__(
		self,
		_database):
		super(
			ModelMainWindow,
			self).__init__(_database)
			
			
		self.f = open(
			os.path.join(
				"language_files",
				"magyar_german"),
			encoding = "utf-8")
		
		self.entries = self.f.readlines()
		random.shuffle(self.entries)
		
		self.n_cur_entry = -1
		self.n_len_entries = len(self.entries)

	
	def next_word_pair(self):
	
		self.n_cur_entry += 1
	
		if self.n_cur_entry >= self.n_len_entries:
			self.n_cur_entry = 0
		
		chosen_entry = self.entries[self.n_cur_entry]
		
		self.source_word = chosen_entry.split("-")[1].strip()
		self.target_word = chosen_entry.split("-")[0].strip()
		
