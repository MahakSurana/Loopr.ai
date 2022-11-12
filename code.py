import os

file_path = os.path.join('.', 'file.txt')

word_dict = dict()

with open(file_path, 'r') as file:
	for line in file:
		for word in line.split():
			if word not in word_dict:
				word_dict[word] = 0
	
			word_dict[word] += 1

max_counter = 0
which_word = ""

for key, value in word_dict.items():
	if value > max_counter:
		max_counter = value
		which_word = key

with open(file_path, 'w+') as file:
	with open("temp.txt", "w") as temp_file:
		for line in file:
			line.replace(which_word, "loopr")
			temp_file.write(line)
	
	
	with open("temp.txt", "r") as temp_file:	
		for line in temp_file:
			file.write(line)
	
	os.remove("temp.txt")

