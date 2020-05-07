import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db) #standard connection seq
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts(id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM PARTS")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES(Null, ?, ?, ?, ?)", (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ?"
                         "WHERE id = ?", (part, customer, retailer, price, id))
        self.conn.commit()

    #add a destructor method
    def __del__(self):
        self.conn.close()

#Instantiate the db  #install sql lite studio to view #not complusory
#
# db = Database('store.db')
# db.insert('4gb DDR4A RAM','John DOE','Microcenter','160')
# db.insert('4gb DDR4A RAM','Joe KING','Microcenter','165')
# db.insert('ASUZ MBOD','Joe KING','Microcenter','220')
# db.insert('Power Unit','Henry LIU','Newegg','120')

#At the end run the file in the terminal
#py db.py
#this creates the database file 'store.db'
#after first run, remember to comment out