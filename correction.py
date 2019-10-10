"""
Dog_bites.py
Reported number of dog bites in each borough of NYC from 2015 to 2017.
"""

import sys
import urllib.request
import csv
import collections

#https://data.cityofnewyork.us/Health/DOHMH-Dog-Bite-Data/rsgh-akpg
url = "https://data.cityofnewyork.us/api/views/rsgh-akpg/rows.csv"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

readbytes = infile.read()    #Read whole file into one big sequence of bytes.
infile.close()

try:
    s = readbytes.decode("utf-8")
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

lines = csv.reader(s.splitlines()[1:])   #Skip the first line.

#list of names of boroughs
listOfStrings = [line[7] for line in lines if "DOG" in line[2]]

counter = collections.Counter(listOfStrings)

print("Number of dog bites in each borough from 2015-2017:")
print()

#Alphabetical order, except that "Other" comes last.

for borough in sorted(counter, key = lambda borough: "ZZZZZ" if borough == "Other" else borough):
    print(f"{counter[borough]:5,} {borough}")

sys.exit(0)
