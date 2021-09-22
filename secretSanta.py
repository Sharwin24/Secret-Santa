import random
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Running Secret-Santa")
# Collect credential information
credentialText = open("credentials.txt", "r")
inputCredentials = credentialText.readlines()
credentialsList = [x.split(" ") for x in inputCredentials]
myEmail = credentialsList[0][0]
myPass = credentialsList[0][1]

names = []
emails = []
recipients = []
budget = 0
giftDate = ""

fileName = "SecretSantaSetup.txt"
text = open(fileName,"r")
inputString = text.readlines()
inputRows = [x.replace("\n","").strip().split(",") for x in inputString]
budget = inputRows[0][0]
giftDate = inputRows[0][1]
for x in inputRows[1:]:
	names.append(x[0])
	emails.append(x[1])

nameCopy = names.copy()
for name in nameCopy:
	withoutThisName = [ x for x in names if x != name ]
	randomName = random.choice(withoutThisName)
	recipients.append(randomName)
	names.remove(randomName)

for index in range(len(nameCopy)):
	print("Sending email number " + str(index + 1))
	# Create mail message
	mailContent = f"Hello {nameCopy[index]},\nYou are the secret santa of {recipients[index]}! Remember the budget is ${budget}. Gifts will be given on ${giftDate}!\n\nPython script at:\n https://github.com/Sharwin24/Secret-Santa"
	theirEmail = emails[index]
	message = MIMEMultipart()
	message['From'] = myEmail
	message['To'] = theirEmail
	message['Subject'] = 'Secret Santa'
	message.attach(MIMEText(mailContent, 'plain'))
	# Create a SMTP session to send the email
	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.connect("smtp.gmail.com", 587)
	session.ehlo()
	session.starttls()
	session.login(myEmail, myPass)
	toEmail = message.as_string()
	session.sendmail(myEmail, theirEmail, toEmail)
	session.quit()
print("Finished sending emails!")