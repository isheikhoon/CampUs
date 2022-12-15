import uuid
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="campus",
    database="CampUs"

)

mycursor = db.cursor()


def addUser(Fname:str ,Lname:str , phone:str):
    user = mycursor.execute("select * from user where phone = %s",(phone))
    if user is None:
        return "the user already signup"
    else:
        userid = uuid.uuid4()
        created_at = datetime.now()
        mycursor.execute("INSERT INTO user(userID,Fname,Lname,phone,created_at) VALUES (%s,%s,%s,%s,%s)",(userid,Fname,Lname,phone,created_at)) 
        db.commit()
    return "user signup successfuly"
