import requests
import sys
import getpass
import urllib3
import numpy as np
from pathlib import Path
from bs4 import BeautifulSoup
from createCSV import CSV
from urllib.parse import urljoin

class Schedule:
	def __init__(self,info):
		self.info = info
		self.sigURL = 'https://sig.ufla.br/modulos/login/index.php'
		self.scheduleURL = 'https://sig.ufla.br/modulos/alunos/utilidades/horario.php'
		self.session = requests.Session()

	def getClassSchedule(self):
		pageData = self.connectToSIG()
		self.findFormAndLogin(pageData)
		print ("Extracting data...")
		schedulePage = self.session.get(self.scheduleURL, verify=False)
		soup = BeautifulSoup(schedulePage.text, 'html.parser')
		scheduleBoard = soup.find('tbody')
		matrix = [[td.text for td in tr.findAll('td')] for tr in scheduleBoard.findAll('tr')]
		shceduleDict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
		for index, row in enumerate(matrix):
			matrix[index][0] = self.correctTime(row[0])
		matrix = np.array(matrix)
		for row in matrix:
			for i in range (1, 8):
				if row[i] != '-':
					classAndLocation = row[i].split(' - ')
					classCode = classAndLocation[0].split(' ')[0]
					className = classCode+' - '+soup.find('abbr', string=classCode)['title'].split(' / ')[0]
					scheduleIndex = i-2
					if (scheduleIndex < 0):
						scheduleIndex = 6
					shceduleDict[i-2].append([className,'',row[0], '', self.endDate(row[0]), classAndLocation[1]])
		print("Data extracted!")
		return shceduleDict

	def endDate(self,time):
		hour = int(time.split(':')[0])
		period = time.split(':')[1]

		hour += 1
		if (hour == 12):
			return (str(hour)+':00 PM')
		elif (period == "00 PM"):
			return (str(hour)+':00 PM')
		else:
			return (str(hour)+':00 AM')

	def correctTime(self, time):
		hour = int(time.split(':')[0])
		if (hour > 12):
			hour = hour - 12
			return (str(hour)+':00 PM')
		else :
			return (str(hour)+':00 AM')



	def findFormAndLogin(self,formData):
		soup = BeautifulSoup(formData, 'html.parser')
		form = soup.find('form')
		fields = form.findAll('input')
		formdata = dict( (field.get('name'), field.get('value')) for field in fields)

		formdata['login'] = self.info['login']
		formdata['senha'] = self.info['password']

		posturl = urljoin(self.sigURL, form['action'])

		print ('Trying to login...')
		response = self.session.post(posturl, data=formdata)
		if response.url != self.sigURL:
			print ('Login successful')
			return response
		else:
			print ('Unable to login. Verify your credentials')
			sys.exit()



	def connectToSIG(self):
		#Try to connect to SIG index
		print ('Connecting to '+self.sigURL+' ...')
		page = self.session.get(self.sigURL, verify=False)
		if page.status_code == 200:
			print ('Connected!')
			return page.text
		else:
			print ('Unable to connect to '+self.sigURL+' Aborting...')
			sys.exit()
		


def getInfo():
	info = {}
	info['login'] = input("Enter your SIG login: ")
	info['password'] = getpass.getpass(prompt='Enter your SIG password: ')
	info['startDate'] = input("Enter the start date (DD/MM/YYYY): ")
	info['endDate'] = input("Enter the end date (DD/MM/YYYY): ")
	info['fileName'] = 'calendar.csv'
	return info

def getInfoFromFile(fileData):
	data = fileData.read().splitlines()
	info = {}
	info['login'] = data[0]
	info['password'] = data[1]
	info['startDate'] = data[2]
	info['endDate'] = data[3]
	info['fileName'] = data[4]
	return info


if __name__ == "__main__":
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	configFile = Path("data.config")
	if(configFile.exists()):
		configFile = open('data.config', "r")
		info = getInfoFromFile(configFile)
	else:
		info = getInfo()
	schedule = Schedule(info)
	schedule = schedule.getClassSchedule()
	csvFile = CSV(schedule, info['startDate'], info['endDate'], info['fileName'])
	csvFile.writeFile()



	




