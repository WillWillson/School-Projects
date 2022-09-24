# Imports
import sys
import datetime
import hashlib
import time
import pytz
from numpy import byte

# declaration of variables
givenTime = sys.stdin.readlines()
givenTimeStr = ""
hashNumStr = ""
hashLetterStr = ""
reverseHashNumStr = ""
firstTwoLet = ""
lastTwoNum = ""
finalStr = ""

timezoneC = pytz.timezone('US/Central')

# This part of the code will add the input to a string
i = 0
for i in givenTime:
    givenTimeStr = givenTimeStr + i

epochTime = timezoneC.localize(datetime.datetime.strptime(givenTimeStr, '%Y %m %d %H %M %S '))

# Creates the current time 
currentTime = datetime.datetime.now(tz = pytz.UTC).astimezone(timezoneC)

# Used for set your own current time
#currentTime = timezoneC.localize(datetime.datetime(2010, 6, 13, 12, 55, 34))

# Used to format the current time to match the other time
formatCurrTime = currentTime.strftime('%Y %m %d %H %M %S ')

# Calculates the ammount of seconds from an epoch time
timeSinceEpochTime = int((currentTime - epochTime).total_seconds())

# calculates for the alloted 60 second 
timeSinceEpochTime = timeSinceEpochTime-(timeSinceEpochTime%60)

# will get the coresponding hash for the amount of seconds was determined
hashVariable = hashlib.md5(str(timeSinceEpochTime).encode("utf-8")).hexdigest()
doubleHashVariable = hashlib.md5(str(hashVariable).encode("utf-8")).hexdigest()
hashOutput = str(doubleHashVariable)

# This part of the code will look through the hash output string and check whether or not the value is a digit or not, and ad the string to its own specific string 
j = 0
for j in hashOutput:
    k = str(j)

    # checks if k is a digit
    if k.isdigit() == True:
        hashNumStr += k

    # checks if k is a digit
    elif k.isdigit() == False:
        hashLetterStr += k

# This gets the first two letters of the hash letter string
firstTwoLet = hashLetterStr[:2]

# This reverses the hash number string to be able to add the last ttwo numbers to the final string
reverseHashNumStr = hashNumStr[::-1]

# This get the first two numbers from the reverses string
lastTwoNum = reverseHashNumStr[:2]

# This will add the first two letters, and the first two numbers of the reverse string to the final string
finalStr += firstTwoLet
finalStr += lastTwoNum

# This is the final part of the code that sends the output to stdout, which is the final string, and the current time
sys.stdout.write("current system time: {}\n".format(formatCurrTime))
sys.stdout.write("{}\n".format(finalStr))