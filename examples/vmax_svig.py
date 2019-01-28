import pprint
import pandas as pd
import xmldataset
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
xml_data = open('Vmax_cluster.xml').read()

# for Vmax_cluster

profile="""
        SymCLI_ML
                Symmetrix
                    Symm_Info
                        symid = dataset:mydata
                    Masking_View
                        View_Info
                            view_name = dataset:mydata
                            view_last_update_time = dataset:mydata
                            init_grpname = dataset:mydata
                            Initiators
                                group_name = dataset:mydata
                            Initiator_List
                                Initiator
                                    group_name = dataset:mydata
                                    wwn = dataset:mydata
                                    user_node_name = dataset:mydata
                                    user_port_name = dataset:mydata
        
            """

output = xmldataset.parse_using_profile(xml_data,profile)
print(output)
df=pd.DataFrame.from_records(output['mydata'],columns=["symid","view_name","view_last_update_time","init_grpname","group_name","wwn","user_node_name","user_port_name","filename"])
# print(df['view_last_update_time'])


df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')
# print(df['view_last_update_time']


# renaming columns

renaming_column=df.rename(columns={'symid':'sid','init_grpname':'parent_ig','group_name':'init_grpname'})
#replacing second  row of parent_ig with  parent_ig of first row
renaming_column.parent_ig.iloc[3] = renaming_column.parent_ig.iloc[0]
renaming_column.parent_ig.iloc[4] = renaming_column.parent_ig.iloc[0]
renaming_column.init_grpname.iloc[2] = renaming_column.init_grpname.iloc[1]
renaming_column.init_grpname.iloc[1] = renaming_column.init_grpname.iloc[0]



# # converting time format in pandas
renaming_column.view_last_update_time=pd.to_datetime(renaming_column['view_last_update_time'])


updated_df=pd.DataFrame(data=renaming_column,columns=["sid","view_name","view_last_update_time","parent_ig","init_grpname","wwn","user_node_name","user_port_name","filename"])
# manipulating data
manipulating_values = {'sid':updated_df['sid'][0],'view_name':updated_df['view_name'][0],'view_last_update_time':updated_df['view_last_update_time'][0],'parent_ig':updated_df['parent_ig'][0],'filename':'showview'}
# filling data in NAN(null) values
# filling_nan_values=updated_df.fillna(value=manipulating_values)



deleting_nan_values  = updated_df.apply(lambda x: pd.Series(x.dropna().values))
filling_nan_values=deleting_nan_values.fillna(value=manipulating_values)

# print(filling_nan_values)


engine = create_engine('mysql://root:password@localhost/mysql')

try:
        with engine.connect() as conn, conn.begin():
                filling_nan_values.to_sql('vmax_svig', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"parent_ig": VARCHAR(256),"init_grpname": VARCHAR(256),"wwn": VARCHAR(32),"user_node_name": VARCHAR(256),"user_port_name": VARCHAR(256),"filename": VARCHAR(512)})
except:
        print("Error while connecting to MySQL")

finally:
        conn.close()
        print("MySQL connection is closed")
