import pprint
import pandas as pd
import xmldataset
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine

ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
xml_data = open('cluster_standalone_listview.xml').read()

# for Vmax_cluster

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
                        port = dataset:mydata,name:port_no
                        pd_name = dataset:mydata
                        host_lun = dataset:mydata
                        attr = dataset:mydata
                        capacity = dataset:mydata

    """

output = xmldataset.parse_using_profile(xml_data, profile)

df = pd.DataFrame.from_records(output['mydata'],
                               columns=["symid", "view_name", "view_last_update_time", "init_grpname", "group_name",
                                        "wwn", "user_node_name", "user_port_name", "port_grpname", "dir", "port",
                                        "port_wwn", "stor_grpname", "dev_name", "director", "port_no", "pd_name",
                                        "host_lun", "attr", "capacity"])

df['view_last_update_time'] = df['view_last_update_time'].str.replace(',', ' ')

# renaming columns

renaming_column = df.rename(columns={'symid': 'sid'})
# print(renaming_column)
renaming_column.view_last_update_time = pd.to_datetime(renaming_column['view_last_update_time'])
updated_df = pd.DataFrame(data=renaming_column,
                          columns=["sid", "view_name", "view_last_update_time", "init_grpname", "group_name", "wwn",
                                   "user_node_name", "user_port_name", "port_grpname", "dir", "port", "port_wwn",
                                   "stor_grpname", "dev_name", "director", "port_no", "pd_name", "host_lun", "attr",
                                   "capacity"])
# deleting_nan_values = updated_df.apply(lambda x: pd.Series(x.dropna().values))
# print(updated_df)
#
#
#

#-------------------------------------------
#pushing data to db
#------------------------------------------
engine = create_engine('mysql://root:password@localhost/mysql')
#
try:
    with engine.connect() as conn, conn.begin():
        updated_df.to_sql('listviewx', conn, if_exists='append', index=False,
                          dtype={"sid": VARCHAR(64), "view_name": VARCHAR(256), "init_grpname": VARCHAR(256),
                                 "group_name": VARCHAR(256), "wwn": VARCHAR(32), "user_node_name": VARCHAR(256),
                                 "user_port_name": VARCHAR(256), "port_grpname": VARCHAR(256), "dir": VARCHAR(32),
                                 "port": VARCHAR(256), "port_wwn": VARCHAR(256), "stor_grpname": VARCHAR(256),
                                 "dev_name": VARCHAR(256), "director": VARCHAR(256), "port_no": VARCHAR(256),
                                 "pd_name": VARCHAR(256), "host_lun": VARCHAR(256), "attr": VARCHAR(256),
                                 "capacity": VARCHAR(256)})
except:
    print("Error while connecting to MySQL")
finally:
    conn.close()
    print("MySQL connection is closed")

