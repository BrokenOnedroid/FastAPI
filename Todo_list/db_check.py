import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM todos')

# Fetch and print results
rows = cursor.fetchall()
for row in rows:
    print(row)
if rows.count == 0:
    print("empty")
print("finished")



# Close the connection
conn.close()