from __future__ import print_function
import xml.etree.cElementTree as ET
import pandas as pd
from collections import OrderedDict
import re
tree = ET.parse("cluster_standalone_listview.xml")
root = tree.getroot()
root_tag = root.tag

print(root_tag,root.attrib)

record = {}
rtem = {}
final = {}
trec = {}
listw = []
listp = []
recordx = []
recordz = {}
portdict = {}
listp2 = []
portdict2 = {}

thisdict = {}
thislist = []

for child in root:
    # print(child.tag, child.attrib)
    for subchild in child:
        # print(subchild.tag, subchild.attrib)
        for superchild in subchild:
            # print(superchild.tag, superchild.attrib)
            for sonchild in superchild:
                # print("   " + sonchild.tag, sonchild.attrib)
                if not re.search('(\n+)(.*)', sonchild.text):
                    record[sonchild.tag] = sonchild.text

                elif sonchild.tag :
                    if sonchild.tag == 'Initiators':
                        gname = ''
                        for kid in sonchild:
                            if kid.tag == 'group_name':
                                # gname = kid.text
                                thisdict['group_name'] = kid.text
                                thislist.append(kid.text)
                            rtem[kid.tag] = kid.text
                            if kid.tag == 'user_port_name':
                                # trec.update(rtem)
                                if gname:
                                    rtem[kid.tag] = kid.text
                                listw.append(rtem.items())
                                rtem = {}
                            # elif kid.tag == ''
                            # record.update(trec)
                        while(listw):
                            print(listw.pop(0))
                    # elif sonchild.tag == 'port_info':
                    #     for son1 in sonchild:
                    #             for grandson in son1:
                    #                 portdict[grandson.tag] = grandson.text
                    #                 if grandson.tag == 'port_wwn':
                    #                     # trec.update(rtem)
                    #                     listp.append(portdict.items())
                    #                     portdict = {}
                    #                     # print(listp)
                    # elif sonchild.tag == 'Device':
                    #     for son2 in sonchild:
                    #         if not re.search('(\n+)(.*)', son2.text):
                    #             if son2.tag == 'dev_name':
                    #                 mdev = son2.text
                    #             if not(son2.tag == 'capacity_gb' or son2.tag == 'capacity_tb'):
                    #                 portdict2[son2.tag] = son2.text
                    #             if son2.tag == 'capacity' :
                    #                 if 'dev_name' not in portdict2:
                    #                     portdict2['dev_name'] = mdev
                    #                 else:
                    #                     portdict2.pop('dev_name')
                    #                     portdict2['dev_name'] = mdev
                    #                         # trec.update(rtem)
                    #                 listp2.append(portdict2.items())
                    #                 portdict2 = {}
                    #                 # print(listp2)
                    # else:
                    #     if not re.search('(\n+)(.*)', sonchild.text): # search for the parent tag
                    #         record[sonchild.tag] = sonchild.text
            # print(record)
            i = 0
            # while(listw):
            #     record.update(listw.pop(i))
            #     print(record)
                # recordx.append(record)
                # if 'group_name' in record:
                    # record['init_grpname'] = record['group_name']
                    # print(record)
                # else:
                #     record['group_name'] = ""
                #     print(record)
# print(recordx)

#converting to data farmes
# recordz['testds'] = recordx
# print(recordx)
# df=pd.DataFrame.from_records(recordz['testds'])
# print(df)

