# define a class to perform db operation on book table
# create a class named BookListCreateRetrieveUpdateDelete
# and define methods
# list() --->for reading all records
# create() --->for creating a new record
# retrieve() --> for reading a specific record
# update(id,data) -->for updating a specific rec
# delete(id)

import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",password="root",host="localhost",database="library_db"
        )
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")
    def list(self):
        query = "select * from book"
        self.cursor.execute(query)

        records = self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
                return records
        else:
            print("no records found")

    #
    # def create(self,title,author,price,pages,language):
    #
    #     query="insert into book(title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
    #     data=(title,author,price,pages,language)
    #     self.cursor.execute(query,data)
    #     self.connection.commit()
    #     print("data inserted successfully")

    def create(self, title, author, price, pages, language):

        # Check if the book already exists
        check_query = """
        SELECT * FROM book
        WHERE title=%s AND author=%s AND price=%s
        AND pages=%s AND language=%s
        """

        data = (title, author, price, pages, language)

        self.cursor.execute(check_query, data)

        if self.cursor.fetchone():
            print("Book already exists")
            return False

        # Insert new book
        query = """
        INSERT INTO book(title, author, price, pages, language)
        VALUES(%s, %s, %s, %s, %s)
        """

        self.cursor.execute(query, data)
        self.connection.commit()

        print("Data inserted successfully")
        return True


    def retrieve(self,id):

        query = "select * from book where id=%s"
        self.cursor.execute(query, (id,))
        record = self.cursor.fetchone()
        if record:
            return(record)
            # print("book Details:", record)
        else:
            print("details not found.")
    #
    # def update(self,id):
    #     pass

    def delete(self, id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:#if no updations rowcount returns 0
            # print("data is deleted")
            return True
        else:
            # print("no record found")
            return  False

    def update(self,id,title,author,price,pages,language):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0: #if no updations rowcount returns 0
            # print("data is updated")
            return True
        else:
            # print("no record found")
            return False

book_instance=BookListCreateRetrieveUpdateDelete()
book_instance.list()
# book_instance.create("stu","arun",400,500,"malayalam")
# book_instance = BookListCreateRetrieveUpdateDelete()


# book_instance.create(
#     "The Alchemist",
#     "Paulo Coelho",
#     400,
#     250,
#     "English"
# )
# book_instance.retrieve(2)
# book_instance.delete(2)
# book_instance.update(1,"heart","abhi",400,350,"english")