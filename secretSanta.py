import random
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Main():

	myEmail = "sharwin24@gmail.com"

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

if __name__ == "__main__":
	Main()