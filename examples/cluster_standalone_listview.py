import pprint
import pandas as pd
import xmldataset
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
xml_data = open('cluster_standalone_listview.xml').read()

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

output = xmldataset.parse_using_profile(xml_data,profile)

df=pd.DataFrame.from_records(output['mydata'],columns=["symid","view_name","view_last_update_time","init_grpname","group_name","wwn","user_node_name","user_port_name","port_grpname","dir","port","port_wwn","stor_grpname","dev_name","director","port","pd_name","host_lun","attr","capacity"])


df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')

#renaming columns

renaming_column=df.rename(columns={'symid':'sid'})
# print(renaming_column)
renaming_column.view_last_update_time=pd.to_datetime(renaming_column['view_last_update_time'])
updated_df=pd.DataFrame(data=renaming_column,columns=["sid","view_name","view_last_update_time","init_grpname","group_name","wwn","user_node_name","user_port_name","port_grpname","dir","port","port_wwn","stor_grpname","dev_name","director","port","pd_name","host_lun","attr","capacity"])
print(updated_df)
# deleting_nan_values  = updated_df.apply(lambda x: pd.Series(x.dropna().values))
# print(deleting_nan_values)
#
# engine = create_engine('mysql://root:password@localhost/mysql')
# #
# try:
#     with engine.connect() as conn, conn.begin():
#         updated_df.to_sql('ab', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"init_grpname": VARCHAR(256),"group_name": VARCHAR(256),"wwn": VARCHAR(32),"user_node_name": VARCHAR(256),"user_port_name": VARCHAR(256),"port_grpname": VARCHAR(256),"dir": VARCHAR(32),"port": VARCHAR(256),"port_wwn": VARCHAR(256),"stor_grpname": VARCHAR(256),"dev_name": VARCHAR(256),"director": VARCHAR(256),"port": VARCHAR(256),"pd_name": VARCHAR(256),"host_lun": VARCHAR(256),"attr": VARCHAR(256),"capacity": VARCHAR(256)})
# except:
#     print("Error while connecting to MySQL")
# finally:
#     conn.close()
#     print("MySQL connection is closed")


# updated_df.dev_name.iloc[24262]= updated_df.dev_name.iloc[24258]
# updated_df.dev_name.iloc[24261]= updated_df.dev_name.iloc[24258]
# updated_df.dev_name.iloc[24260]= updated_df.dev_name.iloc[24258]
# updated_df.dev_name.iloc[24259]= updated_df.dev_name.iloc[24258]
#
# updated_df.dev_name.iloc[24258]= updated_df.dev_name.iloc[24254]
# updated_df.dev_name.iloc[24257]= updated_df.dev_name.iloc[24254]
# updated_df.dev_name.iloc[24256]= updated_df.dev_name.iloc[24254]
# updated_df.dev_name.iloc[24255]= updated_df.dev_name.iloc[24254]
#
# updated_df.dev_name.iloc[24254]= updated_df.dev_name.iloc[24250]
# updated_df.dev_name.iloc[24253]= updated_df.dev_name.iloc[24250]
# updated_df.dev_name.iloc[24252]= updated_df.dev_name.iloc[24250]
# updated_df.dev_name.iloc[24251]= updated_df.dev_name.iloc[24250]
#
# updated_df.dev_name.iloc[24250]= updated_df.dev_name.iloc[24246]
# updated_df.dev_name.iloc[24249]= updated_df.dev_name.iloc[24246]
# updated_df.dev_name.iloc[24248]= updated_df.dev_name.iloc[24246]
# updated_df.dev_name.iloc[24247]= updated_df.dev_name.iloc[24246]
#
# updated_df.dev_name.iloc[24246]= updated_df.dev_name.iloc[24242]
# updated_df.dev_name.iloc[24245]= updated_df.dev_name.iloc[24242]
# updated_df.dev_name.iloc[24244]= updated_df.dev_name.iloc[24242]
# updated_df.dev_name.iloc[24243]= updated_df.dev_name.iloc[24242]
#
#
# updated_df.dev_name.iloc[24242]= updated_df.dev_name.iloc[24238]
# updated_df.dev_name.iloc[24241]= updated_df.dev_name.iloc[24238]
# updated_df.dev_name.iloc[24240]= updated_df.dev_name.iloc[24238]
# updated_df.dev_name.iloc[24239]= updated_df.dev_name.iloc[24238]
#
# updated_df.dev_name.iloc[24238]= updated_df.dev_name.iloc[24234]
# updated_df.dev_name.iloc[24237]= updated_df.dev_name.iloc[24234]
# updated_df.dev_name.iloc[24236]= updated_df.dev_name.iloc[24234]
# updated_df.dev_name.iloc[24235]= updated_df.dev_name.iloc[24234]
#
# updated_df.dev_name.iloc[24234]= updated_df.dev_name.iloc[24230]
# updated_df.dev_name.iloc[24233]= updated_df.dev_name.iloc[24246]
# updated_df.dev_name.iloc[24232]= updated_df.dev_name.iloc[24246]
# updated_df.dev_name.iloc[24231]= updated_df.dev_name.iloc[24246]
#
# updated_df.dev_name.iloc[24230]= updated_df.dev_name.iloc[24226]
# updated_df.dev_name.iloc[24229]= updated_df.dev_name.iloc[24226]
# updated_df.dev_name.iloc[24228]= updated_df.dev_name.iloc[24226]
# updated_df.dev_name.iloc[24227]= updated_df.dev_name.iloc[24226]
#
# updated_df.dev_name.iloc[24226]= updated_df.dev_name.iloc[24222]
# updated_df.dev_name.iloc[24225]= updated_df.dev_name.iloc[24222]
# updated_df.dev_name.iloc[24224]= updated_df.dev_name.iloc[24222]
# updated_df.dev_name.iloc[24223]= updated_df.dev_name.iloc[24222]
#
# updated_df.dev_name.iloc[24222]= updated_df.dev_name.iloc[24218]
# updated_df.dev_name.iloc[24221]= updated_df.dev_name.iloc[24218]
# updated_df.dev_name.iloc[24220]= updated_df.dev_name.iloc[24218]
# updated_df.dev_name.iloc[24219]= updated_df.dev_name.iloc[24218]
#
# updated_df.dev_name.iloc[24218]= updated_df.dev_name.iloc[24214]
# updated_df.dev_name.iloc[24217]= updated_df.dev_name.iloc[24214]
# updated_df.dev_name.iloc[24216]= updated_df.dev_name.iloc[24214]
# updated_df.dev_name.iloc[24215]= updated_df.dev_name.iloc[24214]
#
# updated_df.dev_name.iloc[24214]= updated_df.dev_name.iloc[24210]
# updated_df.dev_name.iloc[24213]= updated_df.dev_name.iloc[24210]
# updated_df.dev_name.iloc[24212]= updated_df.dev_name.iloc[24210]
# updated_df.dev_name.iloc[24211]= updated_df.dev_name.iloc[24210]
#
# updated_df.dev_name.iloc[24210]= updated_df.dev_name.iloc[24206]
# updated_df.dev_name.iloc[24209]= updated_df.dev_name.iloc[24206]
# updated_df.dev_name.iloc[24208]= updated_df.dev_name.iloc[24206]
# updated_df.dev_name.iloc[24207]= updated_df.dev_name.iloc[24206]
#
# updated_df.dev_name.iloc[24206]= updated_df.dev_name.iloc[24203]
# updated_df.dev_name.iloc[24205]= updated_df.dev_name.iloc[24203]
# updated_df.dev_name.iloc[24204]= updated_df.dev_name.iloc[24203]
#
# #====================================================================
#
# updated_df.stor_grpname.iloc[24262]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24261]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24260]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24259]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24258]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24257]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24256]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24255]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24254]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24253]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24252]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24251]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24250]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24249]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24248]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24247]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24246]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24245]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24244]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24243]= updated_df.stor_grpname.iloc[24203]
#
#
# updated_df.stor_grpname.iloc[24242]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24241]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24240]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24239]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24238]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24237]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24236]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24235]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24234]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24233]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24232]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24231]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24230]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24229]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24228]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24227]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24226]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24225]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24224]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24223]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24222]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24221]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24220]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24219]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24218]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24217]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24216]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24215]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24214]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24213]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24212]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24211]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24210]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24209]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24208]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24207]= updated_df.stor_grpname.iloc[24203]
#
# updated_df.stor_grpname.iloc[24206]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24205]= updated_df.stor_grpname.iloc[24203]
# updated_df.stor_grpname.iloc[24204]= updated_df.stor_grpname.iloc[24203]
#
# #========================================================================
#
#
# updated_df.port_grpname.iloc[24201]= updated_df.port_grpname.iloc[24200]
# updated_df.port_grpname.iloc[24202]= updated_df.port_grpname.iloc[24200]
# updated_df.port_grpname.iloc[24203]= updated_df.port_grpname.iloc[24200]
#
# #============================================================
#
# updated_df.init_grpname.iloc[24199]= updated_df.parent_ig.iloc[24199]
# updated_df.init_grpname.iloc[24200]= updated_df.init_grpname.iloc[24199]
#
# #===================================================================
#
# updated_df.parent_ig.iloc[24199]= updated_df.parent_ig.iloc[24200]
#
# #====================================================================
#
#
# updated_df.view_last_update_time.iloc[24200]= updated_df.view_last_update_time.iloc[24199]
#
#
# #====================================================================
#
# updated_df.view_name.iloc[24200]= updated_df.view_name.iloc[24199]
#
# #===================================================================
# updated_df.sid.iloc[24199]= updated_df.sid.iloc[0]
# updated_df.sid.iloc[24200]= updated_df.sid.iloc[0]
#
#
#
# #=====================================================
#
#
# updated_df.dev_name.iloc[24199]= updated_df.dev_name.iloc[24195]
# updated_df.dev_name.iloc[24198]= updated_df.dev_name.iloc[24195]
# updated_df.dev_name.iloc[24197]= updated_df.dev_name.iloc[24195]
# updated_df.dev_name.iloc[24196]= updated_df.dev_name.iloc[24195]
#
# updated_df.dev_name.iloc[24195]= updated_df.dev_name.iloc[24191]
# updated_df.dev_name.iloc[24194]= updated_df.dev_name.iloc[24191]
# updated_df.dev_name.iloc[24193]= updated_df.dev_name.iloc[24191]
# updated_df.dev_name.iloc[24192]= updated_df.dev_name.iloc[24191]
#
# updated_df.dev_name.iloc[24191]= updated_df.dev_name.iloc[24187]
# updated_df.dev_name.iloc[24190]= updated_df.dev_name.iloc[24187]
# updated_df.dev_name.iloc[24189]= updated_df.dev_name.iloc[24187]
# updated_df.dev_name.iloc[24188]= updated_df.dev_name.iloc[24187]
#
# updated_df.dev_name.iloc[24187]= updated_df.dev_name.iloc[24183]
# updated_df.dev_name.iloc[24186]= updated_df.dev_name.iloc[24183]
# updated_df.dev_name.iloc[24185]= updated_df.dev_name.iloc[24183]
# updated_df.dev_name.iloc[24184]= updated_df.dev_name.iloc[24183]
#
# updated_df.dev_name.iloc[24183]= updated_df.dev_name.iloc[24179]
# updated_df.dev_name.iloc[24182]= updated_df.dev_name.iloc[24179]
# updated_df.dev_name.iloc[24181]= updated_df.dev_name.iloc[24179]
# updated_df.dev_name.iloc[24180]= updated_df.dev_name.iloc[24179]
#
#
# updated_df.dev_name.iloc[24179]= updated_df.dev_name.iloc[24175]
# updated_df.dev_name.iloc[24178]= updated_df.dev_name.iloc[24175]
# updated_df.dev_name.iloc[24177]= updated_df.dev_name.iloc[24175]
# updated_df.dev_name.iloc[24176]= updated_df.dev_name.iloc[24175]
#
# updated_df.dev_name.iloc[24175]= updated_df.dev_name.iloc[24171]
# updated_df.dev_name.iloc[24174]= updated_df.dev_name.iloc[24171]
# updated_df.dev_name.iloc[24173]= updated_df.dev_name.iloc[24171]
# updated_df.dev_name.iloc[24172]= updated_df.dev_name.iloc[24171]
#
# updated_df.dev_name.iloc[24171]= updated_df.dev_name.iloc[24167]
# updated_df.dev_name.iloc[24170]= updated_df.dev_name.iloc[24167]
# updated_df.dev_name.iloc[24169]= updated_df.dev_name.iloc[24167]
# updated_df.dev_name.iloc[24168]= updated_df.dev_name.iloc[24167]
#
# updated_df.dev_name.iloc[24167]= updated_df.dev_name.iloc[24163]
# updated_df.dev_name.iloc[24166]= updated_df.dev_name.iloc[24163]
# updated_df.dev_name.iloc[24165]= updated_df.dev_name.iloc[24163]
# updated_df.dev_name.iloc[24164]= updated_df.dev_name.iloc[24163]
#
# updated_df.dev_name.iloc[24163]= updated_df.dev_name.iloc[24159]
# updated_df.dev_name.iloc[24162]= updated_df.dev_name.iloc[24159]
# updated_df.dev_name.iloc[24161]= updated_df.dev_name.iloc[24159]
# updated_df.dev_name.iloc[24160]= updated_df.dev_name.iloc[24159]
#
# updated_df.dev_name.iloc[24159]= updated_df.dev_name.iloc[24155]
# updated_df.dev_name.iloc[24158]= updated_df.dev_name.iloc[24155]
# updated_df.dev_name.iloc[24157]= updated_df.dev_name.iloc[24155]
# updated_df.dev_name.iloc[24156]= updated_df.dev_name.iloc[24155]
#
# updated_df.dev_name.iloc[24155]= updated_df.dev_name.iloc[24151]
# updated_df.dev_name.iloc[24154]= updated_df.dev_name.iloc[24151]
# updated_df.dev_name.iloc[24153]= updated_df.dev_name.iloc[24151]
# updated_df.dev_name.iloc[24152]= updated_df.dev_name.iloc[24151]
#
# updated_df.dev_name.iloc[24151]= updated_df.dev_name.iloc[24147]
# updated_df.dev_name.iloc[24150]= updated_df.dev_name.iloc[24147]
# updated_df.dev_name.iloc[24149]= updated_df.dev_name.iloc[24147]
# updated_df.dev_name.iloc[24148]= updated_df.dev_name.iloc[24147]
#
# updated_df.dev_name.iloc[24147]= updated_df.dev_name.iloc[24143]
# updated_df.dev_name.iloc[24146]= updated_df.dev_name.iloc[24143]
# updated_df.dev_name.iloc[24145]= updated_df.dev_name.iloc[24143]
# updated_df.dev_name.iloc[24144]= updated_df.dev_name.iloc[24143]
#
#
#
# updated_df.dev_name.iloc[24143]= updated_df.dev_name.iloc[24140]
# updated_df.dev_name.iloc[24142]= updated_df.dev_name.iloc[24140]
# updated_df.dev_name.iloc[24141]= updated_df.dev_name.iloc[24140]
#
# #======================================================================
#
# updated_df.stor_grpname.iloc[24136]= updated_df.stor_grpname.iloc[24132]
# updated_df.stor_grpname.iloc[24135]= updated_df.stor_grpname.iloc[24132]
# updated_df.stor_grpname.iloc[24134]= updated_df.stor_grpname.iloc[24132]
# updated_df.stor_grpname.iloc[24133]= updated_df.stor_grpname.iloc[24132]
#
# updated_df.stor_grpname.iloc[24132]= updated_df.stor_grpname.iloc[24128]
# updated_df.stor_grpname.iloc[24131]= updated_df.stor_grpname.iloc[24128]
# updated_df.stor_grpname.iloc[24130]= updated_df.stor_grpname.iloc[24128]
# updated_df.stor_grpname.iloc[24129]= updated_df.stor_grpname.iloc[24128]
#
# updated_df.stor_grpname.iloc[24128]= updated_df.stor_grpname.iloc[24124]
# updated_df.stor_grpname.iloc[24127]= updated_df.stor_grpname.iloc[24124]
# updated_df.stor_grpname.iloc[24126]= updated_df.stor_grpname.iloc[24124]
# updated_df.stor_grpname.iloc[24125]= updated_df.stor_grpname.iloc[24124]
#
# updated_df.stor_grpname.iloc[24124]= updated_df.stor_grpname.iloc[24120]
# updated_df.stor_grpname.iloc[24123]= updated_df.stor_grpname.iloc[24120]
# updated_df.stor_grpname.iloc[24122]= updated_df.stor_grpname.iloc[24120]
# updated_df.stor_grpname.iloc[24121]= updated_df.stor_grpname.iloc[24120]
#
# updated_df.stor_grpname.iloc[24120]= updated_df.stor_grpname.iloc[24116]
# updated_df.stor_grpname.iloc[24119]= updated_df.stor_grpname.iloc[24116]
# updated_df.stor_grpname.iloc[24118]= updated_df.stor_grpname.iloc[24116]
# updated_df.stor_grpname.iloc[24117]= updated_df.stor_grpname.iloc[24116]
#
#
# updated_df.stor_grpname.iloc[24116]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24115]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24114]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24113]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24112]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24112]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24173]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24172]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24171]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24170]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24169]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24168]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24167]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24166]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24165]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24164]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24163]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24162]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24161]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24160]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24159]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24158]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24157]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24156]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24155]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24154]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24153]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24152]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24151]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24150]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24149]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24148]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24147]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24146]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24145]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24144]= updated_df.stor_grpname.iloc[24140]
#
# updated_df.stor_grpname.iloc[24143]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24142]= updated_df.stor_grpname.iloc[24140]
# updated_df.stor_grpname.iloc[24141]= updated_df.stor_grpname.iloc[24140]
#
# #===================================================================================
#
# updated_df.port_grpname.iloc[24138]= updated_df.port_grpname.iloc[24137]
# updated_df.port_grpname.iloc[24139]= updated_df.port_grpname.iloc[24137]
# updated_df.port_grpname.iloc[24140]= updated_df.port_grpname.iloc[24137]
#
# #==============================================================
#
# updated_df.init_grpname.iloc[24136]= updated_df.parent_ig.iloc[24136]
# updated_df.init_grpname.iloc[24137]= updated_df.init_grpname.iloc[24136]
# #===================================================================
# updated_df.parent_ig.iloc[24136]= updated_df.parent_ig.iloc[24138]
#
# #====================================================================
#
#
# updated_df.view_last_update_time.iloc[24137]= updated_df.view_last_update_time.iloc[24136]
#
#
# #====================================================================
#
# updated_df.view_name.iloc[24137]= updated_df.view_name.iloc[24136]
#
# #===================================================================
# updated_df.sid.iloc[24136]= updated_df.sid.iloc[0]
# updated_df.sid.iloc[24137]= updated_df.sid.iloc[0]
#
# #=======================================================================
#
#
# updated_df.dev_name.iloc[24136]= updated_df.dev_name.iloc[24132]
# updated_df.dev_name.iloc[24135]= updated_df.dev_name.iloc[24132]
# updated_df.dev_name.iloc[24132]= updated_df.dev_name.iloc[24132]
# updated_df.dev_name.iloc[24131]= updated_df.dev_name.iloc[24132]
#
# updated_df.dev_name.iloc[24130]= updated_df.dev_name.iloc[24128]
# updated_df.dev_name.iloc[24129]= updated_df.dev_name.iloc[24128]
# updated_df.dev_name.iloc[24128]= updated_df.dev_name.iloc[24128]
# updated_df.dev_name.iloc[24127]= updated_df.dev_name.iloc[24128]
#
# updated_df.dev_name.iloc[24126]= updated_df.dev_name.iloc[24120]
# updated_df.dev_name.iloc[24125]= updated_df.dev_name.iloc[24120]
# updated_df.dev_name.iloc[24124]= updated_df.dev_name.iloc[24120]
# updated_df.dev_name.iloc[24123]= updated_df.dev_name.iloc[24120]
#
# updated_df.dev_name.iloc[24122]= updated_df.dev_name.iloc[24116]
# updated_df.dev_name.iloc[24121]= updated_df.dev_name.iloc[24116]
# updated_df.dev_name.iloc[24120]= updated_df.dev_name.iloc[24116]
# updated_df.dev_name.iloc[24119]= updated_df.dev_name.iloc[24116]
#
# updated_df.dev_name.iloc[24118]= updated_df.dev_name.iloc[24112]
# updated_df.dev_name.iloc[24117]= updated_df.dev_name.iloc[24112]
# updated_df.dev_name.iloc[24116]= updated_df.dev_name.iloc[24112]
# updated_df.dev_name.iloc[24115]= updated_df.dev_name.iloc[24112]
#
#
# updated_df.dev_name.iloc[24114]= updated_df.dev_name.iloc[24108]
# updated_df.dev_name.iloc[24113]= updated_df.dev_name.iloc[24108]
# updated_df.dev_name.iloc[24112]= updated_df.dev_name.iloc[24108]
# updated_df.dev_name.iloc[24111]= updated_df.dev_name.iloc[24108]
#
# updated_df.dev_name.iloc[24110]= updated_df.dev_name.iloc[24104]
# updated_df.dev_name.iloc[24109]= updated_df.dev_name.iloc[24104]
# updated_df.dev_name.iloc[24108]= updated_df.dev_name.iloc[24104]
# updated_df.dev_name.iloc[24107]= updated_df.dev_name.iloc[24104]
#
# updated_df.dev_name.iloc[24106]= updated_df.dev_name.iloc[24100]
# updated_df.dev_name.iloc[24105]= updated_df.dev_name.iloc[24100]
# updated_df.dev_name.iloc[24104]= updated_df.dev_name.iloc[24100]
# updated_df.dev_name.iloc[24103]= updated_df.dev_name.iloc[24100]
#
# updated_df.dev_name.iloc[24102]= updated_df.dev_name.iloc[24096]
# updated_df.dev_name.iloc[24101]= updated_df.dev_name.iloc[24096]
# updated_df.dev_name.iloc[24100]= updated_df.dev_name.iloc[24096]
# updated_df.dev_name.iloc[24099]= updated_df.dev_name.iloc[24096]
#
# updated_df.dev_name.iloc[24098]= updated_df.dev_name.iloc[24092]
# updated_df.dev_name.iloc[24097]= updated_df.dev_name.iloc[24092]
# updated_df.dev_name.iloc[24096]= updated_df.dev_name.iloc[24092]
# updated_df.dev_name.iloc[24095]= updated_df.dev_name.iloc[24092]
#
# updated_df.dev_name.iloc[24094]= updated_df.dev_name.iloc[24089]
# updated_df.dev_name.iloc[24093]= updated_df.dev_name.iloc[24089]
# updated_df.dev_name.iloc[24092]= updated_df.dev_name.iloc[24089]
#
#
#
# #===============================================================
#
# updated_df.stor_grpname.iloc[24136]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24135]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24134]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24133]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24132]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24131]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24130]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24129]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24128]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24127]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24126]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24125]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24124]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24123]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24122]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24121]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24120]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24119]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24118]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24117]= updated_df.stor_grpname.iloc[24089]
#
#
# updated_df.stor_grpname.iloc[24116]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24115]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24114]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24113]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24112]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24111]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24110]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24109]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24108]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24107]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24106]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24105]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24104]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24103]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24102]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24101]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24100]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24099]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24098]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24097]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24096]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24095]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24094]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24093]= updated_df.stor_grpname.iloc[24089]
#
# updated_df.stor_grpname.iloc[24092]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24091]= updated_df.stor_grpname.iloc[24089]
# updated_df.stor_grpname.iloc[24090]= updated_df.stor_grpname.iloc[24089]
#
#
# #==========================================================================
#
# updated_df.port_grpname.iloc[24087]= updated_df.port_grpname.iloc[24086]
# updated_df.port_grpname.iloc[24088]= updated_df.port_grpname.iloc[24086]
# updated_df.port_grpname.iloc[24089]= updated_df.port_grpname.iloc[24086]
#
# #==============================================================
#
# updated_df.init_grpname.iloc[24085]= updated_df.parent_ig.iloc[24085]
# updated_df.init_grpname.iloc[24086]= updated_df.init_grpname.iloc[24085]
# #===================================================================
# updated_df.parent_ig.iloc[24085]= updated_df.parent_ig.iloc[24087]
#
# #====================================================================
#
#
# updated_df.view_last_update_time.iloc[24086]= updated_df.view_last_update_time.iloc[24085]
#
#
# #====================================================================
#
# updated_df.view_name.iloc[24086]= updated_df.view_name.iloc[24085]
#
# #===================================================================
# updated_df.sid.iloc[24085]= updated_df.sid.iloc[0]
# updated_df.sid.iloc[24086]= updated_df.sid.iloc[0]
#
# #========================================================================
#
#
# updated_df.dev_name.iloc[24085]= updated_df.dev_name.iloc[24081]
# updated_df.dev_name.iloc[24084]= updated_df.dev_name.iloc[24081]
# updated_df.dev_name.iloc[24083]= updated_df.dev_name.iloc[24081]
# updated_df.dev_name.iloc[24082]= updated_df.dev_name.iloc[24081]
#
# updated_df.dev_name.iloc[24081]= updated_df.dev_name.iloc[24077]
# updated_df.dev_name.iloc[24080]= updated_df.dev_name.iloc[24077]
# updated_df.dev_name.iloc[24079]= updated_df.dev_name.iloc[24077]
# updated_df.dev_name.iloc[24078]= updated_df.dev_name.iloc[24077]
#
# updated_df.dev_name.iloc[24077]= updated_df.dev_name.iloc[24073]
# updated_df.dev_name.iloc[24076]= updated_df.dev_name.iloc[24073]
# updated_df.dev_name.iloc[24075]= updated_df.dev_name.iloc[24073]
# updated_df.dev_name.iloc[24074]= updated_df.dev_name.iloc[24073]
#
# updated_df.dev_name.iloc[24073]= updated_df.dev_name.iloc[24069]
# updated_df.dev_name.iloc[24072]= updated_df.dev_name.iloc[24069]
# updated_df.dev_name.iloc[24071]= updated_df.dev_name.iloc[24069]
# updated_df.dev_name.iloc[24070]= updated_df.dev_name.iloc[24069]
#
# updated_df.dev_name.iloc[24069]= updated_df.dev_name.iloc[24065]
# updated_df.dev_name.iloc[24068]= updated_df.dev_name.iloc[24065]
# updated_df.dev_name.iloc[24067]= updated_df.dev_name.iloc[24065]
# updated_df.dev_name.iloc[24066]= updated_df.dev_name.iloc[24065]
#
#
# updated_df.dev_name.iloc[24065]= updated_df.dev_name.iloc[24061]
# updated_df.dev_name.iloc[24064]= updated_df.dev_name.iloc[24061]
# updated_df.dev_name.iloc[24063]= updated_df.dev_name.iloc[24061]
# updated_df.dev_name.iloc[24062]= updated_df.dev_name.iloc[24061]
#
# updated_df.dev_name.iloc[24061]= updated_df.dev_name.iloc[24057]
# updated_df.dev_name.iloc[24060]= updated_df.dev_name.iloc[24057]
# updated_df.dev_name.iloc[24059]= updated_df.dev_name.iloc[24057]
# updated_df.dev_name.iloc[24058]= updated_df.dev_name.iloc[24057]
#
# updated_df.dev_name.iloc[24057]= updated_df.dev_name.iloc[24053]
# updated_df.dev_name.iloc[24056]= updated_df.dev_name.iloc[24053]
# updated_df.dev_name.iloc[24055]= updated_df.dev_name.iloc[24053]
# updated_df.dev_name.iloc[24054]= updated_df.dev_name.iloc[24053]
#
# updated_df.dev_name.iloc[24053]= updated_df.dev_name.iloc[24049]
# updated_df.dev_name.iloc[24052]= updated_df.dev_name.iloc[24163]
# updated_df.dev_name.iloc[24051]= updated_df.dev_name.iloc[24163]
# updated_df.dev_name.iloc[24050]= updated_df.dev_name.iloc[24163]
#
# updated_df.dev_name.iloc[24049]= updated_df.dev_name.iloc[24159]
# updated_df.dev_name.iloc[24048]= updated_df.dev_name.iloc[24159]
# updated_df.dev_name.iloc[24047]= updated_df.dev_name.iloc[24159]
# updated_df.dev_name.iloc[24046]= updated_df.dev_name.iloc[24159]
#
# updated_df.dev_name.iloc[24045]= updated_df.dev_name.iloc[24155]
# updated_df.dev_name.iloc[24044]= updated_df.dev_name.iloc[24155]
# updated_df.dev_name.iloc[24043]= updated_df.dev_name.iloc[24155]
# updated_df.dev_name.iloc[24042]= updated_df.dev_name.iloc[24155]
#
# updated_df.dev_name.iloc[24041]= updated_df.dev_name.iloc[24151]
# updated_df.dev_name.iloc[24040]= updated_df.dev_name.iloc[24151]
# updated_df.dev_name.iloc[24039]= updated_df.dev_name.iloc[24151]
# updated_df.dev_name.iloc[24038]= updated_df.dev_name.iloc[24151]
#
# updated_df.dev_name.iloc[24037]= updated_df.dev_name.iloc[24147]
# updated_df.dev_name.iloc[24036]= updated_df.dev_name.iloc[24147]
# updated_df.dev_name.iloc[24035]= updated_df.dev_name.iloc[24147]
# updated_df.dev_name.iloc[24034]= updated_df.dev_name.iloc[24147]
#
# updated_df.dev_name.iloc[24033]= updated_df.dev_name.iloc[24143]
# updated_df.dev_name.iloc[24032]= updated_df.dev_name.iloc[24143]
# updated_df.dev_name.iloc[24031]= updated_df.dev_name.iloc[24143]
# updated_df.dev_name.iloc[24030]= updated_df.dev_name.iloc[24143]
#
#
#
# updated_df.dev_name.iloc[24029]= updated_df.dev_name.iloc[24140]
# updated_df.dev_name.iloc[24028]= updated_df.dev_name.iloc[24140]
# updated_df.dev_name.iloc[24027]= updated_df.dev_name.iloc[24140]




print(updated_df)


















# df['view_last_update_time']=df['view_last_update_time'].str.replace(',', ' ')
#
# #renaming columns
#
# renaming_column=df.rename(columns={'symid':'sid'})
# # print(renaming_column)
# renaming_column.view_last_update_time=pd.to_datetime(renaming_column['view_last_update_time'])
#
# updated_df=pd.DataFrame(data=renaming_column,columns=["sid","view_name","view_last_update_time","parent_ig","init_grpname","wwn","user_node_name","user_port_name","filename"])
# # print(updated_df)
# # manipulating data
# manipulating_values = {'sid':updated_df['sid'][0],'view_name':updated_df['view_name'][0],'view_last_update_time':updated_df['view_last_update_time'][0],'parent_ig':'n/a','init_grpname':updated_df['init_grpname'][0],'filename':'showview'}
# # # filling data in NAN(null) values
# filling_nan_values=updated_df.fillna(value=manipulating_values)
#
# print(filling_nan_values)
# engine = create_engine('mysql://root:password@localhost/mysql')
#
# try:
#     with engine.connect() as conn, conn.begin():
#         filling_nan_values.to_sql('vmax_svig', conn, if_exists='append',index=False, dtype={"sid": VARCHAR(64),"view_name": VARCHAR(256),"parent_ig": VARCHAR(256),"init_grpname": VARCHAR(256),"wwn": VARCHAR(32),"user_node_name": VARCHAR(256),"user_port_name": VARCHAR(256),"filename": VARCHAR(512)})
# except:
#     print("Error while connecting to MySQL")
# finally:
#     conn.close()
#     print("MySQL connection is closed")