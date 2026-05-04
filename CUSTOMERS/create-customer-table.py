# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="christyluv92!",
  database = "customerdb"
)
def showtables():
  
  cursorObject = dataBase.cursor()
  cursorObject.execute("SHOW TABLES")
  for i in cursorObject:
    if len(i)>0:
      
      print(i)
    else:
      print("no tables to display")  
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table a

Records = """CREATE TABLE Customers(
             Customerid INT NOT NULL AUTO_INCREMENT,
             Customer_name VARCHAR(500) NOT NULL,
             Email VARCHAR(500) NOT NULL,
             Product_name VARCHAR(500) NOT NULL,
             Product_date VARCHAR(500) NOT NULL,
             Product_id VARCHAR(500) NOT NULL,
             Product_price VARCHAR(500) NOT NULL,
             PRIMARY KEY (Customerid)
                   )"""


# table created
cursorObject.execute(Records) 
print("Customers table created successfully")
showtables()
# disconnecting from server
dataBase.close()