import pyodbc





cnxn_str = ("DRIVER={SQL Server};"
            "Server=WIN-2K8ESS\WIN2K8ESS;"
            "Database=VideoAcademy;"
            "UID=sa;"
            "PWD=ess@123;")



cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
data = cursor.execute(''' SELECT * FROM projectvideos WHERE id = 12 ''')
# cursor.execute(''' CREATE TABLE new_test(Name nvarchar(50),Age int,City nvarchar(50))''')
# cursor.execute(''' select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='RenderStatus' ''')
# new = cursor.execute('''INSERT INTO new_test(Name, Age,City)VALUES('test', 25, 'test'),('test1', '23','test1')''')
# cnxn.commit()
results = cursor.fetchall()
print(results)
for x in results:
    print(x)

# cnxn.commit()


# for driver in pyodbc.drivers():
#     print (driver)


