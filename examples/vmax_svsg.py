import pprint
import pandas as pd
import xmldataset
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
xml_data = open('Vmax_cluster.xml').read()

# for Vmax_svsg

profile="""
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:mydata
            Masking_View
                View_Info
                    view_name = dataset:mydata
                    view_last_update_time = dataset:mydata
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



output = xmldataset.parse_using_profile(xml_data,profile)
df=pd.DataFrame.from_records(output['mydata'],columns=["symid","view_name","view_last_update_time","stor_grpname","dev_name","director","port","pd_name","host_lun","attr","capacity","filename"])
df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')
deleting_nan_values  = df.apply(lambda x: pd.Series(x.dropna().values))
# print(deleting_nan_values)

deleting_nan_values.dev_name.iloc[47] = deleting_nan_values.dev_name.iloc[11]
deleting_nan_values.dev_name.iloc[46] = deleting_nan_values.dev_name.iloc[11]
deleting_nan_values.dev_name.iloc[45] = deleting_nan_values.dev_name.iloc[11]
deleting_nan_values.dev_name.iloc[44] = deleting_nan_values.dev_name.iloc[11]


deleting_nan_values.dev_name.iloc[43] = deleting_nan_values.dev_name.iloc[10]
deleting_nan_values.dev_name.iloc[42] = deleting_nan_values.dev_name.iloc[10]
deleting_nan_values.dev_name.iloc[41] = deleting_nan_values.dev_name.iloc[10]
deleting_nan_values.dev_name.iloc[40] = deleting_nan_values.dev_name.iloc[10]

deleting_nan_values.dev_name.iloc[39] = deleting_nan_values.dev_name.iloc[9]
deleting_nan_values.dev_name.iloc[38] = deleting_nan_values.dev_name.iloc[9]
deleting_nan_values.dev_name.iloc[37] = deleting_nan_values.dev_name.iloc[9]
deleting_nan_values.dev_name.iloc[36] = deleting_nan_values.dev_name.iloc[9]

deleting_nan_values.dev_name.iloc[35] = deleting_nan_values.dev_name.iloc[8]
deleting_nan_values.dev_name.iloc[34] = deleting_nan_values.dev_name.iloc[8]
deleting_nan_values.dev_name.iloc[33] = deleting_nan_values.dev_name.iloc[8]
deleting_nan_values.dev_name.iloc[32] = deleting_nan_values.dev_name.iloc[8]


deleting_nan_values.dev_name.iloc[31] = deleting_nan_values.dev_name.iloc[7]
deleting_nan_values.dev_name.iloc[30] = deleting_nan_values.dev_name.iloc[7]
deleting_nan_values.dev_name.iloc[29] = deleting_nan_values.dev_name.iloc[7]
deleting_nan_values.dev_name.iloc[28] = deleting_nan_values.dev_name.iloc[7]


deleting_nan_values.dev_name.iloc[27] = deleting_nan_values.dev_name.iloc[6]
deleting_nan_values.dev_name.iloc[26] = deleting_nan_values.dev_name.iloc[6]
deleting_nan_values.dev_name.iloc[25] = deleting_nan_values.dev_name.iloc[6]
deleting_nan_values.dev_name.iloc[24] = deleting_nan_values.dev_name.iloc[6]

deleting_nan_values.dev_name.iloc[23] = deleting_nan_values.dev_name.iloc[5]
deleting_nan_values.dev_name.iloc[22] = deleting_nan_values.dev_name.iloc[5]
deleting_nan_values.dev_name.iloc[21] = deleting_nan_values.dev_name.iloc[5]
deleting_nan_values.dev_name.iloc[20] = deleting_nan_values.dev_name.iloc[5]


deleting_nan_values.dev_name.iloc[19] = deleting_nan_values.dev_name.iloc[4]
deleting_nan_values.dev_name.iloc[18] = deleting_nan_values.dev_name.iloc[4]
deleting_nan_values.dev_name.iloc[17] = deleting_nan_values.dev_name.iloc[4]
deleting_nan_values.dev_name.iloc[16] = deleting_nan_values.dev_name.iloc[4]

deleting_nan_values.dev_name.iloc[15] = deleting_nan_values.dev_name.iloc[3]
deleting_nan_values.dev_name.iloc[14] = deleting_nan_values.dev_name.iloc[3]
deleting_nan_values.dev_name.iloc[13] = deleting_nan_values.dev_name.iloc[3]
deleting_nan_values.dev_name.iloc[12] = deleting_nan_values.dev_name.iloc[3]

deleting_nan_values.dev_name.iloc[11] = deleting_nan_values.dev_name.iloc[2]
deleting_nan_values.dev_name.iloc[10] = deleting_nan_values.dev_name.iloc[2]
deleting_nan_values.dev_name.iloc[9] = deleting_nan_values.dev_name.iloc[2]
deleting_nan_values.dev_name.iloc[8] = deleting_nan_values.dev_name.iloc[2]

deleting_nan_values.dev_name.iloc[7] = deleting_nan_values.dev_name.iloc[1]
deleting_nan_values.dev_name.iloc[6] = deleting_nan_values.dev_name.iloc[1]
deleting_nan_values.dev_name.iloc[5] = deleting_nan_values.dev_name.iloc[1]
deleting_nan_values.dev_name.iloc[4] = deleting_nan_values.dev_name.iloc[1]

deleting_nan_values.dev_name.iloc[3] = deleting_nan_values.dev_name.iloc[0]
deleting_nan_values.dev_name.iloc[2] = deleting_nan_values.dev_name.iloc[0]
deleting_nan_values.dev_name.iloc[1] = deleting_nan_values.dev_name.iloc[0]



# print(deleting_nan_values)


renaming_column=deleting_nan_values.rename(columns={'symid':'sid','dev_name':'dev_id','pd_name':'phydev_name'})

print(renaming_column)


renaming_column.view_last_update_time=pd.to_datetime(renaming_column['view_last_update_time'])
# # print(renaming_column)
updated_df=pd.DataFrame(data=renaming_column,columns=["sid","view_name","view_last_update_time","stor_grpname","dev_id","director","port","phydev_name","host_lun","attr","capacity","filename"])

# print(updated_df)
manipulating_values = {'sid':renaming_column['sid'][0],'view_name':renaming_column['view_name'][0],'view_last_update_time':renaming_column['view_last_update_time'][0],'stor_grpname':renaming_column['stor_grpname'][0],'filename':'showview'}
filling_nan_values=renaming_column.fillna(value=manipulating_values)
# print(filling_nan_values)
removing_duplicated_rows=filling_nan_values.drop(filling_nan_values.index[[24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]])
print(removing_duplicated_rows)

engine = create_engine('mysql://root:password@localhost/mysql')
try:
    with engine.connect() as conn, conn.begin():
        removing_duplicated_rows.to_sql('vmax_svsg', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"stor_grpname": VARCHAR(256), "dev_id": VARCHAR(128),'director': VARCHAR(16), 'port': VARCHAR(8), 'phydev_name': VARCHAR(128), 'host_lun': VARCHAR(8), 'attr': VARCHAR(16), 'capacity': VARCHAR(32),'filename': VARCHAR(512)})
except:
    print("Error while connecting to MySQL")
finally:
    conn.close()
    print("MySQL connection is closed")
















