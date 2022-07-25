import mysql.connector
import tabulate
from datetime import date
def displayAll():
    cur.execute("select * from students")
    res = cur.fetchall()
    heading=["PRN", "FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "ADDRESS", "MOBILE", "EMAIL","DOB"]
    if len(res[0])==9:
        heading.append("CGPA")

    print(tabulate.tabulate(res, headers=heading))

def dispNameAge():
    cur.execute("select FIRST_NAME, MIDDLE_NAME, LAST_NAME,DOB from students")
    res =cur.fetchall()
    todays_date=date.today()
    nameAge=[]
    for i in res:
        name=i[0]+' '+i[1]+' '+i[2]
        age=todays_date-i[-1]
        days=age.days//365
        nameAge.append((name,days))
    print(tabulate.tabulate(nameAge,headers=["Name","Age"]))


def addata():
    prn=input(("Enter PRN:"))
    fn=input(("Enter Firstname:"))
    mn=input(("Enter Middlename:"))
    ln=input(("Enter Lastname:"))
    adrs=input(("Enter Address:"))
    mob=input(("Enter mobile.no:"))
    email=input(("Enter Email"))
    dob=input(("Enter DOB:"))
    cur.execute("insert into students values('{}','{}','{}','{}','{}','{}','{}','{}')".format(prn,fn,mn,ln,adrs,mob,email,dob))
    mycon.commit()

def deldata():
    prn=input("Enter prn to be deleted:")
    cur.execute("delete from students where prn = "+prn)
    mycon.commit()

def upstudent():
    prn = input("Enter prn:")
    mob = input(("Enter mobile.no:"))
    email = input(("Enter Email:"))
    cur.execute("update students set MOBILE='{}' , EMAIL='{}' where PRN='{}'".format(mob,email,prn))
    mycon.commit()

def addcgpa():
    cur.execute("desc students;")
    r=cur.fetchall()
    if len(r)==8:
        cur.execute("alter table students add column CGPA float")
        mycon.commit()
        print("\n CGPA field added successfully...\n")
        cur.execute("select prn from students")
        x=cur.fetchall()
        for i in x:
            prn=i[0]
            print("enter CGPA of PRN",prn,end=': ')
            cgpa=float(input())
            cur.execute("update students set CGPA ='{}' where PRN='{}'".format(cgpa,prn))
            mycon.commit()
    else:
        print("\n CGPA field already exist\n")

def functions():
    print('''
            1. Display the database
            2. Display name and age of all students
            3. Add record 
            4. Delete a record
            5. Update email and Phone number
            6. Add column CGPA
            Enter any other key to exit
    ''')

if __name__ == "__main__":
    print("Welcome to DBATU Second year Computer Engineering Department")
    print("--" * 30)
    mycon = mysql.connector.connect(host="localhost", user="root", password="ruddhi", database="comp_sy_dbatu")
    cur = mycon.cursor()
    global flag
    flag = False
    try:
        cur.execute("ALTER TABLE STUDENTS DROP COLUMN CGPA")
    except:
        pass
    flag = True
    if mycon.is_connected():
        functions()
        while True:
            opt = input("Select your choice(h for help): ")
            if opt == '1':
                displayALl()
            elif opt == '2':
                dispNameAge()
            elif opt == '3':
                addata()
            elif opt == '4':
                deldata()
            elif opt == '5':
                upstudent()
            elif opt == '6':
                flag = addcgpa()
            elif opt in 'hH':
                functions()
            else:
                break
    else:
        print("Unable to connect to MySQL")


