import os
from sys import path

def saveResults(sorted_results,output_directory):
	f = open(output_directory,"w")
	for key,value in sorted_results.items():
		f.write( str(key) + " =====> " + str(value) + "\n\n")
	f.close()
