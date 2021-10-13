# Secret Santa?
Secret Santa is a traditional Christmas holiday game/activity. In the game, a group of people(typically friends/colleagues) are anonymously paired to another member of the group. Each member then purchases a Christmas gift for their chosen member. The identity of the gift-giver for each person <i>needs</i> to remain a secret until the day of the gift-giving.

# Purpose and Utility
This script will setup and email participants for a Secret Santa game. The script will automatically send an email from the given credentials to all the participants. The budget of the game, as well as the final gift date will also be included in the email. The pairings are fully randomized and the email will indicate who you're buying a gift for.

# Setup for the Script
This is a quick and dirty python script, to organize a Secret-Santa game between you and your friends. There is some setup involved. First you need to create a txt file named <code>SecretSantaSetup.txt</code>. The first line of the document should be the budget, as an <code>integer</code>, a comma, then the date of the gift giving day. The  following lines should follow the format: <code>FirstName LastName, emailAddress@email.com</code>. Fill out the information for every participant and ensure the <code>txt</code> file is in the same directory as <code>secretSanta.py</code>.

You also need to setup your email credentials. I recommend creating a separate gmail account for this script. Create a <code>txt</code> document in the same directory as <code>secretSanta.py</code>. On the first line, type in your email address, followed by a space, and then the password to the email address. It should look like this:

<code>myEmailName@gmail.com myPassword</code>