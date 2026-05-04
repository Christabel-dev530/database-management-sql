import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="christyluv92!",
    database="customerdb"
)
try:
    
  cursorObject = dataBase.cursor()

  # Correct SQL syntax
  records = "INSERT INTO Customers (Customer_name, Email, Product_name, Product_date, Product_id, Product_price) VALUES (%s, %s, %s, %s, %s, %s)"

  # Use a list of tuples for multiple rows
  values  = [
    ('John Doe', 'johndoe@yahoo.com', 'Milo', '22/02/25', '1', '5000'),
    ('Bon Freight', 'bonfreight@yahoo.com', 'Sugar', '20/02/25', '3', '1700'),
    ('George Shepard', 'georgeshepard@yahoo.com', 'Rice', '21/02/25', '2', '2000'),
    ('Lee Jung', 'leejung@yahoo.com', 'Goldenmorn', '21/02/25', '4', '2800'),
]

  # Execute many records at once
  cursorObject.executemany(records, values)
  # Commit changes
  dataBase.commit()

  print(f"{cursorObject.rowcount} records inserted into Customers table successfully.")
except Exception as e:
  #SQLC.connection.rollback()
  print(f"Error!! either table does not exists or paramter not enough", "error")
finally:
 # finally closing the database connection
  dataBase.close()