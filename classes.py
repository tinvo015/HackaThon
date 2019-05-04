class user:
	def __init__(self, name, photo, voice):
		self.photo = photo
		self.voice = voice
		self.name = name
		self.medical = {}

	def add_medical_info(keyword, values):
		self.medical[keyword] = values
		return self.medical

	def remove_medical_info(keyword):
		i = 5
		del self.medical[keyword]
		return self.medical











