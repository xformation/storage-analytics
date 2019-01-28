import xmldataset
import pprint
import pandas as pd
# Setup Pretty Printing
ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint

xml_data = open('cluster_standalone_listview.xml').read()

profile = """
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:mydata
            Masking_View
                View_Info
                    view_name = dataset:mydata
                    view_last_update_time = dataset:mydata
                    init_grpname = dataset:mydata
                    Initiator_List
                        Initiator
                            group_name = dataset:mydata
                            wwn = dataset:mydata
                            user_node_name = dataset:mydata
                            user_port_name = dataset:mydata
                    port_grpname = dataset:mydata
                    port_info
                        Director_Identification
                            dir = dataset:mydata
                            port = dataset:mydata
                            port_wwn = dataset:mydata
                    stor_grpname = dataset:mydata
                    Device
                        dev_name = dataset:mydata
                        director = dataset:mydata
                        port = dataset:mydata
                        pd_name = dataset:mydata
                        host_lun = dataset:mydata
                        attr = dataset:mydata
                        capacity = dataset:mydata
    """

# xml = """<?xml version="1.0"?>
#   <catalog>
#      <shop number="1">
#         <book id="bk101">
#            <author>Gambardella, Matthew</author>
#            <title>XML Developer's Guide</title>
#            <genre>Computer</genre>
#            <price>44.95</price>
#            <publish_date>2000-10-01</publish_date>
#            <description>An in-depth look at creating applications
#            with XML.</description>
#         </book>
#         <book id="bk102">
#            <author>Ralls, Kim</author>
#            <title>Midnight Rain</title>
#            <genre>Fantasy</genre>
#            <price>5.95</price>
#            <publish_date>2000-12-16</publish_date>
#            <description>A former architect battles corporate zombies,
#            an evil sorceress, and her own childhood to become queen
#            of the world.</description>
#         </book>
#      </shop>
#      <shop number="2">
#         <book id="bk103">
#            <author>Corets, Eva</author>
#            <title>Maeve Ascendant</title>
#            <genre>Fantasy</genre>
#            <price>5.95</price>
#            <publish_date>2000-11-17</publish_date>
#            <description>After the collapse of a nanotechnology
#            society in England, the young survivors lay the
#            foundation for a new society.</description>
#         </book>
#         <book id="bk104">
#            <author>Corets, Eva</author>
#            <title>Oberon's Legacy</title>
#            <genre>Fantasy</genre>
#            <price>5.95</price>
#            <publish_date>2001-03-10</publish_date>
#            <description>In post-apocalypse England, the mysterious
#            agent known only as Oberon helps to create a new life
#            for the inhabitants of London. Sequel to Maeve
#            Ascendant.</description>
#         </book>
#      </shop>
#   </catalog>"""

# profile="""
# catalog
#     shop
#         book
#             author = dataset:title_and_author
#             title  = dataset:title_and_author dataset:title_and_genre
#             genre  = dataset:title_and_genre"""

# result = xmldataset.parse_using_profile(xml, profile)
# df = pd.DataFrame.from_records(result)
output = xmldataset.parse_using_profile(xml_data, profile)
print(output)
df=pd.DataFrame.from_records(output['mydata'], columns=["symid","view_name","view_last_update_time","init_grpname","group_name","wwn","user_node_name","user_port_name","port_grpname","dir","port","port_wwn","stor_grpname","dev_name","director","pd_name","host_lun","attr","capacity"])
print(df)