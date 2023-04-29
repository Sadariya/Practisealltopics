import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='user_input')
    print("Database connected!")
except Exception as e:
    print(e)

cur = dbcon.cursor()

tbnm=input("Enter table name:")
create_tbl=f"create table {tbnm} (id integer primary key,name text,sub text)"
try:
    cur.execute(create_tbl)
    print("Table Created!")
except Exception as e:
    print(e)

# Inset Data
n=int(input("Enter number of records:"))
for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stsub=input("Enter Subject:")

    insert_data=f"insert into {tbnm} values({stid},'{stnm}','{stsub}')"
    try:
        cur.execute(insert_data)
        dbcon.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)


a = input ('do you want to delete table data "Yes" or "NO" : ')

if a == 'YES':
    Delete_data = f"truncate {tbnm}"

    try:
        cur.execute(Delete_data)
        dbcon.commit()
    except Exception as e:
        print (e)