def find_user():
	user_photo = record_photo()
	user_fingerprint = record_fingerprint()
	user_voice = record_voice()

	##Gets profile from database. If user is new, create a new profile

	results
	if (not user_in_database(user_photos, user_fingerprint, user_voice)):
		results = submit_new(user_photos, user_fingerprint, user_voice)
	else:
		results = submit_check(user_photos, user_fingerprint, user_voice)


	return results

def submit_new(user_photos, user_fingerprint, user_voice):
	user = user()

	user.photo = user_photos
	user.fingerprint = user_fingerprint
	user.voice = user_voice

	return results

def submit_check(user_photos, user_fingerprint, user_voice):
	user = user()

	return user_photos == user.photo and user_fingerprint == user.fingerprint and
			user_voice == user.voice