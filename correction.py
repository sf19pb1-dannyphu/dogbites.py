"""
Dog_bites.py
Reported number of dog bites in NYC from 2015 to 2017.
"""

import sys
import urllib.request
import csv
import collections

#https://data.cityofnewyork.us/Health/DOHMH-Dog-Bite-Data/rsgh-akpg
url = "https://data.cityofnewyork.us/api/views/rsgh-akpg/rows.csv?accessType=DOWNLOAD"

try:
    urlfile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

readbytes = urlfile.read() #reads whole file into one big sequence of bytes
urlfile.close()

try:
    string1 = readbytes.decode("utf-8")
except UnicodeError as unicodeError:
    print(unicodeError, file = sys.stderr)
    sys.exit(1)

lines =csv.reader(string1.splitlines()) #list of lists


createtuple = [
    line[7]
    for line in lines
    if "DOG" in line[2]
    ]

print("Count for number of dog bites in each borough from 2015-2017:")

for borough, n in collections.Counter(createtuple).most_common(6):
    print(f"{borough}: {n}")


sys.exit(0)
