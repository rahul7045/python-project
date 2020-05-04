import sqlite3

def data1():
	con=sqlite3.connect("data.db")
	curobj=con.cursor()
	curobj.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY,patid text, patfn text,patln text,patdob text,patage text,patgender text,patadd text,patmob text,patdr text)")
	con.commit()
	con.close()

def add(patid, patfn,patln,patdob,patage,patgender,patadd ,patmob,patdr):
	con=sqlite3.connect("data.db")
	cur=con.cursor()
	cur.execute("INSERT INTO data VALUES (NULL,?,?,?,?,?,?,?,?,?)",(patid, patfn,patln,patdob,patage,patgender,patadd ,patmob,patdr))
	con.commit()
	con.close()
	
def view():
	con=sqlite3.connect("data.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM data")
	row=cur.fetchall()
	con.close()
	return row

def delete() :
	con=sqlite3.connect("data.db")
	cur=con.cursor()
	cur.execute("DELETE FROM data where patid=?)",(patid))
	con.commit()
	con.close()
def search():
	con=sqlite3.connect("data.db")
	cur=con.cursor()
	cur.execute("SELECT FROM data where patfn=?)",(patfn))
	rows=cur.fetchall()
	
	
	con.close()
	return rows
	

	
data1()
