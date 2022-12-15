import uuid
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="CampUs"

)

mycursor = db.cursor()


def addUser(Fname:str ,Lname:str , phone:str):
    userid = str(uuid.uuid4())
    created_at = datetime.now()
    mycursor.execute("INSERT INTO user(userID,Fname,Lname,phone,created_at) VALUES (%s,%s,%s,%s,%s)",(userid,Fname,Lname,phone,created_at))
    db.commit()