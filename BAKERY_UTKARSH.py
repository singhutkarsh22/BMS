import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()




import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(
    host="localhost", user="root", password="vin07@SIN", database="bank"
)
welc=("Welcome to ARSICAULT BAKERY")
WEL=("***************WELCOME TO ARSICAULT BAKERY***************")
print(WEL)
speak(welc)
mycursor = mydb.cursor()
mycursor.execute("create database if not exists bakery")
mycursor.execute("use bakery")
mycursor.execute("create table if not exists item(p_id varchar(10) PRIMARY KEY, product varchar(30), price int)")
swl="select * from item" 
mycursor.execute(swl) 
rust=mycursor.fetchall()
if rust==[]:
    mycursor.execute("insert into item(p_id, product, price)values(1,'Cake', 850)")
    mycursor.execute("insert into item(p_id, product,price)values(2,'Cookie',200)")
    mycursor.execute("insert into item(p_id, product,price)values(3,'Muffin',150)")
    mycursor.execute("insert into item(p_id, product,price)values(4, 'Pastry',300)")
    mycursor.execute("insert into item(p_id, product,price)values(5,'Viennoiserie',550)")
    mycursor.execute("insert into item(p_id, product,price)values(6,'Bun',60)")  
    mydb.commit()



mycursor.execute("create table if not exists cakes(p_id varchar(11) UNIQUE, varities varchar(25))")
sml="select *from cakes"
mycursor.execute(sml)
rest=mycursor.fetchall()
if rest==[]:
    mycursor.execute("insert into cakes(p_id,varities)values(1,'Molten Chocolate Cake')")
    mycursor.execute("insert into cakes(p_id,varities)values(2,'Gooey Butter Cake')")
    mycursor.execute("insert into cakes(p_id,varities)values(3,'Boston Cream Pie')")
    mycursor.execute("insert into cakes(p_id,varities)values(4,'Ice Cream Cake')")
    mycursor.execute("insert into cakes(p_id,varities)values(5,'Red Velvet Cake')")
    mycursor.execute("insert into cakes(p_id,varities)values(6,'German chocolate cake')")  
    mydb.commit()

mycursor.execute("create table if not exists customer(cust_id BIGINT AUTO_INCREMENT PRIMARY KEY, cust_name varchar(35), mobile BIGINT NOT NULL)")
mycursor.execute("create table if not exists employees(emp_id varchar(10) PRIMARY KEY, e_name varchar(35),salary int,post varchar(30), mobile BIGINT NOT NULL)")
sul="select * from employees"
mycursor.execute(sul)
rist=mycursor.fetchall()
if rist==[]:
    mycursor.execute("insert into employees(emp_id,e_name,salary,post,mobile)values(1,'Emma',15000,'Manager',9876895609)")
    mycursor.execute("insert into employees(emp_id,e_name,salary,post,mobile)values(2,'Olivia',12000,'Pastry Chef',8856001234)")
    mycursor.execute("insert into employees(emp_id,e_name,salary,post,mobile)values(3,'Ava',10000,'Boulanger',7867689956)")
    mycursor.execute("insert into employees(emp_id,e_name,salary,post,mobile)values(4,'Sophia',8000,'Vater',8890948473)")
    mycursor.execute("insert into employees(emp_id,e_name,salary,post,mobile)values(5,'Isabella',8000,'Vater',7784474844)")
    mycursor.execute("insert into employees(emp_id,e_name,salary,post,mobile)values(6,'John',8000,'Vater',8874864843)")  
    mydb.commit()





print("\n\nPLEASE CHOOSE\n1 for Admin\n2 for Costumer\n\n")

choice=int(input("Enter your choise : "))

if choice==1:
    user=input("Enter Your Userid : ")
    pas= input("Enter your Password : ")
    if pas=='pms@1':
        ch=""
        while ch!='N' or ch!='n':
            print("----------------------------------------------------------------------")
            wp=(f"Welcome {user} you are logged in as a Admin")
            speak(wp)
            print(f"!      *****Welcome {user} you are logged in as a Admin******       !")
            print("!      Press 1 for ADD item in the shop                              !")            
            print("!      Press 2 for SEE item in the shop                              !")            
            print("!      press 3 to ADD varities of cake in shop                       !")
            print("!      Press 4 to ADD worker in the shop                             !")
            print("!      Press 5 to SEE worker                                         !")
            print("!      Press 6 to SEE salary of any worker                           !")
            print("!      Press 7 for log out                                           !")            
            print("!--------------------------------------------------------------------!")
            c=int(input("Enter Your Choise : "))
            if c==7:
                print("!-------------------------you are logged out-------------------------!")
                break
            if c==1:
                def addi():
                    p_id= int(input("Enter product id : "))
                    product=input("Enter Product Name : ").strip()
                    price=int(input("Enter Price"))
                    s1= ('insert into item(p_id, product, price)values(%s,%s,%s)')
                    d1= (p_id, product, price)
                    mycursor.execute(s1,d1)
                    mydb.commit()
                    print("******ITEMS ADDED SUCCESSFULLY**********")
                addi()
            elif c==2:
                def see():
                    print("Items in the Shop")
                    lo="select * from item"
                    mycursor.execute(lo) 
                    rust=mycursor.fetchall()
                    t=(['p_id', 'product', 'price'])
                    for p_id, product, price in rust:
                        print(p_id,".","\t",product,"\t",'₹',price)
                see()

            elif c==3:
                def update():
                    p_id= int(input("Enter product id : "))
                    varities=input("Enter CAKE VARITIES Name : ").strip()
                    s1=("insert into cakes(p_id,varities) values(%s,%s)")
                    d1= (p_id,varities)
                    mycursor.execute(s1,d1)
                    mydb.commit()
                    print("*********CAKE VARITIES ADDED SUCCESSFULLY**********")
                update()

            elif c==4:
                def addw():
                    emp_id= int(input("Enter employee id : "))
                    e_name=input("Enter Employee Name : ").strip()
                    salary=int(input("entet employee salary : "))
                    post =input("enter employee position : ").strip()
                    mobile= int(input("enter employee Mobile : "))
                    s1=("insert into employees(emp_id,e_name,salary,post,mobile)values(%s,%s,%s,%s,%s)")
                    d1= (emp_id,e_name,salary,post,mobile)
                    mycursor.execute(s1,d1)
                    mydb.commit()
                    print("*********EMPLOYEE ADDED SUCCESSFULLY**********")
                addw()
            elif c==5:
                def seew():
                    print("Employee in the Shop")
                    lo="select * from employees"
                    mycursor.execute(lo) 
                    rust=mycursor.fetchall()
                    t=(['emp_id','e_name','salary','post','mobile'])
                    print(f"emp_id\te_name\tsalary\tpost\tmobile")
                    for emp_id, e_name, salary, post, mobile in rust:
                        print(f"{emp_id}\t{e_name}\t{salary}\t{post}\t{mobile}")
                seew()

            elif c==6:
                def sal():
                    mycursor = mydb.cursor()
                    emp_id=int(input("Enter Employee id : "))
                    s2=(f"SELECT * FROM employees WHERE emp_id={emp_id}")
                    mycursor.execute(s2)
                    detail = mycursor.fetchone()
                    print(f"emp_id\te_name\tsalary\tpost\tmobile")
                    print(f"{detail}\t")
                sal()
    else:
        print("!----------------------------------------------------------------------!")
        print("!       authentication problem please enter correct password           !")
        print("!----------------------------------------------------------------------!")
elif choice==2:
    cust_name=input("enter your name : ")
    mobile =int(input("enter your mobile no :"))
    s1=("insert into customer(cust_id,cust_name,mobile) values(NULL,%s,%s)")
    d1= (cust_name,mobile)
    mycursor.execute(s1,d1)
    mydb.commit()
    ch=""
    while ch!='N' or ch!='n':
        pyo=(f"Welcome {cust_name}")
        speak(pyo)
        print(" !----------------------------------------------------------------------!")
        print(f"!                   *****Welcome {cust_name}******                     !")
        print(" !                   Press 1 for SEE MEENU in the shop                  !")            
        print(" !                   Press 2 for order item in the shop                 !")
        print(" !                   Press 3 for log out                                !")                     
        print(" !----------------------------------------------------------------------!")
        co=int(input("Enter you choice : "))
        if co==1:
            def seeq():
                lo="select * from item"
                mycursor.execute(lo) 
                rust=mycursor.fetchall()
                t=(['p_id', 'product', 'price'])
                print("************Items in the Shop************\n")
                for p_id, product, price in rust:
                    print(f"{p_id}\t{product}\t₹{price}")
            seeq()
        elif co==3:
            print(f"!----------{cust_name} you are log out------------!")
            break
        elif co==2:
            lo="select * from item"
            mycursor.execute(lo) 
            rust=mycursor.fetchall()
            t=(['p_id', 'product', 'price'])
            print("************Items in the Shop************\n")
            for p_id, product, price in rust:
                print(f"{p_id}\t{product}\t₹{price}")
            lo="select * from item"
            c=(lo) 
            rust=mycursor.fetchall()
            print(rust)
            l=[]
            for i in range(len(rust)):
                l.append(rust[i][0])
            p_lid= int(input("Enter Product id : "))
            query = f"SELECT price FROM item WHERE p_id = {p_lid}"
            mycursor.execute(query)
            result = mycursor.fetchone()
            bil=(result[0])

            query = f"SELECT p_id FROM item WHERE p_id = {p_lid}"
            mycursor.execute(query)
            ui= mycursor.fetchone()
            uid=(ui[0])
            uuu=int(uid)

            query = f"SELECT product FROM item WHERE p_id = {p_lid}"
            mycursor.execute(query)
            ni= mycursor.fetchone()



            if p_lid==1:
                print("which cake do you want? ")
                kl="select * from cakes"
                mycursor.execute(kl)
                rut=mycursor.fetchall()
                f=(['p_id','varities'])
                for p_id, varities in rut:
                    print(f"{p_id}\t\t{varities}")
                print("Choose which cake do you want?")
                ck= int(input("enter product id: "))
                puery = f"SELECT varities FROM cakes WHERE p_id={ck}"
                mycursor.execute(puery)
                resu = mycursor.fetchone()
                query = f"SELECT p_id FROM cakes WHERE p_id = {ck}"
                mycursor.execute(query)
                mi= mycursor.fetchone()
                ud=(mi[0])
                vivo=int(ud)
                if ck==vivo:
                    print(f"how many Quantity of {resu[0]} Cake do you want ? ")
                    qty= int(input("Enter qty :"))
                    print(f"You have successfully order your {resu[0]} ")
                    def bills():
                       print("        You have successfully order your item            !")
                       print(f"!------------------{cust_name}'s bill-------------------!")
                       print(f"!------------------{datetime.now()}-------!")
                       print(f"!------the total amount is ₹{bil*qty}-------------------!")
                       print(f"!-------Thank You, Have A Nice Day----------------------!")
                    bills()
                else:
                    print("Please Choose Correct option")   
            elif p_lid==uuu:
                print(f"how many Quantity of {ni[0]} do you want ? ;")
                qty= int(input("Enter qty :"))
                print(f"      You have successfully order your {ni[0]} ")
                print(f"!------------------{cust_name}'s bill-------------------!")
                print(f"!------------------{datetime.now()}-------!")
                print(f"!------the total amount is ₹{bil*qty}-------------------!")
                print(f"!-------Thank You, Have A Nice Day----------------------!")
            else:
                    print("Please Choose Correct option")          
        else:
            print("Please Choose Correct option")

else:
        print("Please Choose Correct option")                           
                        
        