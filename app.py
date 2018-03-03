from datetime import timedelta
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import models as dbHandler
import os
import nltk
import io
import operator
from magpie import Magpie
import csv
magpie = Magpie()
import speech_recognition as sr
app = Flask(__name__)
@app.route("/")
def home():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	else:
         chatlist=[['sys','Hi,I am Prognosis'],['sysm','Let us hear your problems']]
         session['chatlist']=chatlist
        
         return redirect(url_for('chat'))#first page to display


@app.route("/chat")
def chat():
 i=0
 chatlist=session.get('chatlist')
 username=session.get('username')
 return render_template('chat.html',chatlist=chatlist,username=username)

@app.route("/correctprediction/<int:disid>")
def correctprediction(disid):
    dbHandler.predic_correct(disid)
    return redirect(url_for('profile'))

@app.route("/cured/<int:disid>")
def cured(disid)
    dbHandler.cure(disid)
    return redirect(url_for('profile'))

@app.route("/profile",methods=['POST','GET'])
def profile():
    username=session.get('username')
    userdata=dbHandler.useralldetail(username)
    disdata=dbHandler.disdetails(username)
    print username
    print userdata
    print disdata
    userdata=list(userdata[0])
    if not (userdata[6]==None and userdata[7]==None):
        print "not availabe"
    else:
        print userdata[3]
    if userdata[7]==None:
        print "not availabe"
    else:
        print userdata[7]
    return render_template('profile.html',userdata=userdata,disdata=disdata)

@app.route("/testreports",methods=['POST','GET'])
def testreports():
 if request.method=='POST':
    select=request.form['showform']
    
    if select=='bloodpressure':
        print "bcd"
        sys=request.form['syst']
        dis=request.form['dias']
        username=session.get('username')
        dbHandler.insertbp(username,sys,dis)
        return render_template('testreports.html')    
    if select=='sugartest':
        fbs=request.form['fbs']
        ppbs=request.form['ppbs']
        username=session.get('username')
        dbHandler.insertsugar(username,fbs,ppbs)
        return render_template('testreports.html')   
    if select=='bloodtest':
        rbc=request.form['rbc']
        wbc=request.form['wbc']
        tc=request.form['TC']
        neutro=request.form['neutro']
        limph=request.form['limph']
        eucino=request.form['eucino']
        monocite=request.form['monocite']
        platelet=request.form['platelet']
        username=session.get('username')
        dbHandler.insertbloodtest(username,rbc,wbc,tc,neutro,limph,eucino,monocite,platelet)
        return render_template('testreports.html')  
      
 else:
   return render_template('testreports.html')


@app.route("/speech")
def speech():
 
 
 # Record Audio
 r = sr.Recognizer()
 with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    print("Finished recording")
 
 # Speech recognition using Google Speech Recognition
 try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    #speech=r.recognize_google(audio))
    chatlist=session.get('chatlist')
    print("You said: " + r.recognize_google(audio))
    speak=str(r.recognize_google(audio))
    speak.lstrip('u')
    chat=['user',speak]
    chatlist.append(chat)
    print chatlist
    
    
    noun=nltk.word_tokenize(speak)
    print noun
    f=open('medterm.txt','w')

    for i in range(len(noun)):
      with open('symtom.txt','r') as f1:
        for line in f1:
          for word in line.split():
    	    if noun[i] == word :
    		  f.write(noun[i]+'\n')
    session['chatlist']=chatlist
    count=5
    session['count']=5
    return redirect(url_for('prediction'))
 except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
 except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


@app.route("/prediction",methods=['POST','GET'])
def prediction():
    chatlist=session.get('chatlist')
    count=session.get('count')
    if request.method=='POST':
       message=request.form['message']
       #symlist=message.split(',')
       chatlist.append(['user',message])
       if message=='yes':     
        count=count-1 
        symptom = session.get('sym')
        
        data = []
        with open('medterm.txt','a') as myfile:
            myfile.write(symptom + "\n")
        with open('medterm.txt','r') as myfile:
            for i in myfile.readlines():
                data.append(i)
    diseases = []

    for d in csv.reader(open('disease.csv',"rb")):
	    d_tra=str(d[0:1])
	    d_tra=d_tra[2:-2]
	    diseases.append(d_tra)
    magpie = Magpie(
    keras_model='ModelSave/my/model/here.h5',
    word2vec_model='ModelSave/my/embeddings/here',
    scaler='ModelSave/my/scaler/here',
    labels=diseases
    )
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
    
    if count==0:
        count=count-1
        output=[list(items[0]),list(items[1]),list(items[2])]
        outitem=['sys','You have a high chance of '+output[0][0]+'\n'+'other probable diseases are '+output[1][0] +','+ output[2][0]]
        chatlist.append(outitem)
        session['disease']=[output[0][0],output[1][0],output[2][0]]
        username=session.get('username')
        dbHandler.insertdisease(username,output[0][0])
        dbHandler.insertdisease(username,output[1][0])
        dbHandler.insertdisease(username,output[2][0])
        return render_template('chat.html',chatlist=chatlist,username=username)
        
    import random 
    sym=[]
    for (dis,v) in items[:5]:
     dislist=[]
     diseaselist=[]
     with open("diseasefiles/%02s.csv"%dis) as csvfile:
         for row in csvfile:
            dislist.append(row)
         diseaselist=list(set(dislist)-set(data))
         #print diseaselist   
         for i in range(3):
          secure_random = random.SystemRandom()
          sym.append(secure_random.choice(diseaselist))
            
    srandom = random.randint(0,14) 
    print srandom
    print sym   
    chatlist.append(['sys',"Do you have ?\n" + sym[srandom]])
    session['sym']=sym[srandom]
    session['chatlist']=chatlist
    session['count']=count
    username=session.get('username')
    return render_template('chat.html',chatlist=chatlist,username=username)
    
        
         
    
            
	

@app.route("/register",methods=['POST','GET'])
def register():
   if request.method=='POST':
       username = request.form['username']
       password1 = request.form['password']
       password2=request.form['pass']
       email=request.form['email']
       phone=request.form['phone']
       age=request.form['age']
       if password1==password2:
            dbHandler.insertUser(username, password1,email,phone,age)
            return render_template('index.html')                                                        
   else:
       print "register"
       return render_template('register.html')



@app.route("/login",methods=['POST', 'GET'])
def login():
    
 if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        
        user = dbHandler.retrieveUsers()
        udic=dict( user)
        print udic
        if username not in udic.keys():
            print "no user"
            flash('user not found!')
        elif password==udic[username]:
            print "loggedin"
            session['logged_in'] = True
            session['username'] = username
        else:
            print"wrong pass"
            flash('wrong password!')
        return home()
 else:
        return render_template('index.html')
@app.route("/logout")
def logout():
    session.pop('logged_in',None)
    session.pop('username',None)
    return redirect(url_for('login'))

@app.before_request
def make_session_permanent():
    session.permanent=True
    app.permanent_session_lifetime=timedelta(minutes=30)
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(port=8000,debug = True)
