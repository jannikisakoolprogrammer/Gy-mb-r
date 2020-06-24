import sqlite3
import datetime

from code import database_settings
from code import default_system_settings


class Database(object):
	
	def __init__(self):
	
		# A tárgy az adatbázis kapcsolatnak.
		self.connection = None
		
		# A tárgy a cursornak.
		self.cursor = None
		
		# Itt, az adatbázist és a táblázatot előállítom.
		self.connection = sqlite3.connect(database_settings.DATABASE_FILEPATH)		
		self.init_system_settings_table()
		self.init_table_language_mapping()
		self.init_table_word_mapping()
		
		self.cursor = self.connection.cursor()
		
		if not self.default_system_settings_exist():
			self.write_default_system_settings()
	
	
	def init_system_settings_table(self):
		self.connection.execute(database_settings.TABLE_SYSTEM_SETTINGS_CREATE)
		
		
	def init_table_language_mapping(self):
		self.connection.execute(database_settings.TABLE_LANGUAGE_MAPPING_CREATE)
	
	
	def init_table_word_mapping(self):
		self.connection.execute(database_settings.TABLE_WORD_MAPPING_CREATE)
		
	
	def default_system_settings_exist(self):
		self.cursor.execute("SELECT * FROM %s" % (database_settings.TABLE_SYSTEM_SETTINGS))		
		return self.cursor.fetchone()
	
	def write_default_system_settings(self):
		dt_isoformat = datetime.datetime.now().isoformat()
		self.cursor.execute(
			"""
			INSERT INTO %s VALUES (
				'%s',
				'%s',
				'%s')""" % (
				database_settings.TABLE_SYSTEM_SETTINGS,
				default_system_settings.LANGUAGE,
				dt_isoformat,
				dt_isoformat))