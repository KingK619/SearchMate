from modules import *

logger = Signale() 

# Fetch all the text out of the query document and store in a variable
def extractDocx(filename):
	query=""
	Lines=""
	f = magic.Magic(mime=True)
	fileType=""
	if path.exists(filename):
		fileType = f.from_file(filename)
	else:
		logger.error("Input File Doesnot exists")
		exit()

	# Check if document is txt  
	if fileType == "text/plain":
		try:
			file1 = open(filename,"r",encoding="utf8")
			Lines = file1.readlines()
			for line in Lines:
				query+=line	
			return query

		except Exception as e:
			logger.error('Error!!!! '+ str(e))
			exit()

	# Check if document is docx
	if fileType == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
		try:
			query = docxpy.process(filename)
			return query
		except Exception as e:
			logger.error('Error!!!! '+ str(e))
			exit()	

	# Check if document is pdf
	if fileType == "application/pdf":
		try:
			with pdfplumber.open(filename) as pdf:
			    for i in range(0,len(pdf.pages)):
			        page = pdf.pages[i]
	
			    return page.extract_text()
		except Exception as e:
			logger.error('Error!!!! '+ str(e))
			exit()

	else:
		logger.error("File Format not Supported. Supported Formats [[[PDF, DOCX, TXT]]]")
		exit()		        

