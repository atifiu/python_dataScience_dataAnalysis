import cx_Oracle
username = 'arup'
password = 'arup'
#dbname =   '192.168.29.71:1521/testpdb1.localdomain'
dbname =   'testpdb1'
#dsn = "testpdb1"
#encoding="UTF-8"
#con = cx_Oracle.connect(username,password,dbname)
dsn_tns = cx_Oracle.makedsn('192.168.29.71', '1521', service_name = 'testpdb1.localdomain') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
con = cx_Oracle.connect(user = "arup", password = "arup", dsn = dsn_tns, encoding="UTF-8")
print(con.version)
cursor = con.cursor()
#cursor.execute('CREATE TABLE A1(c1 number, c2 number)')
statement1 = ('insert  into a1(c1, c2) values(1, trunc(dbms_random.value( 1,100000)))')
cursor.execute(statement1,)
con.commit()