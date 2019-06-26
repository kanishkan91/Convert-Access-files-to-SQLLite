#import pyodbc
#import pandas as pd
import numpy as np
from sqlalchemy import create_engine
#import sqlite3
import pip
...


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        from pip._internal import main as pip2
        pip2(['install', package])

install('pydobc')
install('sqlite3')
install('pandas')

import pyodbc
import pandas as pd
import sqlite3



#Read in mdb file here
db_file2 = r'C:\Users\Public\Rfiles\IFsForDyadic.mdb'
user='user'
password = 'data4ifs12'

#Define connection to mdb
cnxn = pyodbc.connect('DRIVER=Microsoft Access Driver (*.mdb);DBQ=' + \
                      '{};Uid={};Pwd={};'.format(db_file2, user, password))
cursor=cnxn.cursor()
dict=[]

#Create dictionary of tables to be imported
for row in cursor.tables():
    dict.append(row.table_name)

datadict=pd.DataFrame(dict)
#Drop unnecessary columns below
datadict=datadict.iloc[14:]
datadict.columns=['Name']

#Create connection to database here
connection=sqlite3.connect("IFsForDyadic.db")
cursor=connection.cursor()

#Start reading in files from access to MySql
for row in datadict['Name']:
    qry = "SELECT * FROM [" + str(row) + "]"
    print(qry)
    data1 = pd.read_sql(qry, cnxn)
    # data1 = pd.melt(data1, id_vars=['Country', 'FIPS_CODE'], var_name='Year', value_name='values')
    data1.to_sql(str(row), con=connection, if_exists="replace", index=False)


#Use below instead when you want all data in one table
#connection=sqlite3.connect("IfsHist.db")

#cursor=connection.cursor()


#for row in datadict['Name']:

#sql_command = """DROP TABLE IF EXISTS ;
#CREATE TABLE SeriesName (
#"Country" primary key,
#"SeriesName" text,
#"Year" Number,
#"Value" Value,
#);"""

#cursor.execute(sql_command)

#sql="INSERT into Series (Year,Values) (%s, %s)"
#val=[FullDataBase['Year'],FullDataBase['Value']]

#cursor.execute(sql,val)

#engine = create_engine('sqlite://', echo=False)
#FullDataBase.to_sql('MyDB',con=engine)



#engine = create_engine('sqlite://', echo=False)
#FullDataBase.to_sql('MyDB',con=engine)







