#!/usr/bin/python

import sys
import io
import optparse
import ConfigParser

def use_cases(): 
	cases = """
Use case: 

	$ %(prog)s 
		convert all files in current folder and leave converted files in it.
	$ %(prog)s *.wav 
		convert all files matching pattern *.wav in current folder and leave 
		converted files in it. 
	$ %(prog)s --destination=<path>
		convert all files in current folder and move converted into <path>.
	$ %(prog)s --destination=<path> file1 file2 ...
		convert file1 file2 ... and move converted into <path>.
	$ %(prog)s --band=<band>
		convert all files for <band> recursively.
	$ %(prog)s --band=<band> last 
		convert the last record session for <band>.
	$ %(prog)s --band=<band> 3th 
		convert the third from last record session for <band>.  
	$ %(prog)s --band=<band> --order=date 3th
		convert the third from last record session for <band>.
	$ %(prog)s --band=<band> --order-date --direction=asc 3th 
		convert the third record session for <band>. 
	$ %(prog)s --band=<band> --from=<from_date> --to=<to_date>
		convert all tracks for <band> saved between <from_date> and <to_date>
	$ %(prog)s --band=<band> --after=<date>
		convert all tracks for <band> saved after <date> 
	$ %(prog)s --band=<band> --before=<date>
		convert all tracks for <band> saved before <date>
	$ %(prog)s --source=<path> 
		convert all tracks found into <path> 
	

"""	
	return cases


if __name__ == '__main__':
	optparser = optparse.OptionParser();
	optparser.add_option('-c', '--config', dest="config_path", help="specify the path to the config file", default='convert_tracks.config')
	
	(options, args) = optparser.parse_args()
	
	print use_cases() % {'prog': sys.argv[0]}