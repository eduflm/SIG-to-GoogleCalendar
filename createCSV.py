import csv

#For now, this file only exists as a base for the future

class CSV:
	def __init__(self,schedule, startDate, endDate, fileName):
		self.schedule = schedule
		self.startDate = startDate
		self.endDate = endDate
		self.fileName = fileName



	def writeFile(self):
		with open(self.fileName, 'w', newline='') as csvfile:

			fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Location', 'Private']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

			writer.writeheader()
			writer.writerow({'Subject' : 'GCC-199 - Computação Gráfica', 'Start Date' : '02/27/2018', 'Start Time' : '10:00 AM', 'End Date' : '02/27/2018', 'End Time' : '11:40 AM', 'Location':'PV2-106', 'Private' : 'True'})
			writer.writerow({'Subject' : 'GCC-199 - Computação Gráfica', 'Start Date' : '02/28/2018', 'Start Time' : '10:00 AM', 'End Date' : '02/28/2018', 'End Time' : '11:40 AM', 'Location':'PV2-106', 'Private' : '1True'})
			writer.writerow({'Subject' : 'GCC-199 - Computação Gráfica', 'Start Date' : '02/29/2018', 'Start Time' : '10:00 AM', 'End Date' : '02/29/2018', 'End Time' : '11:40 AM', 'Location':'PV2-106', 'Private' : 'True'})
