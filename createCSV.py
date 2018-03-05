import csv
import datetime

class CSV:
	def __init__(self,schedule, startDate, endDate, fileName):
		self.schedule = schedule
		self.startDate = startDate
		self.endDate = endDate
		self.fileName = fileName

	def correctNumber(self,number):
		number = list(number)
		if(number[0] == 0):
			del number[0]
		return ''.join(number)


	def createDate(self, date):
		splitDate = date.split('/')
		splitDate[0] = self.correctNumber(splitDate[0])
		splitDate[1] = self.correctNumber(splitDate[1])
		return datetime.date(int(splitDate[2]), int(splitDate[1]), int(splitDate[0]))



	def writeFile(self):
		print('Writing in '+self.fileName)
		with open(self.fileName, 'w', newline='') as csvfile:
			fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Location', 'Private']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			self.startDate = self.createDate(self.startDate)
			self.endDate = self.createDate(self.endDate)
			actualDate = self.startDate
			for i in range (abs(self.startDate-self.endDate).days + 1):
				weekDay = actualDate.weekday()
				for classs in self.schedule[weekDay]:
					classs[1] = actualDate.strftime('%m/%d/%Y')
					classs[3] = actualDate.strftime('%m/%d/%Y')
					writer.writerow({'Subject' : classs[0], 'Start Date' : classs[1], 'Start Time' : classs[2], 'End Date' : classs[3], 'End Time' : classs[4], 'Location': classs[5], 'Private' : 'True'})
				actualDate = actualDate + datetime.timedelta(days=1)	
		print('Done!')

