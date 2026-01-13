import pandas as pd
import mysql.connector as sql



conn=sql.connect(host='Localhost',user='root',passwd='ppraktan',database='Railway')
if conn.is_connected():
    print('Successfully connected')
    c1=conn.cursor()
    c1.execute("create table if not exists passengers(pname varchar(30), age varchar(25),trainno varchar(30),noofpas varchar(25),cls varchar(30),destination varchar(25),amt varchar(30),status varchar(25),pnrno varchar(30))")
    print('Table Passengers created')

def menu():
    print()
    print(  "    RAILWAY RESERVATION SYSTEM   ")
    print()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print()
    
    #print("1. Create Table Passenger")
    print("1. Add new  Passenger Detail")
    print("2. Add new in Train Detail")
    print("3. Train Deatils")
    print("4. Passengers Table")
    print("5. Show PNR NO. ")
    print("6. Reservation of Ticket")
    print("7. Exit:")

#def create_passengers():

    
def add_passengers():
    c1=conn.cursor()       
    L=[]
    pname=input("Enter Name:")
    L.append(pname)
    age=input("Enter AGE:")
    L.append(age)
    trainno=input("Enter TRAIN NO.:")
    L.append(trainno)
    noofpas=input("Enter NO. Of Passengers:")
    L.append(noofpas)
    cls=input("ENTER CLASS:")
    L.append(cls)
    destination=input("ENTER DESTINATION:")
    L.append(destination)
    amt=input("ENTER FARE:")
    L.append(amt)
    status=input("Enter status:")
    L.append(status)
    pnrno=input("ENTER pnrno (Disclaimer: PNRno must be at least 5 characters, start with a letter):")
    L.append(pnrno)
    pas=(L)
    sql="insert into passengers(pname,age,trainno,noofpas,cls,destination,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,pas)
    conn.commit()
    print('Record of Passenger inserted')
    df=pd.read_sql("select * from passengers",conn)
    print(df)
    

    
def add_traindetail():
    c1=conn.cursor()
    df=pd.read_sql("select * from traindetail",conn)
    print(df)
    L=[]
    tname=input("ENTER TRAIN NAME :")
    L.append(tname)
    tnum=input("ENTER NUMBER OF TRAIN :")
    L.append(tnum)
    source=input("ENTER SOURCE OF TRAIN :")
    L.append(source)
    destination=input("ENTER DESTINATION OF TRAIN :")
    L.append(destination)
    fare=input("ENTER FARE OF STATION :")
    L.append(fare)
    ac1=input("ENTER No. OF SEATS FOR AC1 :")
    L.append(ac1)
    ac2=input("ENTER No. OF SEATS FOR AC2 :")
    L.append(ac2)
    slp=input("ENTER No. OF SEATS FOR SLEEPER :")
    L.append(slp)
    f=(L)
    sql="insert into traindetail(tname,tnum,source,destination,fare,ac1,ac2,slp)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    conn.commit()
    print('Record inserted in Trains Details')
    
    

def showtrainsdetail():
    print('Trains Details')
    df=pd.read_sql("select * from traindetail",conn)
    print(df)
    
    
    
    
    
def showpassengers():
    print('Passengers detail')
    df=pd.read_sql("select * from passengers",conn)
    print(df)
    
    
def disp_pnrno():
    print("PNR STATUS WINDOW")
    a=(input("Enter Train No. :  "))
    qry="select pname,status from passengers where trainno=%s;"%(a,)
    df=pd.read_sql(qry,conn)
    print(df)
    
    
    
    
def ticketreservation():
    print ("WE HAVE THE FOLLOWING SEAT TYPES FOR YOU:-")
    print ("TNAME IS 1 FOR GOA EXPRESS FROM MUMBAI:-")
    print()
    print ("1. FIRST CLASS AC RS 7000 PER PERSON")
    print ("2. SECOND CLASS AC RS 5000 PER PERSON")
    print ("3. THIRD CLASS AC RS 4000 PER PERSON")
    print ("4. FOR SLEEPER CLASS AC RS 4500 PER PERSON")
    print()
    print("TNAME IS 2 FOR JAMMU EXPRESS FROM DELHI:-")
    print()
    print ("1. FIRST CLASS AC RS 11000 PER PERSON")
    print ("2. SECOND CLASS AC RS 15000 PER PERSON")
    print ("3. THIRD CLASS AC RS 8000 PER PERSON")
    print ("4. FOR SLEEPER CLASS AC RS 8500 PER PERSON")

    try:
        trainname = int(input("ENTER YOUR CHOICE OF TRAIN NAME PLEASE->"))
        x = int(input("ENTER YOUR CHOICE OF TICKET PLEASE->"))
        n = int(input("HOW MANY TICKETS DO YOU NEED:"))
    except ValueError:
        print("Invalid numeric input")
        return

    if trainname == 1:
        prices = {1:7000, 2:5000, 3:4000, 4:4500}
    elif trainname == 2:
        prices = {1:11000, 2:15000, 3:8000, 4:8500}
    else:
        print("PLEASE CHOOSE A VALID TRAIN")
        return

    if x not in prices:
        print("Invalid ticket option")
        return

    s = prices[x] * n
    print(f"YOU HAVE Chosen option {x}")
    print("your TOTAL TICKET PRICE IS =", s, "\n")


    

while True:
    opt=""
    print()
    menu()
    opt=int(input("Enter your choice : "))
    
    #if opt==1:
        #create_passengers()
    if opt==1:
        add_passengers()    
    elif opt==2:
        add_traindetail() 
    elif opt==3:
        showtrainsdetail()
    elif opt==4:
        showpassengers() 
    elif opt==5:
        disp_pnrno()
    elif opt==6:
        ticketreservation()
    elif opt==7:
        print("Thank You!!")
        break
        
    
    else:
        print('invalid option')
        
conn.close() 
    
    