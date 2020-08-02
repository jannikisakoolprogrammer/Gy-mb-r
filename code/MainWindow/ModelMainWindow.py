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
				"data"),
			encoding = "utf-8")
		
		self.entries = self.f.readlines()
		random.shuffle(self.entries)
		
		self.n_cur_entry = -1
		self.n_len_entries = len(self.entries)
		
		self.correct_guesses = 0
		self.incorrect_guesses = 0

	
	def next_word_pair(self):
	
		self.n_cur_entry += 1
	
		if self.n_cur_entry >= self.n_len_entries:
			self.n_cur_entry = 0
			
			# Randomize again
			random.shuffle(self.entries)
		
		chosen_entry = self.entries[self.n_cur_entry]
		
		self.source_word = chosen_entry.split("-")[1].strip()
		self.target_word = chosen_entry.split("-")[0].strip()
	
	
	def get_number_of_entries(self):
		
		return self.n_len_entries
	
	
	def increment_correct_guesses(self):
		
		self.correct_guesses += 1
	
	
	def increment_incorrect_guesses(self):
		
		self.incorrect_guesses += 1
	
	
	def get_correct_guesses(self):
	
		return self.correct_guesses
	
	
	def get_incorrect_guesses(self):
		
		return self.incorrect_guesses
		
