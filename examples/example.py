import xml.etree.ElementTree as ET
import xmldataset
import psycopg2
from sqlalchemy import create_engine
import pprint
import datetime
import pandas as pd
from pandas import DataFrame,read_csv
ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
from datetime import datetime



xml_data = open('Vmax_svpg.xml').read()




# for Vmax_svpg

profile="""
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:mydata
            Masking_View
                View_Info
                    view_name = dataset:mydata
                    view_last_update_time = dataset:mydata
                    port_grpname = dataset:mydata
                    port_info
                        Director_Identification
                            director = dataset:mydata
                            port = dataset:mydata
                            port_wwn = dataset:mydata
       """

#=========================================================



output = xmldataset.parse_using_profile(xml_data,profile)

df = pd.DataFrame.from_records(output['mydata'],columns=["symid","view_name","view_last_update_time","port_grpname","director","port","port_wwn"])
# print(df['view_last_update_time'])


df.view_last_update_time=pd.to_datetime(df['view_last_update_time'])


# dd=df.view_last_update_time
# print(type(dd))

import csv
import datetime

import MySQLdb
conn=MySQLdb.connect('localhost', 'root', 'password', 'mysql')
print('connected')

cur = conn.cursor()


df.to_csv('Vmax_svpg.csv',index=False)
Location=r'C:\mycode\xmldataset\examples\Vmax_svpg.csv'
df=read_csv(Location)

with open(Location) as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        # print(row[2])
        # a = row[0],row[1],row[2],row[3],row[4],row[5],row[6]
        # row[2] = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')

        # print(type(row[2]))
        # if row[2] !='':
        #     c = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
        # else:
        #     pass# print(type(a))
        # cur.execute(
        #     "INSERT INTO ggg(sid, view_name, last_update_time, port_grpname, director, port, port_wwn) VALUES (%s, %s, %s, %s, %s, %s, %s)",a,c)
        cur.execute(
            "INSERT INTO dc(last_update_time)VALUES(%s)",row[2])
# Creating Tables and inserting data
##### for Vmax_svpg

# cur.execute("""
#             CREATE TABLE cc(
#                 sid VARCHAR(64)  ,
#                 view_name VARCHAR(256) ,
#                 last_update_time DATE ,
#                 port_grpname VARCHAR(256)  ,
#                 director VARCHAR(16)  ,
#                 port VARCHAR(8)  ,
#                 port_wwn VARCHAR(32)
#                 )
#                     """)

conn.commit()















