# -*- coding: utf-8 -*-
"""
"""

import xml.etree.cElementTree as et
import pandas as pd


def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None


def main():
    """ main """
    parsed_xml = et.parse("test.xml")
    dfcols = ['symid', 'view_name', 'init_grpname', 'port_grpname','stor_grpname']
    df_xml = pd.DataFrame(columns=dfcols)

    for node in parsed_xml.getroot():
        symid = node.find('symid')
        view_name = node.find('view_name')
        init_grpname = node.find('init_grpname')
        port_grpname = node.find('port_grpname')
        stor_grpname = node.find('stor_grpname')

        df_xml = df_xml.append(
            pd.Series([getvalueofnode(symid), getvalueofnode(view_name), getvalueofnode(init_grpname),
                       getvalueofnode(port_grpname),getvalueofnode(stor_grpname)], index=dfcols),
            ignore_index=True)

    print(df_xml)


main()