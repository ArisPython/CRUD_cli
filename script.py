# connection setting
DB_HOST = "127.0.0.1"
DB_NAME = "employee"
DB_USER = "aris"
DB_PASS = "aris1985"

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST )

#--- setting output cursor ---
# cur = conn.cursor() #--> output tupple
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #--> output dict

# -- NEW TABLE --
# cur.execute("CREATE TABLE employee_cli_test (id SERIAL PRIMARY KEY, name VARCHAR);")

# -- CREATE --
# cur.execute("INSERT INTO employee_cli_test (name) VALUES(%s)", ("Andi Matovani",))

# -- READ --
# cur.execute("SELECT * FROM employee_cli_test;")
# print(cur.fetchall())

cur.execute("SELECT * FROM employee_cli_test WHERE id =%s;",(1,))
# print(cur.fetchone())
print(cur.fetchone()['name'])

conn.commit()

cur.close()


conn.close()