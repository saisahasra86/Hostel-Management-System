from cryptography.fernet import Fernet


class login():

	def __init__(self,username,password):

		self.username = username
		self.password = password


	def validate(self,pas_a,pas_b):

		if pas_a == pas_b:
			return True
		else:
			return False

	def encrypt(self, key):

		fernet = Fernet(key.encode("utf-8"))

		encrypted_password = fernet.encrypt(self.password.encode("utf-8"))

		return encrypted_password

	def decrypt(self, key):

		fernet = Fernet(key.encode("utf-8"))

		decrypted_password = fernet.decrypt(self.password).decode("utf-8")

		return decrypted_password