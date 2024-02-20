import mysql.connector as  con 
connection = con.connect(host = 'localhost' , user = 'root' , password = 'root' )
cursor = connection.cursor()
cursor.execute("show databases like 'plan'")
check = cursor.fetchall()

#below code will check weather the database is present or not if do it will use it else create new one
if not check:
    cursor.execute("create database plan")
    print("Database not found so created new one !!")    
    cursor.execute("use plan")
    print("Database has been selected!!")   
        
else:
    cursor.execute("use plan")    
    print("Database has been selected!!")   

#database has been selected this far

cursor.execute("CREATE TABLE IF NOT EXISTS list (GoodHabbits VARCHAR(50), BadHabbits VARCHAR(50))")
print("Table 'list' created successfully!!")



def addElement():
    goodThings = []
    badThings = []
    try:
        noOfElements = int(input("Enter how many elemnets you want to add :-  "))
        for i in range(0,noOfElements):
            goodElement = str(input("Enter Good Things :- "))
            goodThings.append(goodElement)
            badElement = str(input("Enter Bad Things :- "))
            badThings.append(badElement)
        
        times = len(goodThings)
        for j in range(0,times):
            sql = 'insert into list(GoodHabbits ,BadHabbits) values(%s,%s)'
            val = (goodThings[j],badThings[j])
            cursor.execute(sql,val)
            connection.commit()
        print("Successfully Entry!!")
        home()
        
    except(ValueError):
        print("You have entered another data type rather than integer .Please restart the code and enter Interger value only!!")
        addElement()

def view():
    cursor.execute("SELECT COUNT(*) FROM list")
    row_count = cursor.fetchone()[0]
    if row_count == 0 :
        print("List is empty!!")
    else:
        cursor.execute("select * from list")
        elements = cursor.fetchall()
        for element in elements:
            print(element)

    home()


def delete():
    try:
        edit = int(input("Press 1 to delete all data \nPress 2 for home page\nPress any other key to exit\nEnter your choice here:- "))
        if edit == 1:
            cursor.execute("delete from list")
            print("All data has been successfully deleted!!")
            connection.commit()
            home()
        elif edit == 2:
            home()
        else:
            exit
        
    except(ValueError):
        print("You have entered another data type rather than integer .Please restart the code and enter Interger value only!!")
        edit()


def home():
    try:
        user = int(input("Press 1 to add Elements \nPress 2 to watch list \nPress 3 to delete the list \nEnter any other key to Exit \nEnter you choice here:- "))
        if user == 1 :
            addElement()
        elif user == 2 :
            view()
        elif user == 3 :
            delete()
        else:
            exit

    except(ValueError):
        print("Enter only Integer value here !!")
        home()



home()