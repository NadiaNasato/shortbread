dflt_file = './words/british-english.txt'

def parse(length, f=dflt_file):
	try:
		dict_file = open(f, 'r')

		try:
			dict_set = set()

			for line in dict_file:
				word = normalize(line)
				if len(word) == length:
					dict_set.add(word)

			return dict_set

		finally:
			dict_file.close()

	except IOError:
		raise

def normalize(word):
	return word.strip().lower()
