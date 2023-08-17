import pymysql

connector = pymysql.connect(
    host='localhost',
        user='root', 
        password = "1234",
        db='dia',
) 

cur = connector.cursor()
cur.execute('select * from dia.diabetes_prediction_dataset')
output = cur.fetchall()
column_names = [description[0] for description in cur.description]
print("Column Names:", column_names)

print(type(output))
