import random
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Main():

	emailAndPass = open(emailAndPass, "r")
	inputCredentials = emailAndPass.readlines()
	credentialsList = [x.split(" ") for x in inputCredentials]

	myEmail = credentialsList[0]
	myPass = credentialsList[1]

	names = []
	emails = []
	recipients = []
	budget = 50

	# print("Provide a txt document in the same directory with the specific format of: name, email address")
	# fileName = str(input("Name of the txt file with the .txt at the end: "))

	fileName = "names.txt"
	if fileName[-4:] != ".txt":
		print("File must end in .txt")
		return

	text = open(fileName,"r")
	inputString = text.readlines()
	inputRows = [x.replace("\n","").split(", ") for x in inputString]
	for x in inputRows:
		names.append(x[0])
		emails.append(x[1])

	nameCopy = names.copy()
	for name in nameCopy:
		withoutThisName = [ x for x in names if x != name ]
		randomName = random.choice(withoutThisName)
		recipients.append(randomName)
		names.remove(randomName)

	for i in range(len(nameCopy)):
		print(nameCopy[i] + " has " + recipients[i])

	for index in range(len(nameCopy)):

		# Create mail message
		mailContent = f''' Hello {nameCopy[i]},
		You are the secret santa of {recipients[i]}!
		Remember the budget is ${budget}.

		- Python script at (https://github.com/Sharwin24/Secret-Santa)
 		'''

 		message = MIMEMultipart()
 		message['From'] = myEmail
 		message['To'] = emails[i]
 		message['Subject'] = 'Secret Santa'

 		message.attach(MIMEText(mailContent, 'plain'))

 		session = smtplib.SMTP('smtp.gmail.com', 587)
 		session.connect("smtp.gmail.com", 587)
 		session.ehlo()
 		session.starttls()
 		session.login()


if __name__ == "__main__":
	Main()