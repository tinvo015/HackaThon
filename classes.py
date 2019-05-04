class User:
	def __init__(self, id_num, photo):
		self.photo = photo
		self.medical = {}
		self.id_num = id_num


	def add_medical_info(keyword, values):
		self.medical[keyword] = values
		return self.medical

	def remove_medical_info(keyword):
		del self.medical[keyword]
		return self.medical
