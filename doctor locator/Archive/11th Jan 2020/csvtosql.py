import sqlite3,csv

connection = sqlite3.connect('doctor.db')
with open ('hospitals_directory.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader) 
    query = 'insert into hospital_location({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    cursor = connection.cursor()
    for data in reader:
        cursor.execute(query, data)
    connection.commit()
