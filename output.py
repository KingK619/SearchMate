import os
from sys import path

def saveResults(sorted_results,output_directory):
	print(type(output_directory))
	if path.exists(output_directory):
		f = open(output_directory + "results.txt","w")
		for key,value in sorted_results.items():
			f.write( str(key) + " =====> " + str(value) + "\n\n")
		f.close()
	else:
		logger.error("Path Doesnot exists")
		exit()	
