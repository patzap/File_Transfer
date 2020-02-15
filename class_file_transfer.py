import os, shutil
import logging

logging.basicConfig(filename = 'Class_Transfer.log', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')
logging.debug('Start of script: ')

class transfer:

	def __init__(self, download_path, file_transfer, file_destination):
		self.download_path = download_path 
		self.file_transfer = file_transfer
		self.file_destination = file_destination

	def format_transfer(self):
		os.chdir(self.download_path)
		logging.debug(os.listdir())
		transfer_file = logging.debug([shutil.move(self.download_path, self.destination) 
			for files in self.download_path if files.endswith(self.file_transfer)])
		return transfer_file

python_file = transfer('C:\\Users\\flame\\Downloads', '.py', 'C:\\Users\\flame\\Documents\\Python_projects')
python_file.format_transfer()

java_file = transfer('C:\\Users\\flame\\Downloads', '.java', 'C:\\Users\\flame\\Documents\\Java_Ex')
java_file.format_transfer()



#create a class that contains path and transfer objects
#instances are going to be the specific file formats that will call out the objects, depending if the conditions are met. 