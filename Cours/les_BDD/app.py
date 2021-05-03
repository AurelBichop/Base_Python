import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute(""" 
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text) 
""")

""" d= {"prenom":"Aurel","nom":"BICHOP"}
c.execute("INSERT INTO employees VALUES (:prenom, :nom)", d) """

c.execute("SELECT * FROM employees")
donnees = c.fetchall()
print(donnees)

donnees = c.fetchall()
print(donnees)


conn.commit()
conn.close()
