import time
import argparse

import path_engine

def main():
	show_path = False

	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('start', type=str, help="The first word of the connection")
	arg_parser.add_argument('end', type=str, help="The word you want to reach")
	arg_parser.add_argument('-p', '--path', action='store_true',
		help="Show the path from start word to end word")
	args = arg_parser.parse_args()

	if args.path:
		show_path = True

	start_word = args.start.lower()
	end_word = args.end.lower()

	start_time = time.time()
	found = path_engine.create_graph(start_word, end_word, show_path)
	end_time = time.time()

	if found:
		print('It is possible to connect "%s" to "%s"' % (start_word, end_word))
	else:
		print('It is not possible to connect "%s" to "%s"' % (start_word, end_word))

	print('Time: %s' % (end_time - start_time))

if __name__ == "__main__":
	main()