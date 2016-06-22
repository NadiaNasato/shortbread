dflt_file = './words/british-english.txt'

def parse(f=dflt_file):
	dict_file = open(f, 'r')
	dict_map = {}

	for line in dict_file:
		word = normalize(line)
		length = len(word)
		if length not in dict_map.keys():
			dict_map[length] = set([word])
		else:
			dict_map[length].add(word)

	return dict_map

def normalize(word):
	return word.strip().lower()