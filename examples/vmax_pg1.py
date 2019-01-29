from __future__ import print_function
import xml.etree.cElementTree as ET
import pandas as pd
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
from collections import OrderedDict
import re
tree = ET.parse("cluster_standalone_listview.xml")
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
                record['sid']=sid
                # print(record)
                recordx.append(record.copy())


# df=pd.DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
df=pd.DataFrame.from_records(recordx,columns=['sid','port_grpname','dir','port','port_wwn','filename'])


df.drop_duplicates(subset ="port_wwn", keep = 'first', inplace = True)
# df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')
df['dir']=df['dir'].str.replace('FA-', '')
# df.view_last_update_time=pd.to_datetime(df['view_last_update_time'])

print(df)
manipulating_values = {'filename':'listview'}
filling_nan_values=df.fillna(value=manipulating_values)

# print(filling_nan_values)

engine = create_engine('mysql://root:password@localhost/mysql')

try:
    with engine.connect() as conn, conn.begin():
        filling_nan_values.to_sql('vmax_pg', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"port_grpname": VARCHAR(256), "director": VARCHAR(16), "port": VARCHAR(8), "port_wwn": VARCHAR(32),"filename": VARCHAR(512)})
except:
    print("Error while connecting to MySQL")

finally:
    conn.close()
    print("MySQL connection is closed")















                # print(record.items())
                # for range in recordz['testds']:
                #     print(range)


            #     recordz['testds'] = record
            #     # df = pd.DataFrame.from_records(recordz['testds'])
            #     print(recordz)
#converting to data farmes
# recordz['testds'] = record
# print(recordx)
# df=pd.DataFrame.from_records(recordz['testds'])
# print(df)

def joiner(son_child):
    print()

def final_dict():
    print()
    #take the record and take joiner in final dict