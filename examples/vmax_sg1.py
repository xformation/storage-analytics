from __future__ import print_function
import xml.etree.cElementTree as ET
import pandas as pd
from collections import OrderedDict
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
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
                    if sonchild.tag=='stor_grpname':
                        record[sonchild.tag]=sonchild.text
                elif sonchild.tag == 'Device':
                    for son2 in sonchild:
                        if not re.search('(\n+)(.*)', son2.text):
                            if son2.tag == 'dev_name':
                                mdev = son2.text
                                # print(portdict2)
                            # if son2.tag == 'director':
                            #     portdict2[son2.tag] = son2.text
                            # if son2.tag == 'port':
                            #     portdict2[son2.tag] = son2.text
                            if son2.tag == 'host_lun':
                                portdict2[son2.tag] = son2.text
                            if son2.tag == 'attr':
                                portdict2[son2.tag] = son2.text
                            if son2.tag == 'capacity':
                                portdict2[son2.tag] = son2.text
                                if 'dev_name' not in portdict2:
                                    portdict2['dev_name'] = mdev
                                else:
                                    portdict2.pop('dev_name')
                                    portdict2['dev_name'] = mdev
                                    # trec.update(rtem)
                                listp2.append(portdict2)
                                portdict2={}

                                # print(listp2)
            i = 0
            while(listp2):
                record.update(listp2.pop(i))
                record['sid']=sid
                # print(record)
                recordx.append(record.copy())
df=pd.DataFrame.from_records(recordx,columns=["sid","stor_grpname","dev_name","host_lun","attr","capacity","filename"])
print(df)

df.drop_duplicates(subset ="dev_name", keep = 'first', inplace = True)

# df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')
# df.view_last_update_time=pd.to_datetime(df['view_last_update_time'])

print(df)
manipulating_values = {'filename':'listview'}
filling_nan_values=df.fillna(value=manipulating_values)

engine = create_engine('mysql://root:password@localhost/mysql')
try:
    with engine.connect() as conn, conn.begin():
        filling_nan_values.to_sql('vmax_sg', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"stor_grpname": VARCHAR(256), "dev_id": VARCHAR(128),'director': VARCHAR(16), 'port': VARCHAR(8), 'phydev_name': VARCHAR(128), 'host_lun': VARCHAR(8), 'attr': VARCHAR(16), 'capacity': VARCHAR(32),'filename': VARCHAR(512)})
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