import docxpy, pdfplumber, os
import magic
def extractDocx():
	query=""
	Lines=""
	f = magic.Magic(mime=True)
	filename = input("Enter your filename with extension. Supported Formats [[[PDF, DOCX, TXT]]]: ") 
	fileType = f.from_file(filename)

	if fileType == "text/plain":
		try:
			file1 = open(filename,"r",encoding="utf8")
			Lines = file1.readlines()
			for line in Lines:
				query+=line	
			return query

		except Exception as e:
			print('Error!!!! '+ str(e))
			exit()

	if fileType == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
		try:
			query = docxpy.process(filename)
			return query
		except Exception as e:
			print('Error!!!! '+ str(e))
			exit()	

	if fileType == "application/pdf":
		try:
			with pdfplumber.open(filename) as pdf:
			    for i in range(0,len(pdf.pages)):
			        page = pdf.pages[i]
	
			    return page.extract_text()
		except Exception as e:
			print('Error!!!! '+ str(e))
			exit()

	else:
		print("File Format not Supported. Supported Formats [[[PDF, DOCX, TXT]]]")
		exit()		        

