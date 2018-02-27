import sqlite3 as sql

def insertUser(username,password,email):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password,email) VALUES (?,?,?)", (username,password,email))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("prognosisdb.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users
def userdetail(username):
    con = sql.connect("prognosisdb.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users WHERE username=%02s")%username
    user = cur.fetchall()
    con.close()
    return user
