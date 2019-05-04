import json
from classes import User

def find_user():
	user_photo = record_photo()

	## Gets profile from database. If user is new, create a new profile

	results
	if (submit_check() == -1):
		results = submit_new()
	else:
		results = submit_check()

	return results

# creates new user profile, updates this in json file, and returns newly created profile
def submit_new(user_id, confidence_level):
	user_set = load_json()
	results = User(user_id, photo_path)
	user_set[len(user_set)] = { 'name': 'Bob', "comments": ["good", "no problems"], "medical_history": [] }
	write_json(user_set)
	return results


# ets specific user object from the json file
def submit_check(user_id, confidence_level):
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


if __name__ == '__main__':
	submit_check(3, 0.9)