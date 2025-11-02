#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)
    major_year = makeMajorYear(major, year)
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)
    #print(student_id)
    print(output, end="")


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + idNum[idLen - 3:]

  #print(id)
  return id

def makeMajorYear(major, year):
  # First 3 letters of major (no spaces)
  major_code = major[:3].upper()

  # Convert full year word to abbreviation
  if year.lower().startswith("fresh"):
    year_code = "FR"
  elif year.lower().startswith("soph"):
    year_code = "SO"
  elif year.lower().startswith("jun"):
    year_code = "JR"
  elif year.lower().startswith("sen"):
    year_code = "SR"
  else:
    year_code = year[:2].upper()

  return major_code + "-" + year_code

if __name__ == '__main__':
  main()
