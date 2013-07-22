#!/usr/bin/python

import sys

def use_cases():
	cases = """
Use cases:

	$ %(prog)s add <band>
	$ %(prog)s del <band>
	$ %(prog)s edit <band>
	$ %(prog)s add <folder> to <band>
	$ %(prog)s del <folder> from <band>
	$ %(prog)s edit <folder> of <band>
	"""
	
	return cases

if __name__ == '__main__':
	print use_cases() % {'prog': sys.argv[0]}