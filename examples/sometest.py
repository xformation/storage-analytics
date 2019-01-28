import xml.etree.cElementTree as ET
import operator
tree = ET.parse("cluster_standalone_listview.xml")
root = tree.getroot()
root_tag = root.tag

# print(root_tag)
# traversing to each elements using loops
for child in root:
    # print(child.tag,child.attrib)
    if child.attrib == {}:
        for ch in child:
            # print(ch.tag)
            for h in ch:
                # print(h.tag)
                if h.tag == 'symid':
                    if h.tag == 'symid' and h.text != '':
                        symid = h.tag,h.text
                        print(symid)
            if ch.tag == 'Masking_View':
                for m in ch:
                    print(m.tag, m.attrib,m.text)

                    for element in m:
                        # print(element.text)
                        # print(element.tag, element.text)
                        if element.tag == 'view_name' and element.text != '':
                            viewname = element.tag,element.text
                            print(viewname)
                        if element.tag == 'view_last_update_time' and element.text !='':
                            view_last_update_time = element.tag,element.text
                            print(view_last_update_time)
                        if element.tag == 'init_grpname' and element.text !='':
                            init_grpname = element.tag,element.text
                            print(init_grpname)
                        if element.tag == 'Initiator_List':
                            for x in element:
                                # print(x.tag)
                                for y in x:
                                    # print(y.tag)
                                    if y.tag == 'wwn' and y.text!='':
                                        wwn=y.tag,y.text
                                        print(wwn)
                                    if y.tag == 'user_node_name' and y.text!='':
                                        user_node_name=y.tag,y.text
                                        print(user_node_name)
                                    if y.tag == 'user_port_name' and y.text!='':
                                        user_port_name=y.tag,y.text
                                        print(user_port_name)