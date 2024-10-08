import sqlite3 as sqlite 
import os
dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'student_database.db')

class student_db:

	@classmethod
	
	def create_table(cls):
		
		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='student_table'  ")

		if c.fetchone()[0] == 0 :

			c.execute(""" CREATE TABLE student_table(

					name text,
					address text,
					contact_number text,
					username text,
					password text,
					key text,
					hostel_name text,
					mess_due real,
					other_dues real,
					room_type int,
					room_number text					
					

				)""")

		conn.commit()
		conn.close()



	@classmethod
	def insert_records(cls, details):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("INSERT INTO student_table VALUES (?,?,?,?,?,?,?,?,?,?,?)", details)


		conn.commit()
		conn.close()


	@classmethod
	def get_all_records(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM student_table")
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_records_by_name(cls, name_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM student_table WHERE name = ?", (name_, ))
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_record_by_username(cls, username_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM student_table WHERE username = ?", (username_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record		


	@classmethod
	def get_record_by_id(cls, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM student_table WHERE oid = ?", (id_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record



	@classmethod
	def get_records_by_hostel(cls, hall_nam):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM student_table WHERE hostel_name = ?", (hall_nam, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record


	@classmethod
	def update_mess_charge(cls, charge, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE student_table SET mess_due = ?
					WHERE oid = ? """, (charge,id_))

		conn.commit()
		conn.close()



	@classmethod
	def update_other_charge(cls, charge, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE student_table SET other_dues = ?
					WHERE oid = ? """, (charge,id_))

		conn.commit()
		conn.close()


	@classmethod
	def update_hall_name(cls, hostel_name, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE student_table SET hall_name = ?
					WHERE oid = ? """, (hostel_name,id_))

		conn.commit()
		conn.close()


	@classmethod
	def update_room_type(cls, typ, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE student_table SET room_type = ?
					WHERE oid = ? """, (typ,id_))

		conn.commit()
		conn.close()


	@classmethod
	def update_room_number(cls, num, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE student_table SET room_number = ?
					WHERE oid = ? """, (num,id_))

		conn.commit()
		conn.close()	






