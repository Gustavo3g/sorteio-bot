import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bot_instagram",
  database="bot_instagram"
)

mycursor = mydb.cursor()

