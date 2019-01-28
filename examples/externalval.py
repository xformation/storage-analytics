import pprint
import pandas as pd
import xmldataset
# from sqlalchemy.types import VARCHAR
# from sqlalchemy import create_engine
ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
xml_data = open('cluster_standalone_listview.xml').read()
# print(xml_data)



# for Vmax_cluster
#
profile="""
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:vxn
            Masking_View
                View_Info
                    view_name = dataset:vxn  
                    view_last_update_time = dataset:vxn
                    init_grpname = dataset:vxn
"""
#
output = xmldataset.parse_using_profile(xml_data,profile)
print(output)
# print(output)
# df=pd.DataFrame.from_records(output['vxn'])
# deleting_nan_values  = df.apply(lambda x: pd.Series(x.dropna().values))

# print(df)