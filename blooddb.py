import mysql.connector

class Blood_bank:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',password='groot2515',host='localhost',database='blood_db'
        )
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("successfully connected")

    def get(self):
        query="select * from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        return records


    def post(self,name,b_grp,phone,city,l_d):
        query="insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
        data=(name,b_grp,phone,city,l_d)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("successfully created")

    def get_by_id(self, id):
        query = "select * from donor where id=%s"
        self.cursor.execute(query, (id,))
        record = self.cursor.fetchone()
        # if record:
        #     print("book Details:", record)
        # else:
        #     print("details not found.")
        return record

    def delete(self, id):
        query="delete from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0: #if no updations rowcount returns 0
            # print("data is deleted")
            return True
        else:
            # print("no record found")
            return False


