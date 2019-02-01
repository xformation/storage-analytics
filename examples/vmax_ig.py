from __future__ import print_function
import xml.etree.cElementTree as ET
import pandas as pd
from collections import OrderedDict
import re
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine

filename = "1695_listview.xml"

tree = ET.parse(filename)
root = tree.getroot()
root_tag = root.tag

# print(root_tag,root.attrib)

record = {}
rtem = {}; gterm = {}
final = {}
trec = {}
listw = []
listp = []
recordx = []
recordz = {}
portdict = {}
listp2 = []
portdict2 = {}
listgroup =[]
flist = []
gn = ''; a = '';i = ''
flag = 0
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
                    if sonchild.tag=='view_name':
                        record[sonchild.tag]=sonchild.text
                    if sonchild.tag=='view_last_update_time':
                        record[sonchild.tag]=sonchild.text
                    if sonchild.tag=='init_grpname':
                        record[sonchild.tag] = sonchild.text
                elif sonchild.tag :
                    if sonchild.tag == 'Initiators':
                        # trec = record
                        for kid in sonchild:
                            if kid.tag == 'group_name':
                                # gterm[kid.tag] = kid.text
                                listgroup.append(kid.text)
                                # gterm = {}
                            #     print(listgroup)

                            rtem[kid.tag] = kid.text
                            if kid.tag == 'user_port_name':
                                # trec.update(rtem)
                                listw.append(rtem.items())
                                rtem = {}
                                        # print(listp)
            # if listgroup:
                # print(listgroup)
                # listgroup = []
            #-----------
            #trying for the group names
            #------------------
                # if listgroup:
                #     gn = listgroup.pop(0)
                # i = 0
                # while (listw):
                #     record.update(listw.pop(i))
                #     if 'group_name' not in record:
                #         record['group_name'] = gn
                #     print(record)
                #     if not listw:
                #         record = {}
            #-------------------------------
            # processing group names
            #-------------------------------
            if listgroup:
                if flag:
                    # record.update(listgroup.pop(0))
                    a = listgroup.pop(0)
                    # print(len(listgroup))
                    if len(listgroup) == 0:
                        flag = 0
                    # print(record)
                else:
                    flag = 1

            i = 0
            while(listw):
                record.update(listw.pop(i))
                if a:
                    record['group_name'] = a
                    record['sid'] = sid
                else:
                    record['group_name'] = 'n/a'
                    record['sid'] = sid
                if record['user_node_name'].isspace():
                    record['user_node_name'] = 'n/a'
                if record['user_port_name'].isspace():
                    record['user_port_name'] = 'n/a'
                # print(record)
                flist.append(record.copy())

                if not listw:
                    record = {}
                    a = ''  #resetting the group name when done with last group name

# print(flist)
# for i in flist:
#     print(i)
# print(listgroup)

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

df=pd.DataFrame.from_records(flist,columns=["sid","view_name","view_last_update_time","init_grpname","group_name","wwn","user_node_name","user_port_name","filename"])
# print(df)

df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')
df.view_last_update_time=pd.to_datetime(df['view_last_update_time'])

manipulating_values = {'user_node_name':'n/a','user_port_name': 'n/a','filename':'listview'}
filling_nan_values=df.fillna(value=manipulating_values)

engine = create_engine('mysql://root:password@localhost/mysql')

try:
        with engine.connect() as conn, conn.begin():
            filling_nan_values.to_sql('vmax_ig', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"parent_ig": VARCHAR(256),"init_grpname": VARCHAR(256),"wwn": VARCHAR(32),"user_node_name": VARCHAR(256),"user_port_name": VARCHAR(256),"filename": VARCHAR(512)})
except:
        print("Error while connecting to MySQL")

finally:
        conn.close()
        print("MySQL connection is closed")