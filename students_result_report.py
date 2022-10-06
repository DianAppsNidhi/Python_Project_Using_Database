import mysql.connector

con = mysql.connector.connect(host = "localhost", password ="winserver" , user = "root", port = 3306, database = "Student_Records")
# print(con)



def check_student_Rollno(student_id):
    sql = 'select * from Students where Rollno = %s'
    c = con.cursor(buffered=True)
    data = (student_id,)

    
    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False    



def add_student_record():
    Rollno = int(input("enter the roll no: "))
    
    if (check_student_Rollno(Rollno) == True):
        print("You are adding the registered  roll no \n Please make entry with new roll no")
        home_page()

    else:
        print("Fill the details of{Rollno} ")
        Name = input("Enter your name  : ")
        Total_Marks = int(input("Enter Total_Marks   : "))
        Obtain_Marks = int(input("Enter Obtain Marks  : "))
        data = (Rollno ,Name, Total_Marks, Obtain_Marks)

        sql = 'insert into Students  values (%s, %s, %s, %s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Your details has been added successfully")
        home_page()

def update_student_record():
    Rollno = int(input("Enter student roll no"))

    if (check_student_Rollno(Rollno) == False):
        print("You are checking the wrong student id") 
        home_page()

    else:
        Obtain_Marks = (input("Update marks of roll no "))
        sql = 'update  Students set Obtain_Marks = %s  where  Rollno = %s'
        data = (Obtain_Marks, Rollno)

        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Marks  has been updated")
        home_page()

def remove_student_record():
    Rollno = int(input("Enter student roll no "))

    if (check_student_Rollno(Rollno) == False):
        print("You are trying to delete the unexisting record")
        home_page()

    else:
        sql = 'delete from Students where Rollno=%s'
        #print(sql)
        data = (Rollno,)
        print(data)

        c = con.cursor()
        c.execute(sql, data)
        
        con.commit()
        print("Your record   has been deleted" )
        home_page()

        
        
def display_student_record():
    print("Displat Students Records")
    sql = 'select * from Students'
    c  = con.cursor()
    c.execute(sql)

    r  = c.fetchall()
    for i in r:
        print("student roll no: ", i[0])
        print("student Name: ", i[1])
        print("student Total Marks: ", i[2])
        print("student Obtain Marks: ", i[3])

    press = input("Press Any key To Continue..")
    home_page()    


        

def search_student():
    Rollno = int(input("Enter student roll no "))
    
    if(check_student_Rollno(Rollno) == False):
        print("student Record Not exists\nTry Again")
        press = input("Choose Any number To Continue..")
        home_page()
    else:
        
        sql = 'select * from Students where Rollno = %s'
        data = (Rollno,)
        c = con.cursor()
        
        
        c.execute(sql, data)    

        r = c.fetchall()
        print(r)
        home_page()


        

def home_page():
 print("Students Exam Repots portal")
 print("Choose Below Numbers  to Update ")
 print("1 to Add Student")
 print("2 to Remove Student ")
 print("3 to Update Student")
 print("4 to Display Student")
 print("5 to Search_Student")


 chose_number = int(input("Enter your Choice : "))
 if chose_number == 1:
  add_student_record()
 elif chose_number == 2:
  remove_student_record()
 elif chose_number == 3:
  update_student_record()
 elif chose_number == 4:
  display_student_record()
 elif chose_number == 5:
  search_student()
 elif chose_number ==6:
    exit(0)
 else:
  print("Invalid Choice, please choose another one")
  home_page()




home_page()

