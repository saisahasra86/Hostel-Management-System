import sqlite3 as sqlite
import os
dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'complaints_database.db')

class complaints_db:

	@classmethod
	def create_table(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='complaints_table'  ")

		if c.fetchone()[0] == 0 :

			c.execute(""" CREATE TABLE complaints_table(

				from_student_id int,
				from_student_name text,
				warden_id int,
				warden_name text,
				hostel_name text,
				complaint text,
				ATR text

				)""")

		conn.commit()
		conn.close()



	@classmethod
	def insert_records(cls, details):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("INSERT INTO complaints_table VALUES (?,?,?,?,?,?,?)", details)


		conn.commit()
		conn.close()


	@classmethod
	def get_all_records(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM complaints_table")
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_record_by_student_id(cls, student_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("SELECT oid, * FROM complaints_table WHERE oid = ?", (student_id, ))
		record = c.fetchall()
		

		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_records_by_warden_id(cls, warden_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("SELECT oid, * FROM complaints_table WHERE oid = ?", (warden_id, ))
		record = c.fetchall()
		

		conn.commit()
		conn.close()

		return records


	@classmethod
	def update_ATR(cls, atr, comp_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE complaints_table SET ATR = ?
					WHERE oid = ?""", (atr,comp_id))

		conn.commit()
		conn.close()



# complaints_db.create_table()
# complaints_db.insert_records((1,'Vyahruth',2,'jon','Chenab','no water', ''))

# recordsssss = complaints_db.get_all_records()

# print(recordsssss)

# complaints_db.insert_records((4,'niharika',2,'jon', 'Raavi', 'electricity gone', 'Okay, will see'))
# complaints_db.update_ATR("will fix it", recordsssss[0][0])

# recordsssss = complaints_db.get_all_records()
# print(recordsssss)
















