import os
import mysql.connector
from dotenv import load_dotenv

def connectDB():
    load_dotenv()

    mydb = mysql.connector.connect(
      user = "recipeApp",
      password = "cS348!project",
      host = "165.232.138.171",
      database = "main"
    )

    # mydb = mysql.connector.connect(
    #     host =                      os.getenv('DB_HOSTNAME'),
    #     user =                      os.getenv('DB_USER'),
    #     password =                  os.getenv('DB_PASSWORD'),
    #     database =                  os.getenv('DB_NAME')
    # )

    return mydb