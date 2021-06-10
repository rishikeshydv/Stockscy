import mysql.connector

class dbms(object):
    def __init__(self):
        self.create_connection()
        self.create__table()
    def create_connection(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='rANJUYADAv@123',
            database='my_data'
            )
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS data_table """)
        self.curr.execute("""create table data_table(
            Name text,
            Price text
            ) """)
    def process(self,item,spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""insert into data_table values (%s,%s,%s)""",(
            item['Name'][0],
            item['Price'][0]
            ))
        self.conn.commit()
        self.conn.close()
        
       
        