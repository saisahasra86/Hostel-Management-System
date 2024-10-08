import sqlite3 as sqlite
import os
dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'mess_manager_database.db')

class mess_manager_db:

	@classmethod
	def create_table(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='_table'  ")

		if c.fetchone()[0] == 0 :

			c.execute(""" CREATE TABLE warden_table(
				
				name text,
				username text,
				password text,
				salary real,
				hostel_name text
				hostel_id int,
				clerk_id int,
				mess_manager_id int
					
				)""")

		conn.commit()
		conn.close()