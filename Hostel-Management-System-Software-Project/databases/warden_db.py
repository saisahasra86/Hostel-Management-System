import sqlite3 as sqlite
import os
dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'warden_database.db')

class warden_db:

	@classmethod
	def create_table(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='warden_table'  ")

		if c.fetchone()[0] == 0 :

			c.execute(""" CREATE TABLE warden_table(
				
				name text,
				username text,
				password text,
				key text,
				salary real,
				hostel_name text,
				hostel_id int,
				clerk_salary real,
				amenity_collection real,
				institute_grant real,
				ward_salary_spent real,
				work_salary_spent real,
				clerk_salary_spent real
					
				)""")

		conn.commit()
		conn.close()


	@classmethod
	def insert_record(cls,details):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("INSERT INTO warden_table VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", details)


		conn.commit()
		conn.close()


	@classmethod
	def get_all_records(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM warden_table")
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_record_by_id(cls, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM warden_table WHERE oid = ?", (id_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record


	@classmethod
	def get_records_by_name(cls, name_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM warden_table WHERE name = ?", (name_, ))
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_record_by_username(cls, username_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM warden_table WHERE username = ?", (username_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record

	@classmethod
	def get_record_by_hostel_id(cls, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM warden_table WHERE hostel_id = ?", (id_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record	



	@classmethod
	def update_warden_name(cls, new_nam, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET name = ?
					WHERE oid = ? """, (new_nam,war_id))

		conn.commit()
		conn.close()


	@classmethod
	def update_warden_username(cls, new_nam, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET username = ?
					WHERE oid = ? """, (new_nam,war_id))

		conn.commit()
		conn.close()


	# @classmethod
	# def update_warden_password(cls, new_pass, war_id):

	# 	conn = sqlite.connect(file)
	# 	c = conn.cursor()

	# 	c.execute("""UPDATE warden_table SET password = ?
	# 				WHERE oid = ? """, (new_pass,war_id))

	# 	conn.commit()
	# 	conn.close()



	@classmethod
	def update_warden_salary(cls, new_sal, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET salary = ?
					WHERE oid = ? """, (new_sal,war_id))

		conn.commit()
		conn.close()


	@classmethod
	def update_clerk_salary(cls, new_sal, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET clerk_salary = ?
					WHERE oid = ? """, (new_sal,war_id))

		conn.commit()
		conn.close()


	@classmethod
	def update_amenities_collection(cls, total, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET amenity_collection = ?
					WHERE oid = ? """, (total,war_id))

		conn.commit()
		conn.close()


	@classmethod
	def update_institute_grant(cls, total, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET institute_grant = ?
					WHERE oid = ? """, (total,war_id))

		conn.commit()
		conn.close()


	@classmethod
	def update_ward_salary_spent(cls, total, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET ward_salary_spent = ?
					WHERE oid = ? """, (total,war_id))

		conn.commit()
		conn.close()


	@classmethod
	def update_clerk_salary_spent(cls, total, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET clerk_salary_spent = ?
					WHERE oid = ? """, (total,war_id))

		conn.commit()
		conn.close()


	@classmethod
	def update_work_salary_spent(cls, total, war_id):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE warden_table SET work_salary_spent = ?
					WHERE oid = ? """, (total,war_id))

		conn.commit()
		conn.close()



warden_db.create_table()






