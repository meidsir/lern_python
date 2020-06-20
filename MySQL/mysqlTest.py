import MySQLdb

db = MySQLdb.connect("localhost","root","root123","world",charset='utf8')

cursor = db.cursor()
cursor.execute("select * from world.city where id=1293 ")

data = cursor.fetchone()

print (data)

db.close()