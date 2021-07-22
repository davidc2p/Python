import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.;'
                      'Database=RC_APP;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM RC_APP..Account')

for row in cursor:
    print(row)