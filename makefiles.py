import csv
with open("cleandata.csv") as csvfile:
  csvReader = csv.reader(csvfile)
  for row in csvReader:
        with open("diseasefiles/%02s.csvion"%row[0], 'a') as csv:
          columnTitleRow =row[1]
          csv.write(columnTitleRow + "\n")
