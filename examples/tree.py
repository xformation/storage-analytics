import xml.etree.cElementTree as ET
import pandas as pd
from collections import OrderedDict


tree = ET.parse("cluster_standalone_listview.xml")
root = tree.getroot()
root_tag = root.tag
# print(root_tag)

## traversing to each elements using loops
# for child in root:
#     print(child.tag,child.attrib)
#     if child.attrib == {}:
#         for ch in child:
#             print(ch.tag)
#             if ch.tag == 'Symm_Info':
#                 symid = ch.text
#             if ch.tag == 'Masking_View':
#                 for m in ch:
#                     print("inside masking view",m.tag, m.attrib,m.text)
#                     for view in m:
#                         print("    "+"inside View_Info", view.tag, view.text)
                        # if view.text == 'view_name':
                        #     viewname = view.text
                        # if view.text == 'view_last_update_time':
                        #     lastupdate = view.text
                        # if view.text == 'init_grpname':
                        #     initgroup = view.find('init_grpname')
                        # print('* {} {} {}'.format(viewname,lastupdate,initgroup))



    # for view in child:
    #     print(view.tag)
    #     for mask in view:
    #         print(mask.tag)
        # for cc in c:
        #     for ccd in cc:
        #         print (ccd.tag, ccd.text)



# for form in root.findall("Symmetrix/Symm_Info/symid"):
#     print(form.text)
#     x=(form.attrib)
#     print(x)
#     z=list(x)
#     for i in z:
#         print(x[i])

testrecord = {}
j=0;
maskingview = tree.findall('Symmetrix/Masking_View/View_Info')
# print(maskingview)


# def info_for_wwn(each_wwn):
#     for elements in maskingview:
#         syminfo = elements.find('')
#         print(syminfo)
#         print(elements)
#         view = elements.find('view_name').text
#         viewtag = elements.find('view_name').tag
#         lastupdated = elements.find('view_last_update_time').text
#         lastupdatedtag = elements.find('view_last_update_time').tag
#         initgrp = elements.find('init_grpname').text
#         initgrptag = elements.find('init_grpname').tag
#         # wwntag = elements.find('Initiators/wwn').tag
#
#         # print(view, lastupdated, initgrp, wwn)
#         testrecord = {viewtag: view, lastupdatedtag: lastupdated, initgrptag:initgrp}
#         print(testrecord)
#         # tmpdf = {elements.find('view_name').tag : view}
# record = {'gone': [testrecord]}
# df = pd.DataFrame.from_records(record['gone'])
# print(df)

## getting all luns out of the xml  ### working tested ##
listwwn = listwwn1 = []
wwt = root.findall('Initiators')
for each_wwn in root.iter('wwn'):
        listwwn1.append(each_wwn.text)
# print(listwwn1)

# print(listwwn) # print all list of the wwn's
listwwn= list(OrderedDict.fromkeys(listwwn))
# print(listwwn)
# print(listwwn.pop()) # getting out the last item , need to send out index to start from first till end
# info_for_wwn()

dictlist = []
for elements in maskingview:
    # syminfo = elements.find('')
    # print(syminfo)
    # print(elements)
    view = elements.find('view_name').text
    viewtag = elements.find('view_name').tag
    lastupdated = elements.find('view_last_update_time').text
    lastupdatedtag = elements.find('view_last_update_time').tag
    initgrp = elements.find('init_grpname').text
    initgrptag = elements.find('init_grpname').tag
    # wwntag = elements.find('Initiators/wwn').tag

    # print(view, lastupdated, initgrp, wwn)
    testrecord = {viewtag: view, lastupdatedtag: lastupdated, initgrptag: initgrp}
    # print(testrecord)
    dictlist.append(testrecord)
# print(len(dictlist))
print(dictlist)

d = 0
diclist2 = []
i=j=0
# for record in dictlist:
#     while(listwwn):
#         # record.update({['wwn']: 5})
#         record['wwn']= listwwn.pop(i)
#         print(record)
#         # diclist2.append(record)
#         i += 1
#         record['wwn'] = listwwn.pop(i)
#         print(record)
#         break
#     dictlist.pop(j)
#     j += 1
