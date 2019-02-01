import pprint
import pandas as pd
import xmldataset
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine

ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint

filex = 'symdev1918'
filename = filex + '.xml'
xml_data = open(filename).read()

profile = """
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:mydata
            Device
                Dev_Info
                    dev_name = dataset:mydata
                    configuration = dataset:mydata
                    device_group = dataset:mydata
                    ld_name = dataset:mydata
                    status = dataset:mydata,name:dev_status
                    attached_bcv = dataset:mydata
                    snapvx_source = dataset:mydata
                    snapvx_target = dataset:mydata
                    thin_pool_name = dataset:mydata
                    SRP_name = dataset:mydata
                Product
                    wwn = dataset:mydata
                Flags
                    snap_save_device = dataset:mydata
                    gatekeeper = dataset:mydata
                    meta = dataset:mydata
                Capacity
                    megabytes = dataset:mydata
                    cylinders = dataset:mydata
                    blocks = dataset:mydata
                    kilobytes = dataset:mydata
                RDF
                    RDF_Info
                        pair_state = dataset:mydata
                        consistency_state = dataset:mydata
                    Mode
                        mode = dataset:mydata
                        adaptive_copy = dataset:mydata
                        adaptive_copy_write_pending = dataset:mydata
                    Status
                        link = dataset:mydata,name:link_status
                        link_status_change_time = dataset:mydata
                    Local
                        ra_group_num = dataset:mydata,name:local_ra_group_num
                    Remote
                        dev_name = dataset:mydata,name:remote_dev_name 
                        remote_symid = dataset:mydata
                        wwn  = dataset:mydata,name:remote_wwn
                        state = dataset:mydata,name:remote_dev_state
         """
output = xmldataset.parse_using_profile(xml_data, profile)
df = pd.DataFrame.from_records(output['mydata'],
                               columns=['symid', 'dev_name', 'configuration', 'device_group', 'ld_name', 'attached_bcv',
                                        'dev_status', 'snapvx_source', 'snapvx_target', 'thin_pool_name', 'SRP_name',
                                        'vdev_tgt', 'wwn', 'snap_save_device', 'gatekeeper', 'meta', 'megabytes',
                                        'cylinders', 'blocks', 'kilobytes', 'pair_state', 'consistency_state', 'mode',
                                        'adaptive_copy', 'adaptive_copy_write_pending', 'link_status',
                                        'link_status_change_time', 'local_ra_group_num', 'remote_dev_name',
                                        'remote_symid', 'remote_wwn', 'remote_dev_state', 'filename'])
# df.drop_duplicates(subset='wwn', keep='first', inplace=True)


# deleting_nan_values = df.apply(lambda x: pd.Series(x.dropna().values))
# deleting_nan_values.drop_duplicates(subset='wwn', keep='first', inplace=True)

manipulating_values = {'symid':df['symid'][0],'device_group':'N/A','ld_name':'N/A','snapvx_source':'N/A', 'snapvx_target':'N/A','vdev_tgt':'N/A','pair_state':'N/A','consistency_state':'N/A',
                       'mode':'N/A','adaptive_copy':'N/A', 'adaptive_copy_write_pending':'N/A', 'link_status':'N/A',
                      'link_status_change_time':'N/A', 'local_ra_group_num':'N/A', 'remote_dev_name':'N/A',
                      'remote_symid':'N/A', 'remote_wwn':'N/A', 'remote_dev_state':'N/A', 'filename':filex}

fillsymid=df.fillna(value=manipulating_values)
engine = create_engine('mysql://root:password@localhost/mysql')
with engine.connect() as conn, conn.begin():
    fillsymid.to_sql('symdev', conn, if_exists='append', index=False)
