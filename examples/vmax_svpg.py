import pprint
import pandas as pd
import xmldataset
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
xml_data = open('Vmax_cluster.xml').read()

# for Vmax_svpg

profile="""
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:mydata
            Masking_View
                View_Info
                    view_name = dataset:mydata
                    view_last_update_time = dataset:mydata
                    port_grpname = dataset:mydata
                    port_info
                        Director_Identification
                            dir = dataset:mydata
                            port = dataset:mydata
                            port_wwn = dataset:mydata
       """



output = xmldataset.parse_using_profile(xml_data,profile)


df = pd.DataFrame.from_records(output['mydata'],columns=["symid","view_name","view_last_update_time","port_grpname","dir","port","port_wwn","filename"])
print(df)
df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')


renaming_column=df.rename(columns={'symid':'sid','dir':'director'})
renaming_column.view_last_update_time=pd.to_datetime(renaming_column['view_last_update_time'])


updated_df=pd.DataFrame(data=renaming_column,columns=["sid","view_name","view_last_update_time","port_grpname","director","port","port_wwn","filename"])
manipulating_values = {'sid':renaming_column['sid'][0],'view_name':renaming_column['view_name'][0],'view_last_update_time':renaming_column['view_last_update_time'][0],'port_grpname':renaming_column['port_grpname'][0],'filename':'showview'}
filling_nan_values=updated_df.fillna(value=manipulating_values)

removing_duplicated_rows=filling_nan_values.drop(filling_nan_values.index[[4,5,6,7,8,9,10,11]])
print(removing_duplicated_rows)

engine = create_engine('mysql://root:password@localhost/mysql')

try:
    with engine.connect() as conn, conn.begin():
        removing_duplicated_rows.to_sql('vmax_svpg', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"port_grpname": VARCHAR(256), "director": VARCHAR(16), "port": VARCHAR(8), "port_wwn": VARCHAR(32),"filename": VARCHAR(512)})
except:
    print("Error while connecting to MySQL")

finally:
    conn.close()
    print("MySQL connection is closed")