import random
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Main():
    print("Running Secret-Santa")
    input("Press Enter to Continue (This will send emails!)")
    # Collect credential information
    with open("credentials.txt", "r") as f:
        inputCredentials = f.readlines()
    credentialsList = [x.split(" ") for x in inputCredentials]
    myEmail = credentialsList[0][0]
    myPass = credentialsList[0][1]

    # Initialize variables for Setup
    names = []
    emails = []
    recipients = []
    budget = 0
    giftDate = ""

    # Obtain variables for setup through given TXT
    fileName = "SecretSantaSetup.txt"
    try:
        text = open(fileName, "r")
    except:
        print("Invalid SecretSantaSetup file name")
        return
    inputString = text.readlines()
    inputRows = [x.replace("\n", "").strip().split(",") for x in inputString]
    budget = inputRows[0][0]
    giftDate = inputRows[0][1]
    for x in inputRows[1:]:
        names.append(x[0])
        emails.append(x[1])

    nameCopy = names.copy()
    for name in nameCopy:
        withoutThisName = [x for x in names if x != name]
        randomName = random.choice(withoutThisName)
        recipients.append(randomName)
        names.remove(randomName)

    erroredEmails = 0
    for index in range(len(nameCopy)):
        print("Sending email number " + str(index + 1))
        # Create mail message
        try:
            mailContent = f"Hello {nameCopy[index]},\nYou are the secret santa of {recipients[index]}! Remember the budget is ${budget}. Gifts will be given on {giftDate}!\n\nPython script at:\n https://github.com/Sharwin24/Secret-Santa"
            theirEmail = emails[index]
            message = MIMEMultipart()
            message['From'] = myEmail
            message['To'] = theirEmail
            message['Subject'] = 'Secret Santa'
            message.attach(MIMEText(mailContent, 'plain'))
            # Create a SMTP session to send the email
            session = smtplib.SMTP("smtp.gmail.com", 587)
            session.connect("smtp.gmail.com", 587)
            session.ehlo()
            session.starttls()
            session.login(myEmail, myPass)
            toEmail = message.as_string()
            session.sendmail(myEmail, theirEmail, toEmail)
            session.quit()
        except Exception as e:
            print(f"Error sending email {index + 1}")
            print("===============================")
            print(e)
            print("===============================\n")
            erroredEmails = erroredEmails + 1
    print(f"Successfully sent {len(nameCopy) - erroredEmails} emails")


if __name__ == '__main__':
    Main()