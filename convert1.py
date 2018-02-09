import csv
csvFile = open("cleandata.csv", "rb")
csvReader = csv.reader(csvFile)
i=0
for row in csvReader:
    x_tra=str(row[0:1])
    x_tra=x_tra[2:-2]
    y_tra=str(row[1:2])
    y_tra=y_tra[2:-2]
    path = "Directory/" + str(i) + ".lab"
    path1 = "Directory/" + str(i) + ".txt"
    with open(path,"w") as f1:
        f1.write(x_tra)
    with open(path1,"w") as f2:
        f2.write(y_tra)
    print x_tra
    print y_tra
    i+=1
