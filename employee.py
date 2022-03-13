import sqlite3
from prettytable import PrettyTable

folder = sqlite3.connect("employeedata.db")

listoftables = folder.execute("select name from sqlite_master where type ='table' and name = 'employee' ").fetchall()

if listoftables != []:
    print("Table already exists!")
else:
    folder.execute(''' create table employee(
                   empcode integer primary key autoincrement,
                   name text,
                   phone integer,
                   email text,
                   designation text,
                   salary integer,
                   company text ); ''')
    print("Table is created")

while True:
    print("Select the options in the menu :")
    print("1. Add the Employees ")
    print("2. View All employees ")
    print("3. Search an employee using employee name ")
    print("4. Update an employee details using employee Code ")
    print("5. Delete an employee using employee Code ")
    print("6. Display all the details of employees whose salary is greater than 50000 ")
    print("7. Display the count of total number of employees in the company ")
    print("8. Display all the employee details in alphabetical order, within the specific salary range")
    print("9. Display all the employees data, whose salary is less than the average salary of all the employees ")
    print("10. EXIT ")

    choice = int(input("Enter a option :"))
    if choice == 1 :
        getname = input("Enter the name :")
        getphone = input("Enter the phone :")
        getemail = input("Enter the email :")
        getdesignation = input("Enter the designation :")
        getsalary = input("Enter the salary :")
        getcompany = input("Enter the company :")

        folder.execute("insert into employee(name,phone,email,designation,salary,company)\
                      values('"+getname+"',"+getphone+",'"+getemail+"','"+getdesignation+"',"+getsalary+",'"+getcompany+"')")
        folder.commit()
        print("Data added sucessfully ")

    elif choice == 2:
        result = folder.execute("select * from employee ")
        table = PrettyTable(["emp code","Name","phone","email","designation","salary","company"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

    elif choice == 3:
        getname = input("Enter the name :")
        result = folder.execute("select * from employee where name = '"+getname+"'")
        table = PrettyTable(["emp code", "Name", "phone", "email", "designation", "salary", "company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 4:
        getcode = input("Enter the code :")
        getname = input("Enter the name :")
        getphone = input("Enter the phone :")
        getemail = input("Enter the email :")
        getdesignation = input("Enter the designation :")
        getsalary = input("Enter the salary :")
        getcompany = input("Enter the company :")
        folder.execute("update employee set \
         name = '"+getname+"',phone = "+getphone+",email = '"+getemail+"',designation = '"+getdesignation+"',salary = "+getsalary+",company = '"+getcompany+"' where empcode=" +getcode)
        folder.commit()
        print("updated sucessfully")

    elif choice == 5:
        getcode= input("Enter the emp code ")

        folder.execute("delete from employee where empcode=" +getcode)
        folder.commit()
        print("deleted sucessfully")

    elif choice == 6:
        result = folder.execute("select * from employee where salary > 50000")
        table = PrettyTable(["emp code", "Name", "phone", "email", "designation", "salary", "company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 7:
        result = folder.execute("select count(*) as count from employee")
        table = PrettyTable(["COUNT"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 8:
        loweramount = input("Enter the amount :")
        higheramount = input("Enter the amount :")

        result = folder.execute("select * from employee where salary between "+loweramount+" and "+higheramount+" order by name asc")
        table = PrettyTable(["emp code", "Name", "phone", "email", "designation", "salary", "company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 9:
        result = folder.execute("select * from employee where salary<(select avg(salary) as salary from employee)")
        table = PrettyTable(["emp code", "Name", "phone", "email", "designation", "salary", "company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 10:
        folder.close()
        break
    else:
        print("invalid option !")



























