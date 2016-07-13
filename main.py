import time
import argparse
import sys

import path_engine

def main():
	show_path = False
	dict_file = None

	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('start', type=str, help="The first word of the connection")
	arg_parser.add_argument('end', type=str, help="The word you want to reach")
	arg_parser.add_argument('-p', '--path', action='store_true',
		help="Show the path from start word to end word")
	arg_parser.add_argument('-f', '--file',
		help="Use a different dictionary file")
	args = arg_parser.parse_args()

	if args.path:
		show_path = True

	if args.file:
		dict_file = args.file

	start_word = args.start
	end_word = args.end

	start_time = time.time()

	try:
		found = path_engine.create_graph(start_word, end_word, show_path, dict_file)

	except IOError, e:
		print e
		sys.exit(0)

	else:
		end_time = time.time()

		if found:
			print('It is possible to connect "%s" to "%s"' % (start_word, end_word))
		else:
			print('It is not possible to connect "%s" to "%s"' % (start_word, end_word))

		print('Time: %s' % (end_time - start_time))

if __name__ == "__main__":
	main()