import requests
import sys
import getpass
import urllib3
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
		schedulePage = self.session.get(self.scheduleURL, verify=False)
		soup = BeautifulSoup(schedulePage.text, 'html.parser')
		scheduleBoard = soup.find('tbody')
		matrix = [[td.text for td in tr.findAll('td')] for tr in scheduleBoard.findAll('tr')]
		for index, row in enumerate(matrix):
			matrix[index][0] = self.correctTime(row[0])
		for row in matrix:
			print (row)			

		#Como estamos em período de recesso, ainda não é possível testar o programa

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
	#info['startDate'] = input("Enter the start date (MM/DD/YYYY): ")
	#info['endDate'] = input("Enter the end date (MM/DD/YYYY): ")
	info['startDate'] = '01/03/2018'
	info['endDate'] = '09/03/2018'
	info['fileName'] = 'example.csv'
	return info


if __name__ == "__main__":
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	info = getInfo()
	schedule = Schedule(info)
	schedule.getClassSchedule()
	csvFile = CSV(schedule, info['startDate'], info['endDate'], info['fileName'])
	csvFile.writeFile()



	




