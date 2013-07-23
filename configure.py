#!/usr/bin/python

import sys
import pymongo
import curses
from term import Colors
from band import Band

# initializations
c = Colors()


def use_cases():
	cases = """
Use cases:

	$ %(prog)s add <band>
	$ %(prog)s del <band>
	$ %(prog)s edit <band>
	$ %(prog)s list
	$ %(prog)s add <folder> to <band>
	$ %(prog)s del <folder> from <band>
	$ %(prog)s edit <folder> of <band>
	$ %(prog)s list <band>
	"""
	
	return cases

def message(msg, type='notice'):
	output = '%s>>>%s %s'
	if type == 'warning':
		print output % (c.fg('yellow'), c.reset(), msg)
	elif type == 'error':
		print output % (c.fg('red'), c.reset(), msg)
	else:
		print output % (c.fg('cyan'), c.reset(), msg)

def init_db():
	try:
		mongo = pymongo.MongoClient()
	except pymongo.errors.ConnectionFailure:
		message('Cannot connect to mongodb.', 'error')
		raise
	
	return mongo.convert_tracks	

if __name__ == '__main__':
	print use_cases() % {'prog': sys.argv[0]}

	if len(sys.argv) not in [3, 5]:
		message('Invalid number of arguments.', 'error')
		raise Exception('Invalid number of arguments.')
	
	action = sys.argv[1]
	if len(sys.argv) == 3:
		command = 'band'
		band_name = sys.argv[2]
	else:
		command = 'folder'
		folder_name = sys.argv[2]
		band_name = sys.argv[4]
	
	db = init_db()
	config = db.config
	
