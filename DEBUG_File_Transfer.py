import os, shutil
import logging 

# Simple script that imports .java an .py files from the Download folder into a Python or Java folder. 

logging.basicConfig(filename = 'File_Transfer.log', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')
logging.debug('Start of programming')

def download_path(path):
	os.chdir(path)
	download_list = os.listdir()
	return download_list

def py_java_transfer(java_destination, py_destination):

	try:

		num = 1

		while num > 3:
			# Loops the list of files in the download_path function and searches for files that end with .java and transfers them to the Java folder
			java_transfer = [shutil.move(java_files, java_destination) 
			for java_files in download_path('C:\\Users\\flame\\Downloads') if java_files.endswith('.java')]

			# Repeats the same process as the one above but with .py files. 
			py_transfer = [shutil.move(py_files, py_destination) 
			for py_files in download_path('C:\\Users\\flame\\Downloads') if py_files.endswith('.py')] 
			num += 1

		if num == 3:
			

	except:
		raise Exception('Error')

def other_files(downloads):
	
	logging.debug(type(downloads))

	extra_files = 'C:\\Users\\flame\\Downloads\\Extra_Files'
	logging.debug(type(extra_files))
	for other in downloads:
		logging.debug(type(other))
		shutil.move(other, extra_files)
	
py_java_transfer('C:\\Users\\flame\\Documents\\Java_Ex', 
	'C:\\Users\\flame\\Documents\\Python_projects')

other_files(download_path('C:\\Users\\flame\\Downloads'))