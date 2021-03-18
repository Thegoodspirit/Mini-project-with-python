import os
import sqlite3

os.chdir('C://Users/evil1/Desktop/python/project/login and sigin system with python and mysqlite3')

def database(con,d):
    cobj=con.cursor()
    cobj.execute(' INSERT INTO info ( first_name ,last_name , age , username , password  ) VALUES(?,?,?,?,?)',d)
    con.commit()

def signin(con):
    
    fn = str(input(" Enter the first name :-"))
    data.append(fn)
    ln = str(input("entrer the last name :- "))
    data.append(ln)
    ag = int(input("enter you age :-"))
    data.append(ag)
    u = str(input("Enter the username:- "))
    data.append(u)
    p = str(input("enter you passwoerd:- "))
    data.append(p)
    database(con,data)
    

def login(con):
    cobj=con.cursor()
    data1=[]
    print("\n")
    print("enter the your username or password to login")
    u1 = str(input("enter your username:- "))
    p1 = str(input("enter your password:- "))
    data1.append(u1)
    data1.append(p1)
    cobj.execute(''' SELECT * FROM info ''')
    record =  cobj.fetchall()
    data1 = set(data1) 
    for row in record:
        r = set(row)
        if data1.issubset(r):
            print("login successful")
            break
    else:
        print("try again")
        c = str(input("if you want to login again choies (y or n) :-"))
        if c == 'y':
            print("\n")
            print("create you account ")
            return signin(con)
        else:
            print("thanks have a nice day")
            exit



print("welcome to balbla company :- ")
data = []
u = []
p = []
con = sqlite3.connect('database.db')
flag = 0
print("1. sign in")
print("2. login ")
flag=int(input("Enter your choies ( 1 or 2 ) :- "))
if flag == 1:
    print("\n")
    print("create you account ")
    signin(con)
else:
    login(con)
con.close()