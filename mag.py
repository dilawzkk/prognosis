from magpie import Magpie

import csv
magpie = Magpie()
#magpie.init_word_vectors('Data/Directory', vec_dim=100)
#magpie.train_word2vec('data/hep-categories', vec_dim=100)


#magpie.fit_scaler('data/hep-categories')
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
print magpie.predict_from_text('pleuritic pain')

#[('label1', 0.96), ('label3', 0.65), ('label2', 0.21)]

