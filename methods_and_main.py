import json
from classes import User
from trainfaces import recognize_faces

image_path = '57210745_424343178361531_7059295302397722624_n.jpg'

def find_user(image_path):
	## Gets profile from database. If user is new, create a new profile
	user_id, confidence_level = recognize_faces(image_path)
	if (submit_check(user_id, image_path) == -1):
		results = submit_new(user_id, image_path)
	else:
		results = submit_check(user_id, image_path)

	return results, confidence_level

# creates new user profile, updates this in json file, and returns newly created profile
def submit_new(user_id, confidence_level, input_key, input_value):
	user_set = load_json()
	results = User(user_id, image_path)
	# user_set[user_id] = { 'name': 'Pringles', "comments": ["good", "no problems"], "medical_history": [] }
	# dictionary = user_set[user_id]
	#print(user_set)
	dictionary = {}
	for keys, values in user_set.items():
		if keys == str(user_id):
			dictionary = values

	temp = []
	temp.append(input_value)
	dictionary[input_key] = temp

	'''
	for keys, values in dictionary.items():
		if keys == str(input_key):
			temp = []
			temp.append(input_value)
			dictionary[keys] = temp
	'''
	user_set[str(user_id)] = dictionary
	write_json(user_set)
	return results

# ets specific user object from the json file
def submit_check(user_id, image_path):
	# user_id = get user id from neural network
	user_set = load_json()
	for keys, values in user_set.items():
		if keys == user_id:
			return keys
		else:
			return -1

def load_json():
	with open("test.json") as f:
  		data = json.load(f)
	return data

def write_json(user_set):
	with open('user_set.txt', 'w') as json_file:
  		json.dump(user_set, json_file)
	return 0

def get_user_info(user_id, confidence_level):
	user_set = load_json()
	for keys, values in user_set.items():
		print(user_id)
		if keys == str(user_id):
			return values
	return -1

def return_gui(image_path):
	user_id, confidence_level = recognize_faces(image_path)
	info = get_user_info(user_id, confidence_level)
	# for keys, values in info.items():
		# for item in values:
			# print(values)

	return user_id, confidence_level, 'alternative_path', info

if __name__ == '__main__':
	#result, random = find_user(image_path)
	user_id, confidence_level, alternative_path, info = return_gui(image_path)
	print(user_id)
	print(confidence_level)
	print(alternative_path)
	print(info)
	# path, confidence level finger+, id num, 