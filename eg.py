import csv
disease = []
for d in csv.reader(open('disease.csv',"rb")):
	d_tra=str(d[0:1])
	d_tra=d_tra[2:-2]
	disease.append(d_tra)

print disease
