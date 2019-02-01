from __future__ import print_function
import xml.etree.cElementTree as ET
import pandas as pd
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
from collections import OrderedDict
import re

tree = ET.parse("1695_listview.xml")
root = tree.getroot()
root_tag = root.tag

# print(root_tag,root.attrib)

record = {}
rtem = {}
final = {}
trec = {}
listw = []
listp = []
recordx = []

portdict = {}
listp2 = []
portdict2 = {}

for child in root:
    # print(child.tag, child.attrib)
    for subchild in child:
        # print(subchild.tag, subchild.attrib)
        if subchild.tag == 'Symm_Info':
            for id in subchild:
                sid = id.text
        for superchild in subchild:
            # print(superchild.tag, superchild.attrib)
            for sonchild in superchild:
                # print("   " + sonchild.tag, sonchild.attrib)
                if not re.search('(\n+)(.*)', sonchild.text):
                    # record[sonchild.tag] = sonchild.text
                    # print(sonchild.tag)
                    if sonchild.tag=='view_name':
                        record[sonchild.tag]=sonchild.text
                    if sonchild.tag=='view_last_update_time':
                        record[sonchild.tag]=sonchild.text
                    if sonchild.tag=='port_grpname':
                        record[sonchild.tag]=sonchild.text
                elif sonchild.tag == 'port_info':
                    for son1 in sonchild:
                            for grandson in son1:
                                portdict[grandson.tag] = grandson.text
                                if grandson.tag == 'port_wwn':
                                        # trec.update(rtem)
                                    listp.append(portdict.items())
                                    portdict = {}
                                        # print(listp)
            i = 0
            while(listp):
                record.update(listp.pop(i))
                record['sid'] = sid
                # print(record)
                recordx.append(record.copy())
df=pd.DataFrame.from_records(recordx,columns=['sid','view_name','view_last_update_time','port_grpname','dir','port','port_wwn','filename'])
print(df)
df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')
df['dir']=df['dir'].str.replace('FA-', '')
df.view_last_update_time=pd.to_datetime(df['view_last_update_time'])


manipulating_values = {'filename':'listview'}
filling_nan_values=df.fillna(value=manipulating_values)

engine = create_engine('mysql://root:password@localhost/mysql')

try:
    with engine.connect() as conn, conn.begin():
        filling_nan_values.to_sql('vmax_pg', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"port_grpname": VARCHAR(256), "director": VARCHAR(16), "port": VARCHAR(8), "port_wwn": VARCHAR(32),"filename": VARCHAR(512)})
except:
    print("Error while connecting to MySQL")

finally:
    conn.close()
    print("MySQL connection is closed")