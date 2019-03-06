import pyodbc
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3

connection=sqlite3.connect("IFs.db")

cursor=connection.cursor()

db_file2 = r'C:\Users\Public\Rfiles\IFs.mdb'
user='user'
password = 'data4ifs12'

cnxn = pyodbc.connect('DRIVER=Microsoft Access Driver (*.mdb);DBQ=' + \
                      '{};Uid={};Pwd={};'.format(db_file2, user, password))
cursor=cnxn.cursor()
dict=[]

for row in cursor.tables():
    dict.append(row.table_name)

dict=pd.DataFrame(dict)
dict=dict.iloc[12:]

print(dict)



