# script to save results in a txt document.
# saves links with their corresponding find score. 

import os

def saveResults(sorted_results,output_directory):
	if os.path.exists(output_directory):
		f = open(output_directory + "results.txt","w")
		for key,value in sorted_results.items():
			f.write( str(key) + " =====> " + str(value) + "\n\n")
		f.close()
	else:
		logger.error("Path Doesnot exists")
		exit()	
