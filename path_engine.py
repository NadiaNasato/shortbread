import string
import parser

def create_graph(start_word, end_word, show_path=False, dict_file=None):
	found = False
	start = start_word.lower()
	end = end_word.lower()

	if len(end) != len(start):
		return found

	try:
		if dict_file:
			words = parser.parse(len(start), dict_file)
		else:
			words = parser.parse(len(start))

	except IOError:
		raise

	else:

		if start not in words or end not in words:
			return found

		word_graph = {}
		for word in words:
			word_graph[word] = {
				'visited': False,
				'parent': None,
			}

		nodes = [start, ]
		word_graph[start]['visited'] = True

		while len(nodes) > 0 and not found:
			node = nodes.pop(0)
			for word in make_word(node):
				if word in words and not word_graph[word]['visited']:
					visit_node(word, node, word_graph)
					nodes.append(word)
					if word == end:
						found = True

		if found and show_path:
			words_path = find_path(start, end, word_graph)
			print_path(words_path)

		return found

def make_word(word):
	length = len(word)

	for i in range(length):
		for l in string.ascii_lowercase:
			yield word[0:i] + l + word[i+1:length]

def visit_node(node, parent, word_graph):
	word_graph[node]['visited'] = True
	word_graph[node]['parent'] = parent

def find_path(start, end, word_graph):
	word = end
	words = [word, ]
	while word_graph[word]['parent'] is not None:
		word = word_graph[word]['parent']
		words.append(word)
	words.reverse()
	return words

def print_path(words):
	for word in words:
		print word