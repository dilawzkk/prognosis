from magpie import Magpie

import csv
magpie = Magpie()
magpie.init_word_vectors('Data/Directory', vec_dim=100)
#magpie.train_word2vec('Data/Directory', vec_dim=100)


#magpie.fit_scaler('Data/Directory')
diseases = []

for d in csv.reader(open('disease.csv',"rb")):
	d_tra=str(d[0:1])
	d_tra=d_tra[2:-2]
	diseases.append(d_tra)


#for d in csv.DictReader(open('disease.csv'), delimiter='\t'):
    #counts.append(int(d['Counts']))

#print ('Counts = ', counts)
#magpie.train('Data/Directory', diseases , epochs=3)



#magpie.save_word2vec_model('ModelSave/my/embeddings/here')
#magpie.save_scaler('ModelSave/my/scaler/here', overwrite=True)
#magpie.save_model('ModelSave/my/model/here.h5')
magpie = Magpie(
   keras_model='ModelSave/my/model/here.h5',
   word2vec_model='ModelSave/my/embeddings/here',
   scaler='ModelSave/my/scaler/here',
   labels=diseases
)
#in loop
import io
import operator
dictionary={}
dict1={'influenza':0}
data = []
with io.open('medterm.txt', encoding='latin-1') as myfile:
    for i in myfile.readlines():
        data.append(i)
for i in range(len(data)):
  dictionary= magpie.predict_from_text(data[i])
  dictionary=dict(dictionary)
  #dictionary.sort() 
  dict1 = {key: dict1.get(key, 0) + dictionary.get(key, 0) for key in set(dict1) | set(dictionary)}
#sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(0),reverse=True)
items = [(v, k) for k, v in dict1.items()]
items.sort()
items.reverse()
items = [(k, v) for v, k in items] 
print items

for (dis,v) in items[:5]:
   with open("diseasefiles/%02s.csv"%dis) as csvfile:
     sym=csvfile.readlines()[0:3]
     print sym   

#print magpie.predict_from_text('pleuritic pain')
#print magpie.predict_from_text('vomiting')
#[('label1', 0.96), ('label3', 0.65), ('label2', 0.21)]

