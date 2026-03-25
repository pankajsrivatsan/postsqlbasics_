import psycopg2

conn= psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres123"


)

cur= conn.cursor()
print("connected successfully!")

cur.close()
conn.close()
