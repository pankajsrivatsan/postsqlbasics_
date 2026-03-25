import psycopg2

conn= psycopg2.connect(
    host= "localhost",
    database= "postgres",
    user= "postgres",
    password="postgres123"

)
cur= conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id        SERIAL PRIMARY KEY,
            name      VARCHAR(100),
            email     VARCHAR(150),
            age       INT


        )
""")

conn.commit()
print("table created!")

cur.close()
conn.close()
