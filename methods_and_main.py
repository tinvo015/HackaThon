def find_user():
	user_photo = record_photo()
	user_fingerprint = record_fingerprint()
	user_voice = record_voice()

	##Gets profile from database. If user is new, create a new profile

	results
	if (not user_in_database(user_photos, user_fingerprint, user_voice)):
		results = submit_new_user(user_photos, user_fingerprint, user_voice)
	else:
		results = get_user(user_photos, user_fingerprint, user_voice)


	return results


#creates new user profile, updates this in json file, and returns newly created profile
def submit_new(user_photos, user_fingerprint, user_voice):
	user_set = import json data file into hashset
	results = User(len(user_set) + 1, user_photos, user_voice, user_fingerprint)
	user_set.add(results)
	dump user_set back into json data file
	return results


#gets specific user object from the json file
def submit_check(user_photos, user_fingerprint, user_voice):
	user_id = get user id from neural network

	user_set = import json data file into hashset
	for person in user_set
		if person.id_num == user_id:
			return person