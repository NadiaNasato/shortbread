import string
import parser

global LETTERS
LETTERS = list(string.ascii_lowercase)

def create_graph(start, end, show_path=False):
	length = len(start)
	words = parser.parse()[length]
	found = False
	
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
		for i in range(length):
			for l in LETTERS:
				word = make_word(node, i, l)
				if word in words and not word_graph[word]['visited']:
					visit_node(word, node, word_graph)
					nodes.append(word)
					if word == end:
						found = True

	if found and show_path:
		words_path = find_path(start, end, word_graph)
		print_path(words_path)

	return found

def make_word(word, index, letter):
	return word[0:index] + letter + word[index+1:len(word)]

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