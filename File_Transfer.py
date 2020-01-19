import os, shutil

'''Simple script that imports .java an .py files from the Download folder into a Python or Java folder. 
	The remaining files that are not the two are moved into the Extra_Files folder
	By Patrick Zapata (PatZap) Updated Jan 18 2020
'''


def download_path(path):
	os.chdir(path)
	download_list = os.listdir()
	return download_list

def py_java_transfer(java_destination, py_destination):

	# Loops the list of files in the download_path function and searches for files that end with .java and transfers them to the Java folder
	java_transfer = [shutil.move(java_files, java_destination) 
	for java_files in download_path('C:\\Users\\flame\\Downloads') if java_files.endswith('.java')]

	# Repeats the same process as the one above but with .py files. 
	py_transfer = [shutil.move(py_files, py_destination) 
	for py_files in download_path('C:\\Users\\flame\\Downloads') if py_files.endswith('.py')] 
			
			
def other_files(downloads):
	
	extra_files = 'C:\\Users\\flame\\Downloads\\Extra_Files'
	for other in downloads:
		shutil.move(other, extra_files)
	
py_java_transfer('C:\\Users\\flame\\Documents\\Java_Ex', 
	'C:\\Users\\flame\\Documents\\Python_projects')

other_files(download_path('C:\\Users\\flame\\Downloads'))