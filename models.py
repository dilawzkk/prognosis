import sqlite3 as sql

def insertUser(username,password,email,phone,age):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password,email,Contact,Age) VALUES (?,?,?)", (username,password,email,phone,age))
    con.commit()
    con.close()

def retrieveUsers():
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.commit()
    con.close()
    return users

def predic_correct(disid):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    valid="valid"
    cur.execute("UPDATE diseases SET status=? WHERE id=? ",(valid, disid))
    print "updated........................................"
    user = cur.fetchall()
    con.commit()
    con.close()
    return user

def userdetail(username):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users WHERE username=%02s")%username
    user = cur.fetchall()
    con.commit()
    con.close()
    return user
def useralldetail(username):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=\'"+username+"\'")
    user = cur.fetchall()
    con.commit()
    con.close()
    return user
def disdetails(username):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM diseases WHERE username=\'"+username+"\'")
    user = cur.fetchall()
    con.commit()
    con.close()
    return user
def insertdisease(username,disease):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("INSERT INTO diseases(username,disease) VALUES (?,?)",(username,disease))
    con.commit()
    con.close()
def insertbp(username,sys,dis):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute('''UPDATE users SET syst= ?,dias=? WHERE username = ?''', (sys,dis,username))
    con.commit()
    con.close()
def insertsugar(username,fbs,ppbs):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    print fbs
    print "asd"
    cur.execute('''UPDATE users SET FBS= ?,PP=? WHERE username = ?''', (fbs,ppbs,username))
    con.commit()
    con.close()
def insertbloodtest(username,rbc,wbc,tc,neutro,limph,eucino,monocite,platelet):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    print "asd"
    cur.execute('''''''''UPDATE users SET rbc= ?,wbc=?,tc=?, neutro=?, limph=?, eucino=?, monocite=?, platelet=? WHERE username = ?''''''''',                         (rbc,wbc,tc,neutro,limph,eucino,monocite,platelet,username))
    con.commit()
    con.close()

