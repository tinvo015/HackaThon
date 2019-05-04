import json

def load_json():
	with open("test.json") as f:
  		data = json.load(f)
	print(len(data))
	return data






if __name__ == '__main__':
	data = load_json()
	for keys,values in data.items():
		print(keys)
